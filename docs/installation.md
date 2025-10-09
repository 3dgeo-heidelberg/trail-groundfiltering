# Installation of software

In this workshop, we will use 
- the [AFwizard](https://github.com/ssciwr/afwizard) library for advanced ground point filtering in LiDAR data, and
- [HELIOS++](https://github.com/3dgeo-heidelberg/helios) for LiDAR simulation.

First, we will install Miniforge, a distribution of the `conda` and `mamba` package managers. This will allow us to install and manage Python and the required libraries in a dedicated environment. In addition, we will install LAStools, a popular toolbox for LiDAR data processing, which is required by a module in AFwizard.

## 1. Mamba

Mamba is a fast, robust, and cross-platform package manager. As [recommended by the developers](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html), we will install Mamba through the Miniforge distribution. Follow the instructions from this page:
[Mamba Installation](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install). We provide a short summary below.

Here is the direct link to the Windows installer: https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe. Follow the prompts, taking note of the option to "Create start menu shortcuts".


## 2. LAStools

**LAStools** is a widely used and efficient toolbox for processing LiDAR data in LAS/LAZ format. It includes tools for filtering, classification, tiling, conversion, and much more.

- Download LAStools from the official site (select the appropriate operating system):
  [https://rapidlasso.de/downloads/](https://rapidlasso.de/downloads/)
- After downloading, extract the contents of the ZIP/TAR archive to a directory of your choice, e.g., `C:\LAStools`. Remember this path, as you will later need to set it in the AFwizard notebooks.

## 3. Mamba environment with needed libraries

To create a Mamba environment with the necessary libraries, follow these steps:

1. Open a terminal (**Miniforge Prompt** on Windows, Terminal on macOS/Linux).
2. Create a new `mamba` environment named `groundfiltering` with Python 3.13, AFwizard and HELIOS++:
```bash
mamba create -n groundfiltering python afwizard helios=2.0.2 rasterio laspy -c conda-forge
```
3. Activate the newly created environment:
```bash
mamba activate groundfiltering
```
4. Open the imports notebook to verify the installation:
```bash
cd path/to/TRAIL_GROUNDFILTERING/docs
jupyter-lab imports.ipynb
```

## Additional resources (not needed for the workshop)

For more information using `mamba` and `conda`, you can refer to the following resources:
- [Mamba user guide](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#mamba)
- [Conda documentation](https://docs.conda.io/en/latest/)

If you want to use LAStools standalone, you can find the documentation here:
- [LAStools documentation](https://downloads.rapidlasso.de/html/index.html)

## Troubleshooting

