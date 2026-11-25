<h1 align="center">Emptyroom projs</h1>

<p align="center">
  Computes signal-space projection (SSP) vectors from empty-room MEG with MNE-Python compute_proj_raw and saves the projectors with a plot.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.645"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.645-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Computes signal-space projection (SSP) vectors from empty-room MEG with MNE-Python compute_proj_raw and saves the projectors with a plot.**

Runs mne.compute_proj_raw on continuous data (designed for empty-room recordings) to capture environmental noise, with configurable vector counts per sensor type and time window. Apply the resulting projectors to subject recordings to remove that noise.

| | |
|---|---|
| **Inputs** | `neuro/meg/fif` |
| **Outputs** | `neuro/meeg/mne/projection` · `raw` |
| **Container** | `brainlife/mne:0.23dev` |
| **Resources** | 8 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.645](https://doi.org/10.25663/brainlife.app.645) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `raw01` | `neuro/meg/fif` | yes | Continuous MEG recording (FIF), typically empty room. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir` | `neuro/meeg/mne/projection` | Emptyroom projector |
| `out_figs` | `raw` | Plot of the empty-room projectors (PNG). |

<details>
<summary><b>Parameters</b> (10)</summary>

| Parameter | Type | Default | Description |
|---|---|---|---|
| `start` | number | `0` | Time (in sec) to start computing SSP. |
| `stop` | number |  | Time (in sec) to stop computing SSP. Default (empty): None -> will go to the end of the file. |
| `duration` | number | `1` | Duration (in sec) to chunk data into for SSP If duration is None, data will not be chunked. |
| `n_grad` | number | `2` | Number of vectors for gradiometers. |
| `n_mag` | number | `2` | Number of vectors for magnetometers. |
| `n_eeg` | number | `0` | Number of vectors for EEG channels. |
| `reject` | string |  | Epoch rejection configuration (see Epochs). |
| `flat` | string |  | Epoch flat configuration (see Epochs). |
| `n_jobs` | number | `1` | The number of jobs to run in parallel. If -1, it is set to the number of CPU cores. Requires the joblib package. None (default) is a marker for ‘unset’ that will be interpreted as n_jobs=1 (sequential execution) unless the call is performed under a joblib.parallel_backend() context manager that sets another value for n_jobs. Number of jobs to use to compute covariance. |
| `meg` | enum | `separate` | Can be ‘separate’ (default) or ‘combined’ to compute projectors for magnetometers and gradiometers separately or jointly. If ‘combined’, n_mag == n_grad is required and the number of projectors computed for MEG will be n_mag. Options: `separate`, `combined`. |

</details>

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.645](https://doi.org/10.25663/brainlife.app.645), choose `neuro/meg/fif` from your project, set the parameters and press **Execute**. The results are saved to your project as `neuro/meeg/mne/projection`, `raw`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:0.23dev`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "fif": "/path/to/raw01/fif",
       "channels": "/path/to/raw01/channels",
       "headshape": "/path/to/raw01/headshape",
       "coordsystem": "/path/to/raw01/coordsystem",
       "calibration": "/path/to/raw01/calibration",
       "crosstalk": "/path/to/raw01/crosstalk",
       "destination": "/path/to/raw01/destination",
       "events": "/path/to/raw01/events",
       "events_json": "/path/to/raw01/events_json",
       "start": 0,
       "stop": "<number>",
       "duration": 1,
       "n_grad": 2,
       "n_mag": 2,
       "n_eeg": 0,
       "reject": "",
       "flat": "",
       "n_jobs": 1,
       "meg": "separate"
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Emptyroom projs. brainlife.io App. [doi:10.25663/brainlife.app.645](https://doi.org/10.25663/brainlife.app.645)
- Gramfort A, et al. MEG and EEG data analysis with MNE-Python. Front Neurosci 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Guiomar Niso
- Saeed Zahran

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
