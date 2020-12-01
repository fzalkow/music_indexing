'''
File name: common/__init__.py
Author: Frank Zalkow
Date: 2020
License: MIT
This file is part of the following repository:
  https://github.com/fzalkow/music_indexing
'''

import numpy as np
import librosa

CHROMA_DIMS = 12


def compute_features(fn_audio):
    Fs = 22050
    H = 2205
    smooth = 41
    downsample = 10

    x, _ = librosa.load(fn_audio, sr=Fs)
    X_iirt = librosa.spectrum.iirt(x, sr=Fs, win_length=H*2, hop_length=H, center=True)
    fmin = librosa.midi_to_hz(24)
    X_cens = librosa.feature.chroma_cens(sr=Fs, C=X_iirt, fmin=fmin, bins_per_octave=CHROMA_DIMS, n_octaves=7,
                                         win_len_smooth=smooth, norm=2)[:, ::downsample]

    return X_cens


def generate_shingles(X_cens, L=20):
    num_shingles = X_cens.shape[1] - L + 1
    shingles = np.empty((num_shingles, L * CHROMA_DIMS))
    for idx in range(num_shingles):
        shingles[idx, :] = X_cens[:, idx:idx + L].ravel()
    return shingles
