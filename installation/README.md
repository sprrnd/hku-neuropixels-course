# HKU Neuropixels Course - Installation Guide
---

 # Installing Miniforge and Python

 **Miniforge** is recommended for installing Python for this course.

 Miniforge is an open-source project that provides a minimal entry point to Python together with the Conda and Mamba package management systems.

 It contains a small selection of pre-configured packages and uses the **conda-forge** channel as its default and only channel.

 This provides a lightweight and reproducible way of managing Python environments.

 ## Installation

 Instructions for installing Miniforge on Windows, Linux, and macOS can be found here:

 https://github.com/conda-forge/miniforge#install

 Alternatively, a step-by-step guide is available here:

 https://biapol.github.io/blog/mara\_lampert/getting\_started\_with\_mambaforge\_and\_python/readme.html

 Install the appropriate version for your operating system.

 After installation, **restart your terminal** so that Miniforge becomes available.

 ### Windows

 On Windows, Conda is not automatically initialised for Command Prompt or PowerShell.

 It is therefore recommended to use the **Miniforge Prompt**.

 ### macOS and Linux

 macOS and Linux users should use their default terminal.

---

 # Conda environments

 When you open the command line after installing Miniforge, you may see something similar to:

```
(base) C:\Users\YourName>
```

 The `(base)` indicates that you are currently in the Conda base environment.

 ## Do not install course packages into `base`

 It is recommended **not to install packages directly into your `base` environment**.

 Installing many packages into `base` can lead to package incompatibilities. If the base environment becomes difficult to repair, you may need to delete and reinstall Miniforge.

 Instead, create a separate environment for each project or course.

---

 # Creating the course environment

 The course repository contains an `environment.yml` file defining the Python environment used during the course.

 First, clone the repository:

```
git clone https://github.com/sprrnd/hku-neuropixels-course.git
```

 Move into the repository:

```
cd hku-neuropixels-course
```

 Create the environment:

```
conda env create -f environment.yml
```

 This will create an environment called:

```
hku-neuropixels-course
```

 Depending on your installation, you can use either `conda` or `mamba` for environment management.

 For example:

```
mamba env create -f environment.yml
```

 > **Note:** Replace `conda` with `mamba` according to your preference. The same environment file can be used with either package manager.

---

 # Activating and deactivating environments

 After installation, activate the course environment:

```
conda activate hku-neuropixels-course
```

 or:

```
mamba activate hku-neuropixels-course
```

 You can deactivate the environment with:

```
conda deactivate
```

 When an environment is active, its name appears before the file directory or username in your terminal.

 For example:

```
(neuropixels-course) C:\Users\YourName\hku-neuropixels-course>
```

 The `(hku-neuropixels-course)` indicates that the course environment is currently active.

---

 # Installing packages manually

 The `environment.yml` file should install the packages required for the course.

 You should therefore **not manually install packages unless instructed to do so**.

 If you need an additional package for your own analysis, install it into the course environment rather than the `base` environment.

