# HKU Neuropixels Course

 This repository contains the software environment, example notebooks, exercises, and reference material for the **HKU Neuropixels Course**.

 The course introduces practical analysis of Neuropixels electrophysiology data, from raw preprocessing through spike sorting, quality control and downstream analysis.

 We will use a combination of Python-based tools and dedicated Neuropixels software, including:

 - SpikeGLX
- CatGT
- NeuroPyxels
- Kilosort
- Phy
- Bombcell
- SpikeInterface
- IBL Neuropixels tools
- Jupyter notebooks

 The repository is designed so that participants can:

 - Install and test the required software before the course.
- Clone the course repository.
- Run the example Jupyter notebooks.
- Complete the analysis exercises.
- Use the repository as a reference after the course.

---

 # Operating System

 ## Windows is required for this course

 Some of the software used in this course is **Windows-only**, in particular:

 - SpikeGLX
- CatGT

 Please ensure that you are running **Windows 10 or above** if you want to follow the complete course workflow.

 Participants using macOS or Linux may be able to complete some of the Python-based analysis exercises, but they will **not be able to run all of the acquisition and preprocessing software used in this course**.

 For the full course experience, a Windows 10/11 computer is therefore recommended.

---

 # Contents

 - Important: Operating System
- Recommended computer setup
- Software overview
- Installing Miniforge and Python
- Creating the course environment
- Installing uv
- Installing Git
- Installing Visual Studio Code
- VS Code extensions
- Installation check
- SpikeGLX
- CatGT
- NeuroPyxels
- Kilosort
- Phy
- Bombcell
- SpikeInterface
- IBL Neuropixels
- Pinpoint
- Using the environment in VS Code
- Using JupyterLab
- Course repository structure
- Working with the notebooks
- Data
- File paths
- Git and the course repository
- Troubleshooting
- Reproducibility
- Useful resources
- Before the course
- Course philosophy
- Questions and problems
- Acknowledgements

---

 # Recommended computer setup

 Neuropixels datasets can be large, and some analysis steps can require substantial memory, storage, and CPU resources.

 As a general recommendation:

 - **Operating system:** Windows 10 or Windows 11
- **RAM:** 16 GB minimum; 32 GB or more recommended
- **Storage:** SSD strongly recommended
- **Free disk space:** at least 50 GB; more may be required for larger Neuropixels datasets
- **CPU:** a modern multi-core processor is recommended

 The exact requirements will depend on the size of the datasets used during the course.

 > **Important:** Raw Neuropixels recordings can be very large. Do not assume that a dataset will fit comfortably on a laptop simply because the corresponding notebook is small.

---

 # Software overview

 The course uses several different types of software.

 ## Acquisition and preprocessing

 ### SpikeGLX

 SpikeGLX is the acquisition application used with Neuropixels probes.

 ### CatGT

 CatGT is used for preprocessing Neuropixels recordings acquired with SpikeGLX.

 Both SpikeGLX and CatGT are Windows-only.

---

 ## Python-based analysis

 The course Python environment includes:

 - NumPy
- SciPy
- pandas
- Matplotlib
- scikit-learn
- JupyterLab
- IPython kernel
- h5py
- tqdm
- PyYAML
- SpikeInterface
- Phy
- IBL Neuropixels tools
- NeuroPyxels
- Bombcell

---

 ## Spike sorting and curation

 The course also introduces:

 - Kilosort for spike sorting
- Phy for manual curation
- Bombcell for automated quality metrics and curation
- SpikeInterface for building and managing spike-sorting workflows

---

 # Installing Miniforge and Python

 ## Why Miniforge?

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

 This has several advantages:

 - Package requirements are isolated.
- Different projects can use different Python versions.
- Package conflicts are less likely to affect other projects.
- Environments can be recreated from an environment file.
- The software environment used for an analysis can be documented and shared.

---

 # Creating the course environment

 The course repository contains an `environment.yml` file defining the Python environment used during the course.

 First, clone the repository:

```
git clone https://github.com/YOUR-USERNAME/neuropixels-course.git
```

 Move into the repository:

```
cd neuropixels-course
```

 Create the environment:

```
conda env create -f environment.yml
```

 This will create an environment called:

```
neuropixels-course
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
conda activate neuropixels-course
```

 or:

```
mamba activate neuropixels-course
```

 You can deactivate the environment with:

```
conda deactivate
```

 When an environment is active, its name appears before the file directory or username in your terminal.

 For example:

