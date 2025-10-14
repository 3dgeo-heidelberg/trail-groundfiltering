# Installation and Download

In this workshop, we will use 

- the [AFwizard](https://github.com/ssciwr/afwizard) library for advanced ground point filtering in LiDAR data, and
- [HELIOS++](https://github.com/3dgeo-heidelberg/helios) for LiDAR simulation.

First, we will install Miniforge, a distribution of the `conda` and `mamba` package managers. This will allow us to install and manage Python and the required libraries in a dedicated environment. In addition, we will install LAStools, a popular toolbox for LiDAR data processing, which is required by a module in AFwizard.


## 1. Dataset and Code

[Download (heiBOX)](https://heibox.uni-heidelberg.de/d/5fb2dbf7edbe44669630){ .md-button .md-button--primary }

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

**LAStools** is a widely used and efficient toolbox for processing LiDAR data in LAS/LAZ format. It includes tools for filtering, classification, tiling, conversion, and much more. All registered workshop participants will receiva a free LAStools license valid for 4 weeks."

- Download LAStools from the official site (select the appropriate operating system):
  [https://rapidlasso.de/downloads/](https://rapidlasso.de/downloads/)
- After downloading, extract the contents of the ZIP/TAR archive to a directory of your choice, e.g., `C:\LAStools`. Remember this path, as you will later need to set it in the AFwizard notebooks.

## 4. Mamba environment with needed libraries

To create a Mamba environment with the necessary libraries, follow these steps:

1. Open a terminal (**Miniforge Prompt** on Windows, Terminal on macOS/Linux).
2. Create a new `mamba` environment named `groundfiltering` with Python 3.13, AFwizard and HELIOS++:
    
    ```bash
    mamba create -n groundfiltering python afwizard helios=2.0.2 rasterio laspy scipy -c conda-forge
    ```
    This might take a few minutes as `mamba` resolves dependencies and downloads the required packages. Just be patient and wait.
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


## Additional resources (not needed for the workshop)

For more information using `mamba` and `conda`, you can refer to the following resources:

- [Mamba user guide](https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#mamba)
- [Conda documentation](https://docs.conda.io/en/latest/)

If you want to use LAStools standalone, you can find the documentation here:

- [LAStools documentation](https://downloads.rapidlasso.de/html/index.html)

## Troubleshooting

- **Issue**: `critical libmamba Shell not initialized` when trying to activate the environment.
  - **Solution**: Close the prompt, reopen the Miniforge prompt and try again.

## Further information (advancced)

This website is hosted on GitHub: [https://github.com/3dgeo-heidelberg/trail-groundfiltering](https://github.com/3dgeo-heidelberg/trail-groundfiltering)

If you have `git` installed, you can also clone the repository using:
```
git clone https://github.com/3dgeo-heidelberg/trail-groundfiltering.git
```

You find the scripts in the `docs` folder and would need to place the data in the `data` subfolder.