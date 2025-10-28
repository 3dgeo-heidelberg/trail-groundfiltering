# Installation and Download

In this workshop, we will use 

- the [AFwizard](https://github.com/ssciwr/afwizard) library for advanced ground point filtering in LiDAR data, and
- [HELIOS++](https://github.com/3dgeo-heidelberg/helios) for LiDAR simulation.

First, we will download the data and code. We then install Miniforge, a distribution of the `conda` and `mamba` package managers. This will allow us to install and manage Python and the required libraries in a dedicated environment. In addition, we will install LAStools, a popular toolbox for LiDAR data processing, which is required by a module in AFwizard.

If you have any questions or problems with installation, please contact [Hannah Weiser](https://www.geog.uni-heidelberg.de/en/people-at-the-institute/hannah-weiser).

## 1. Dataset and Code

[Download (heiBOX)](https://heibox.uni-heidelberg.de/d/5fb2dbf7edbe44669630){target="_blank" .md-button .md-button--primary}

Instructions:

- Click on the "Download data (heiBOX)" link above and download as "ZIP" (green button).
- Unzip the archive to a folder named `trail-groundfiltering` (i.e., keep the default name). Note down the path to this folder, as you will need it later (see [Section 4.4](#4-mamba-environment-with-needed-libraries)).
- Now you are all set up and have both the scripts (`.ipynb` and `.py` files) and data (in the `data` subfolder).


## 2. Mamba

Mamba is a fast, robust, and cross-platform package manager. As [recommended by the developers](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html), we will install Mamba through the Miniforge distribution. Follow the instructions from this page:
[Mamba Installation](https://github.com/conda-forge/miniforge?tab=readme-ov-file#install). We provide a short summary below.

Here is the direct link to the Windows installer: [https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe). Follow the prompts, taking note of the option to "Create start menu shortcuts".

For installation on Unix-like platforms, follow the instructions at: [https://github.com/conda-forge/miniforge?tab=readme-ov-file#unix-like-platforms-macos-linux--wsl](https://github.com/conda-forge/miniforge?tab=readme-ov-file#unix-like-platforms-macos-linux--wsl). 


## 3. LAStools

**LAStools** is a widely used and efficient toolbox for processing LiDAR data in LAS/LAZ format. It includes tools for filtering, classification, tiling, conversion, and much more. All registered workshop participants will receive a free LAStools license valid for 4 weeks during the in-person workshop.

- Download LAStools v2.0.0 from the following URL: [https://github.com/LAStools/LAStools/releases/download/v2.0.0/LAStools.zip](https://github.com/LAStools/LAStools/releases/download/v2.0.0/LAStools.zip). IMPORTANT: Use this specific version to ensure compatibility with AFwizard. The newest LAStools version will not work in the demo or trial license version.
- After downloading, extract the contents of the ZIP/TAR archive to a directory of your choice, e.g., `C:\LAStools`. Remember this path, as you will later need to set it in the AFwizard notebooks.

If you are on Linux or Mac OS, install LAStools using "Wine" as described here: [https://rapidlasso.de/using-lastools-on-mac-os-x-with-wine/](https://rapidlasso.de/using-lastools-on-mac-os-x-with-wine/). In step 2 of this tutorial, download LAStools v2.0.0 as indicated above instead of the version linked in the tutorial.

## 4. Mamba environment with needed libraries

To create a Mamba environment with the necessary libraries, follow these steps:

1. Open a terminal (**Miniforge Prompt** on Windows, Terminal on macOS/Linux).
2. Create a new `mamba` environment named `groundfiltering` with Python 3.13, AFwizard and HELIOS++:
    
    ```bash
    mamba create -n groundfiltering python afwizard helios=2.0.2 rasterio laspy scipy -c conda-forge
    ```
    This might take a few minutes (for lower end devices up to 20 minutes) as `mamba` resolves dependencies and downloads the required packages. Just be patient and wait.
3. Close Miniforge. Reopen the Miniforge prompt and activate the newly created environment by typing:

    ```bash
    mamba activate groundfiltering
    ```

4. Change to your `trail-groundfiltering` directory (see [Section 1](#1-dataset-and-code)) and start Jupyter Lab:
    
    ```bash
    cd path/to/trail-groundfiltering
    jupyter-lab
    ```

5. Open the imports notebook and execute the code cell to verify the installation. In the workshop, use steps 1, 3 and 4 to start Jupyter Lab and open the notebooks.


## Troubleshooting

- **Issue** when trying to activate the environment:
   
   ```
   critical libmamba Shell not initialized
   
   'mamba' is running as a subprocess and can't modify the parent shell.
    Thus you must initialize your shell before using activate and deactivate.
   ```
  
  - **Solution**: Close and reopen the Miniforge prompt and try again.

## Further information (advanced)


### Git repository 

This website is hosted on GitHub: [https://github.com/3dgeo-heidelberg/trail-groundfiltering](https://github.com/3dgeo-heidelberg/trail-groundfiltering)

If you have `git` installed, you can also clone the repository using:
```
git clone https://github.com/3dgeo-heidelberg/trail-groundfiltering.git
```

You find the scripts in the `docs` folder and would need to place the data in the `data` subfolder.


### Useful terminal commands

- To navigate between folders use `cd` (*change directory*): `cd "C:\my folder\my sub-folder"`
ATTENTION: if your folders or files **contain spaces**, you should use quotation marks **" "**.

- To list existing environments : `mamba env list`

- To activate an environment :  `mamba activate __my_environment__` (in our case: `mamba activate groundfiltering`)

- To open Jupyter notebooks : `jupyter-lab __my_notebook__.ipynb`

- To list dependencies *once you are in an active environement*: `mamba list`

- ... something is missing - we can add it on the go (provided that we're inside an active environment) : `mamba install __my_package__`

### Additional resources

For more information using `mamba` and `conda`, you can refer to the following resources:

- [Mamba user guide](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#mamba)
- [Conda documentation](https://docs.conda.io/en/latest/)

If you want to use LAStools standalone, you can find the documentation here:

- [LAStools documentation](https://downloads.rapidlasso.de/html/index.html)