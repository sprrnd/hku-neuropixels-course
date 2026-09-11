# HKU Neuropixels Course

 This repository contains the software environment, example notebooks and reference material for the **HKU Neuropixels Course**.

 The course introduces practical analysis of Neuropixels electrophysiology data, from raw preprocessing through spike sorting, quality control and downstream analysis.

 We will use a combination of Python-based tools and dedicated Neuropixels software, including:

 - *SpikeGLX* for data acquisition
 - *Kilosort* for spike sorting
- *Phy* for manual curation
- *Bombcell* for automated quality metrics and curation
- *NeuroPyxels* for loading, processing and plotting Neuropixels data
- *SpikeInterface* for building and managing spike-sorting workflows


 The repository is designed so that participants can:

 - Install and test the required software before the course.
- Clone the course repository.
- Run the example Jupyter notebooks.
- Complete the analysis exercises.
- Use the repository as a reference after the course.


---

 # Course preparation

---

 ## Operating System

 The software used in this course has been tested on Windows, macOS and Linux.

---

 ## Recommended computer setup

 Neuropixels datasets can be large. Some analysis steps can require substantial memory, storage and CPU resources.

 As a general recommendation:

- **RAM:** 8 GB minimum; 16-32 GB or more recommended
- **Storage:** SSD strongly recommended
- **Free disk space:** at least 50 GB or external drive; more may be required for larger Neuropixels datasets
- **CPU:** a modern multi-core processor is recommended

---

 ## Installation

You can find detailed installation instructions in the `installation` folder.

 ### Installation check

 A dedicated notebook is provided to check that your computer and Python environment are correctly configured before starting the course.

 You can find it in:

```
installation/installation_test.ipynb
```

 Please run this notebook **before the course**.

 The notebook checks that the required Python packages are installed and that the course environment is working correctly.

---