---

 # Installing uv

 [`uv`](<https://docs.astral.sh/uv/>) is a fast Python package and project manager.

 It can be used as an alternative to pip for installing Python packages and managing Python environments.

 To install `uv` using Conda:

```
conda install conda-forge::uv
```

 Alternatively:

```
pip install uv
```

 For the course, you can use either `pip` or `uv` where appropriate.

---

 # Installing Git

 Git is used to download and update the course repository.

 If Git is not already installed, download it from:

 https://git-scm.com/downloads

 After installation, check that it is available:

```
git --version
```

 You should see something similar to:

```
git version 2.x.x
```

---

 # Installing Visual Studio Code

 We will use **Visual Studio Code (VS Code)** for the course.

 Download VS Code from:

 https://code.visualstudio.com/

 Install the version appropriate for your operating system.

 After installation, open VS Code.

---

 # VS Code extensions

 The course uses two main VS Code extensions.

 ## Python

 Install the Microsoft Python extension:

 https://marketplace.visualstudio.com/items?itemName=ms-python.python

 ## Jupyter

 Install the Microsoft Jupyter extension:

 https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter

 These extensions allow VS Code to recognise Python environments and run Jupyter notebooks.

---

 # Installation check

 A dedicated notebook is provided to check that your computer and Python environment are correctly configured before starting the course.

 You can find it in:

```
installation/installation_test.ipynb
```

 Please run this notebook **before the course**.

 The notebook checks that the required Python packages are installed and that the course environment is working correctly.

 If all checks pass, you are ready to start the course.

 If any checks fail, please see the Troubleshooting section below.

---

 # SpikeGLX

 SpikeGLX is the acquisition application used in this course.

 Download SpikeGLX from:

 https://billkarsh.github.io/SpikeGLX/#latest-application-downloads

 ## SpikeGLX\_NISIM

 When working through the course exercises, **prioritise using `SpikeGLX_NISIM.exe` rather than `SpikeGLX.exe`** where appropriate.

 Using `SpikeGLX_NISIM.exe` avoids the need to install the National Instruments (NI) drivers required by the hardware acquisition version.

 > **Important:** SpikeGLX is Windows-only.


---

 # NeuroPyxels

 [NeuroPyxels](<https://github.com/m-beau/NeuroPyxels>) is a Python library for loading, processing, and plotting Neuropixels data.

 Follow the installation instructions provided by the project:

 https://github.com/m-beau/NeuroPyxels#%EF%B8%8F-installation

 NeuroPyxels will be used for selected data loading, processing, and visualisation exercises.

---

 # Phy

 Phy is the main manual curation tool used in the course for inspecting and curating spike-sorting results.

 Phy provides an interactive interface for examining:

 - Spike waveforms
- Cluster quality
- Firing rates
- Templates
- Feature distributions
- Cluster assignments
- Other properties of sorted units

 Installation instructions:

 https://phy.readthedocs.io/en/latest/installation/

 GitHub:

 https://github.com/cortex-lab/phy

 Phy can also be installed from the course Python environment.

---

 # Bombcell

 Bombcell provides automated quality metrics and curation tools for spike-sorted electrophysiology data.

 The course uses the **Python version of Bombcell**.

 Installation instructions:

 https://github.com/Julie-Fabre/bombcell#python

 After installation, please run the sample Jupyter notebook provided in the Bombcell repository:

 https://github.com/Julie-Fabre/bombcell#-quick-start-guide

 Running the example notebook before the course will help ensure that Bombcell is correctly installed and that its dependencies are working.

---

 # SpikeInterface

 SpikeInterface is a Python framework for creating flexible and reproducible spike-sorting workflows.

 It provides tools for:

 - Reading electrophysiology data
- Preprocessing
- Spike sorting
- Waveform extraction
- Quality metrics
- Visualisation
- Comparing sorting results
- Curation and post-processing

 Documentation:

 https://spikeinterface.readthedocs.io/

 GitHub:

 https://github.com/SpikeInterface/spikeinterface

 A common import used in the course is:

```
import spikeinterface.full as si
```

 SpikeInterface supports a range of electrophysiology formats and spike sorters and provides a unified interface for many parts of the analysis pipeline.

---

 # IBL Neuropixels

 The International Brain Laboratory (IBL) provides tools and standards for working with large-scale neuroscience datasets, including Neuropixels recordings.

 The `ibl-neuropixel` package contains tools for working with Neuropixels 1.0 and 2.0 data.

 GitHub:

 https://github.com/int-brain-lab/ibl-neuropixel

 The package will be used for selected Neuropixels-specific analyses.

---

 # Pinpoint

 Pinpoint is a tool for interacting with and exploring neuroscience datasets.

 Pinpoint can be run directly in a desktop browser:

 https://data.virtualbrainlab.org/Pinpoint/

 Alternatively, Pinpoint can be downloaded from Steam:

 https://store.steampowered.com/app/2434260/Pinpoint/

 The course may use Pinpoint for exploring and visualising datasets.

---

 # Using the environment in VS Code

 Open the course repository in VS Code.

 From the repository directory, you can run:

```
code .
```

 Alternatively:

 1. Open VS Code.
2. Select **File → Open Folder...**
3. Select the `hku-neuropixels-course` folder.

---

 ## Selecting the Python interpreter

 In VS Code:

 1. Open a Python file or Jupyter notebook.
2. Open the Command Palette:
   - **Windows/Linux:** `Ctrl+Shift+P`
   - **macOS:** `Cmd+Shift+P`
3. Search for:

```
Python: Select Interpreter
```

 4. Select:

```
hku-neuropixels-course
```

 The selected interpreter should correspond to the Python installation inside your Conda environment.

---

 # Selecting the Jupyter kernel

 When you open a `.ipynb` notebook in VS Code, you will see a kernel/interpreter selector near the top-right of the notebook.

 Select:

```
hku-neuropixels-course
```

 or the corresponding Python 3.11 environment.

 > **Important:** Selecting the correct Jupyter kernel is one of the most common sources of problems when working with notebooks. If an import works in your terminal but fails in a notebook, first check which kernel the notebook is using.


 # Working with the notebooks

 The course notebooks are intended to be run in order unless otherwise specified.

 Before starting a notebook:

 1. Activate the Conda environment.
2. Open the repository in VS Code.
3. Select the `hku-neuropixels-course` Python environment.
4. Open the notebook.
5. Select the `hku-neuropixels-course` Jupyter kernel.

 For example:

```
conda activate hku-neuropixels-course
cd hku-neuropixels-course
code .
```

 Then open the appropriate notebook from the `notebooks/` directory.


---


 # Git and the course repository


 ## Clone the repository

```
git clone https://github.com/sprrnd/hku-neuropixels-course.git
```

 ## Update your local copy

 If the instructor adds new notebooks or fixes an error:

```
git pull
```

 Run this from inside the repository:

```
cd hku-neuropixels-course
git pull
```

 > **Important:** If you have modified course files locally, `git pull` may produce conflicts. If you are unsure what to do, do not delete or overwrite your work—ask the course instructor.


---

 # Useful resources

 ## Miniforge

 https://github.com/conda-forge/miniforge

 ## Python

 https://docs.python.org/3/

 ## uv

 https://docs.astral.sh/uv/

 ## Visual Studio Code

 https://code.visualstudio.com/

 ## NumPy

 https://numpy.org/

 ## SciPy

 https://scipy.org/

 ## pandas

 https://pandas.pydata.org/

 ## Matplotlib

 https://matplotlib.org/

 ## scikit-learn

 https://scikit-learn.org/

 ## Jupyter

 https://jupyter.org/

 ## SpikeGLX

 https://billkarsh.github.io/SpikeGLX/

 ## CatGT

 https://billkarsh.github.io/SpikeGLX/#catgt

 ## NeuroPyxels

 https://github.com/m-beau/NeuroPyxels

 ## Kilosort

 https://github.com/MouseLand/Kilosort

 ## Phy

 Documentation:

 https://phy.readthedocs.io/

 GitHub:

 https://github.com/cortex-lab/phy

 ## Bombcell

 https://github.com/Julie-Fabre/bombcell

 ## SpikeInterface

 Documentation:

 https://spikeinterface.readthedocs.io/

 GitHub:

 https://github.com/SpikeInterface/spikeinterface

 ## IBL Neuropixels

 https://github.com/int-brain-lab/ibl-neuropixel

 ## Pinpoint

 Browser:

 https://data.virtualbrainlab.org/Pinpoint/

 Steam:

 https://store.steampowered.com/app/2434260/Pinpoint/

---

 # Before the course

 Please complete the following setup **before arriving at the course**.

 ## Computer and software

- [ ] Miniforge is installed
- [ ] Git is installed
- [ ] VS Code is installed
- [ ] VS Code Python extension is installed
- [ ] VS Code Jupyter extension is installed

 ## Python environment

 - [ ] Course repository has been cloned
- [ ] `environment.yml` has been used to create the environment
- [ ] `hku-neuropixels-course` environment activates successfully
- [ ] Python reports version 3.11.x
- [ ] The installation check notebook runs successfully
- [ ] All checks in the installation check notebook pass

 ## Neuropixels software

 - [ ] SpikeGLX is installed
- [ ] NeuroPyxels is installed
- [ ] Phy is installed
- [ ] Bombcell Python version is installed
- [ ] SpikeInterface is installed
- [ ] IBL Neuropixels tools are installed

 ## Notebooks

 - [ ] A course notebook opens successfully in VS Code
- [ ] The `hku-neuropixels-course` Jupyter kernel is available
- [ ] A course notebook runs successfully

 If you encounter problems, please resolve them before the course where possible. If you cannot resolve an issue, bring the error message and details of your setup to the course.

