import os
from pathlib import Path
import time
import matplotlib.pyplot as plt
import matplotlib
from ipywidgets import interact
import pyhelios
from pyhelios import SimulationBuilder
import numpy as np
from osgeo import gdal
import rasterio as rio
import laspy

def tellme(s):
    plt.title(s, fontsize=12)
    plt.draw()

    
def read_raster(raster_file):
    with rio.open(raster_file) as src:
        dem = src.read(1, masked=True)
        tf = src.transform
        bounds = src.bounds
        width= src.width
        height = src.height
    origin_left, origin_bottom, origin_right, origin_top = bounds
    
    return dem, tf, bounds, origin_left, origin_bottom, origin_right, origin_top


def interactive_flight_trajectory(dtm, tf, n_pos=4):
    plt.figure(figsize=(10, 8))

    zoom_out = 100
    
    plt.imshow(dtm, cmap='terrain')
    plt.colorbar(label="terrain height [m]")

    plt.axis('equal')

    ax = plt.gca()
    ax.set_xlim([-zoom_out, np.shape(dtm)[1]+zoom_out])
    ax.set_ylim([np.shape(dtm)[0]+zoom_out, -zoom_out])

    tellme('Select the trajectory of the aircraft carrying the virtual laser scanner.')

    plt.waitforbuttonpress()

    while True:
        pt = []
        while len(pt) < n_pos:
            tellme(f'Please choose {n_pos} positions with the mouse.')
            pt = np.asarray(plt.ginput(n_pos, timeout=-1))
        for k in range(n_pos):
            if k % 2 != 0 or k == n_pos:
                continue
            line = plt.plot([pt[k][0], pt[k+1][0]], [pt[k][1], pt[k+1][1]], label=f'Pass {int(k/2)+1}', color='steelblue')  # 'firebrick'
            ar_length = 10000
            arrow = plt.arrow(pt[k+1][0], pt[k+1][1], -(pt[k][0]-pt[k+1][0])/ar_length, (pt[k+1][1]-pt[k][1])/ar_length, head_width=50, edgecolor='none', facecolor='steelblue')
        plt.legend()

        tellme('Happy?\nKeypress for "Yes", mouseclick for "No"')

        if plt.waitforbuttonpress(timeout=-1):
            plt.close()
            break

        ax = plt.gca()

        for art in ax.get_children():
            if isinstance(art, matplotlib.patches.FancyArrow) or isinstance(art, matplotlib.lines.Line2D):
                art.remove()
    
    waypoints = []
    for i in range(len(pt)):
        x, y = tf * (pt[i][0], pt[i][1])
        waypoints.append([x, y])
                 
    print(f"You have chosen your flight lines.\n{[[float(np.round(x, 2)), float(np.round(y, 2))] for x, y in waypoints]}")
    
    return waypoints

def find_playback_dir(survey_path, output_folder='output', helios_root=None):
    if not helios_root:
        helios_root = os.getcwd()
    playback = Path(helios_root) / output_folder
    with open(Path(helios_root) / survey_path, 'r') as sf:
        for line in sf:
            if '<survey name' in line:
                survey_name = line.split('name="')[1].split('"')[0]
    if not (playback / survey_name).is_dir():
        raise FileNotFoundError('Could not locate output directory')
    last_run_dir = sorted(list((playback / survey_name).glob('*')), key=lambda f: f.stat().st_ctime, reverse=True)[0]
    return last_run_dir

def read_strip(path):
    las = laspy.read(path)
    pc = np.array([las.x, las.y, las.z]).T
    object_id = las["hitObjectId"]
    gps_time = las["gps_time"]
    classification = las["classification"]

    return pc, object_id, gps_time, classification


def add_support_points(waypoints):
    indices = np.arange(0, waypoints.shape[0], 2)
    new_waypoints = []
    for idx in indices:
        wp = waypoints[idx, :]
        new_waypoints.append(wp)
        wp2 = waypoints[idx+1, :]
        new_wp = wp + (wp2[:2] - wp[:2]) / 2
        new_waypoints.append(new_wp)
        new_waypoints.append(wp2)

    return new_waypoints


def waypoints_above_ground(waypoints, dtm_file, height_agl):
    src = rio.open(dtm_file)
    mean_dtm_height = np.mean(src.read(1, masked=True))
    vals = np.array([z for z in src.sample(waypoints)])[:, 0]
    vals[vals < 0] = mean_dtm_height
    vals += height_agl
    
    return np.column_stack((waypoints, vals))
