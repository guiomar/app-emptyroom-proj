# Copyright (c) 2021 brainlife.io
#
# This file is a MNE python-based brainlife.io App
#
# Author: Guiomar Niso
# Indiana University

# set up environment
import os
import json
import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Load brainlife config.json
with open(__location__+'/config.json') as config_json:
    config = json.load(config_json)

# == LOAD DATA ==
fname = config['fif']
raw = mne.io.read_raw(fname)

# == GET CONFIG VALUES ==
start = config['start']
stop = config['stop']
duration = config['duration']
n_grad = config['n_grad']
n_mag = config['n_mag']

# == COMPUTE EMPTYROOOM PROJECTOR ==
er_proj = mne.compute_proj_raw(raw, start, stop, duration, n_grad, n_mag)

# == SAVE FILE ==
er_proj.save(os.path.join('out_dir','proj.fif'))


# == FIGURES ==
plt.figure(1)
fig_ep = mne.viz.plot_projs_topomap(er_proj, colorbar=True, vlim='joint',
                           info=empty_room_raw.info)
fig_ep.savefig(os.path.join('out_figs','emptyroom_projectors.png'))