```
(neuropixels-course) C:\Users\YourName\neuropixels-course>
```

 The `(neuropixels-course)` indicates that the course environment is currently active.

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
notebooks/00_installation_check.ipynb
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

 # CatGT

 CatGT is a preprocessing tool commonly used with Neuropixels data acquired using SpikeGLX.

 Download CatGT and read the documentation here:

 https://billkarsh.github.io/SpikeGLX/#catgt

 > **Important:** CatGT is Windows-only.

 The course will provide examples of using CatGT to prepare Neuropixels recordings for downstream analysis.

---

 # NeuroPyxels

 [NeuroPyxels](<https://github.com/m-beau/NeuroPyxels>) is a Python library for loading, processing, and plotting Neuropixels data.

 Follow the installation instructions provided by the project:

 https://github.com/m-beau/NeuroPyxels#%EF%B8%8F-installation

 NeuroPyxels will be used for selected data loading, processing, and visualisation exercises.

---

 # Kilosort

 Kilosort is a powerful spike-sorting tool designed for large-scale electrophysiological recordings, including Neuropixels data.

 The course may use Kilosort for spike sorting and subsequent analysis of the resulting units.

 Installation instructions and documentation:

 https://github.com/MouseLand/Kilosort

 Please follow the installation instructions provided by the Kilosort project.

 > **Note:** Kilosort installation requirements can depend on the version being used and on your GPU configuration. Follow the version-specific installation instructions rather than installing an arbitrary version.

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
3. Select the `neuropixels-course` folder.

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
neuropixels-course
```

 The selected interpreter should correspond to the Python installation inside your Conda environment.

---

 # Selecting the Jupyter kernel

 When you open a `.ipynb` notebook in VS Code, you will see a kernel/interpreter selector near the top-right of the notebook.

 Select:

```
neuropixels-course
```

 or the corresponding Python 3.11 environment.

 > **Important:** Selecting the correct Jupyter kernel is one of the most common sources of problems when working with notebooks. If an import works in your terminal but fails in a notebook, first check which kernel the notebook is using.

---

 # Using JupyterLab

 You can also run the notebooks using JupyterLab.

 First activate the course environment:

```
conda activate neuropixels-course
```

 Then start JupyterLab:

```
jupyter lab
```

 A browser window should open automatically.

 If it does not, JupyterLab will display a URL in the terminal that you can copy into your browser.

 To stop JupyterLab, return to the terminal and press:

```
Ctrl+C
```

---

 # Course repository structure

 The repository will generally be organised as follows:

```
neuropixels-course/
│
├── README.md
├── environment.yml
├── .gitignore
│
├── notebooks/
│   ├── 00_installation_check.ipynb
│   ├── 01_python_and_numpy.ipynb
│   ├── 02_loading_data.ipynb
│   ├── 03_visualising_neuropixels.ipynb
│   ├── 04_preprocessing.ipynb
│   ├── 05_spike_sorting.ipynb
│   └── 06_unit_analysis.ipynb
│
├── exercises/
│   └── ...
│
├── scripts/
│   └── ...
│
└── data/
    └── README.md
```

 The exact notebook structure may change as the course develops.

---

 # Working with the notebooks

 The course notebooks are intended to be run in order unless otherwise specified.

 Before starting a notebook:

 1. Activate the Conda environment.
2. Open the repository in VS Code.
3. Select the `neuropixels-course` Python environment.
4. Open the notebook.
5. Select the `neuropixels-course` Jupyter kernel.

 For example:

```
conda activate neuropixels-course
cd neuropixels-course
code .
```

 Then open the appropriate notebook from the `notebooks/` directory.

---

 # Running a notebook

 In VS Code, cells can be run individually using the **Run Cell** button.

 You can also use:

 - `Shift + Enter` to run a cell and move to the next cell.
- `Ctrl + Enter` / `Cmd + Enter` to run a cell without moving.

 Before running the entire notebook, it is often useful to run the cells sequentially so that you understand what each step is doing.

---

 # Restarting a notebook

 If a notebook gets into an unexpected state, restart the Python kernel.

 In VS Code:

 **Notebook → Restart Kernel**

 Then run the cells again from the beginning.

 This is particularly useful if variables have been modified or overwritten during an exercise.

---

 # Data

 The course repository may contain links or instructions for downloading example Neuropixels datasets.

 Large raw datasets will generally **not** be stored directly in this Git repository.

 This is intentional.

 Git repositories are not appropriate for storing large electrophysiology recordings.

 Instead, datasets should be downloaded separately and stored locally.

 For example:

```
neuropixels-course/
│
├── notebooks/
├── exercises/
├── scripts/
│
└── data/
    ├── example_dataset/
    └── README.md
```

 The `data/` directory should normally be excluded from Git using `.gitignore`.

---

 # File paths

 When working with Neuropixels datasets, you will frequently need to specify file and folder paths.

 For example:

```
from pathlib import Path

data_folder = Path("data/example_dataset")
```

 Using `pathlib.Path` is recommended because it works well across Windows, macOS, and Linux.

 Avoid hard-coding paths such as:

```
data_folder = "C:\\Users\\John\\Desktop\\data"
```

 because these paths will only work on a particular computer.

 Instead, use paths relative to the course repository whenever possible.

---

 # Git and the course repository

 If you are unfamiliar with Git, you do not need to learn the entire Git system to complete the course.

 The most important operations are:

 ## Clone the repository

```
git clone https://github.com/YOUR-USERNAME/neuropixels-course.git
```

 ## Update your local copy

 If the instructor adds new notebooks or fixes an error:

```
git pull
```

 Run this from inside the repository:

```
cd neuropixels-course
git pull
```

 > **Important:** If you have modified course files locally, `git pull` may produce conflicts. If you are unsure what to do, do not delete or overwrite your work—ask the course instructor.

---

 # Updating the environment

 If the instructor changes `environment.yml`, you may need to update your environment.

 Run:

```
conda activate neuropixels-course
conda env update -f environment.yml
```

 or:

```
mamba activate neuropixels-course
mamba env update -f environment.yml
```

 Only update the environment when instructed to do so, as changes to the environment during the course can sometimes introduce compatibility issues.

---

 # Troubleshooting

 ## `conda` is not recognised

 If you see an error such as:

```
conda: command not found
```

 or on Windows:

```
'conda' is not recognized as an internal or external command
```

 First make sure that you have restarted your terminal after installing Miniforge.

 On Windows, open the **Miniforge Prompt** rather than Command Prompt or PowerShell.

 Then try:

```
conda --version
```

---

 ## The `neuropixels-course` environment does not appear

 Check the available Conda environments:

```
conda env list
```

 You should see something similar to:

```
base
neuropixels-course
```

 If the environment is missing, recreate it:

```
conda env create -f environment.yml
```

---

 ## Python is the wrong version

 Activate the course environment:

```
conda activate neuropixels-course
```

 Then check:

```
python --version
```

 The result should be Python 3.11.x.

 If VS Code reports a different version, check the selected Python interpreter.

---

 ## A package cannot be imported

 For example:

```
ModuleNotFoundError: No module named 'spikeinterface'
```

 First check that the correct environment is active:

```
conda activate neuropixels-course
```

 Then run the installation check notebook:

```
notebooks/00_installation_check.ipynb
```

 If the package is installed but the notebook still cannot find it, check the Jupyter kernel selected in VS Code.

---

 ## The notebook uses the wrong Python environment

 This is a very common issue.

 In VS Code:

 1. Open the notebook.
2. Click the kernel selector at the top right.
3. Select:

```
neuropixels-course
```

 If necessary, restart the kernel and run the notebook again.

---

 ## Jupyter is not installed

 Check:

```
jupyter --version
```

 If the command is not available, make sure the course environment is active:

```
conda activate neuropixels-course
```

 Then check again.

---

 ## SpikeGLX or CatGT will not run

 First confirm that you are using:

 - Windows 10 or later
- A supported version of the software
- The correct executable

 For SpikeGLX, consider using:

```
SpikeGLX_NISIM.exe
```

 for the course exercises to avoid the requirement for NI drivers.

 Refer to the SpikeGLX documentation for installation and troubleshooting:

 https://billkarsh.github.io/SpikeGLX/

---

 ## Kilosort is not working

 Kilosort can have additional hardware and software requirements, particularly when using GPU acceleration.

 Check the official Kilosort installation instructions:

 https://github.com/MouseLand/Kilosort

 Do not assume that a Kilosort installation problem is caused by the course Python environment. Kilosort may have its own dependencies and hardware requirements.

---

 ## Phy is not working

 Check the official installation instructions:

 https://phy.readthedocs.io/en/latest/installation/

 Make sure that Phy is being launched from the environment in which it was installed.

---

 ## Bombcell is not working

 First check the official Python installation instructions:

 https://github.com/Julie-Fabre/bombcell#python

 Then run the example notebook from the Bombcell repository:

 https://github.com/Julie-Fabre/bombcell#-quick-start-guide

 Running the example notebook is a useful way to determine whether the issue is specific to the course notebooks or to the Bombcell installation itself.

---

 ## SpikeInterface cannot read my data

 First check that you are providing the correct folder.

 For SpikeGLX data, the relevant recording folder typically contains files associated with the recording streams.

 Refer to the SpikeInterface documentation for information about loading Neuropixels and SpikeGLX recordings:

 https://spikeinterface.readthedocs.io/

 Do not modify or rename raw acquisition files unless you know exactly what the consequences will be.

---

 ## The analysis is very slow

 Some Neuropixels operations are computationally expensive.

 This can be normal.

 For example:

 - Reading large recordings
- Filtering
- Motion correction
- Spike sorting
- Extracting waveforms
- Computing quality metrics
- Generating large visualisations

 Some operations can take a substantial amount of time and may use multiple CPU cores or a GPU.

 Start with the parameters provided in the course notebooks rather than immediately increasing the number of workers.

---

 # Reproducibility

 One of the goals of this course is to encourage reproducible analysis.

 A reproducible analysis should ideally specify:

 - The Python version
- Package versions
- Input data
- Analysis parameters
- Processing steps
- Output files
- Code used to generate the results

 The `environment.yml` file provides one part of this reproducibility by describing the Python software environment.

 For more advanced projects, consider recording the exact package versions used for an analysis.

 You can inspect installed Conda packages using:

```
conda list
```

 and Python packages using:

```
pip list
```

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

 - [ ] Windows 10 or Windows 11 is installed
- [ ] Miniforge is installed
- [ ] The Miniforge Prompt opens successfully
- [ ] Conda works from the Miniforge Prompt
- [ ] Git is installed
- [ ] VS Code is installed
- [ ] VS Code Python extension is installed
- [ ] VS Code Jupyter extension is installed

 ## Python environment

 - [ ] Course repository has been cloned
- [ ] `environment.yml` has been used to create the environment
- [ ] `neuropixels-course` environment activates successfully
- [ ] Python reports version 3.11.x
- [ ] The installation check notebook runs successfully
- [ ] All checks in the installation check notebook pass

 ## Neuropixels software

 - [ ] SpikeGLX is installed
- [ ] SpikeGLX\_NISIM.exe has been tested
- [ ] CatGT is installed
- [ ] NeuroPyxels is installed
- [ ] Kilosort is installed, if required for the course
- [ ] Phy is installed
- [ ] Bombcell Python version is installed
- [ ] Bombcell example notebook has been run
- [ ] SpikeInterface is installed
- [ ] IBL Neuropixels tools are installed

 ## Notebooks

 - [ ] A course notebook opens successfully in VS Code
- [ ] The `neuropixels-course` Jupyter kernel is available
- [ ] A course notebook runs successfully

 If you encounter problems, please resolve them before the course where possible. If you cannot resolve an issue, bring the error message and details of your setup to the course.

---

 # Quick start

 If everything is already installed, the normal workflow is:

```
# Enter the repository
cd neuropixels-course

# Activate the course environment
conda activate neuropixels-course

# Open VS Code
code .
```

 Then:

 1. Open the installation check notebook.
2. Select the `neuropixels-course` Jupyter kernel.
3. Run the installation checks.
4. Once all checks pass, proceed to the course notebooks.

 Alternatively, launch JupyterLab with:

```
jupyter lab
```

---

 # Course philosophy

 The aim of this course is not simply to provide a collection of commands for analysing Neuropixels recordings.

 Instead, we will focus on understanding the complete analysis pipeline:

```
Neuropixels acquisition
        │
        ▼
SpikeGLX
        │
        ▼
Raw Neuropixels data
        │
        ▼
CatGT / preprocessing
        │
        ▼
Data inspection and visualisation
        │
        ▼
Spike sorting
        │
        ├───────────────┐
        ▼               ▼
    Kilosort       Other sorters
        │
        ▼
Spike-sorting results
        │
        ├──────────────────────────┐
        ▼                          ▼
      Phy                    Bombcell
Manual curation          Automated QC
        │                          │
        └────────────┬─────────────┘
                     ▼
               Curated units
                     │
                     ▼
          Downstream analysis
                     │
                     ▼
        Figures and interpretation
```

 We will also use Python frameworks such as SpikeInterface, NeuroPyxels, and IBL Neuropixels tools to work with and analyse the resulting data.

 The notebooks are intended to be both **hands-on exercises** and **reference material** that you can return to when analysing your own Neuropixels datasets.

---

 # Questions and problems

 If you encounter a problem during installation or while working through the course:

 1. Read the relevant section of this README.
2. Run the installation check notebook.
3. Check that the `neuropixels-course` Conda environment is active.
4. Check that VS Code/Jupyter is using the correct Python environment.
5. Check the installation instructions for the specific software.
6. Restart VS Code or Jupyter if necessary.
7. If the problem persists, report the error including:
   - Operating system
   - Python version
   - The software or notebook that produced the error
   - The command that produced the error
   - The complete error message

 When asking for help, **please copy the complete error message rather than only describing what went wrong**. This makes diagnosing problems much easier.

---
