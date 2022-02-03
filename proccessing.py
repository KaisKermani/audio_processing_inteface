import numpy as np
import scipy.io.wavfile as wavfile
from scipy.fft import rfft, rfftfreq, irfft
from normalization import norm


def dft_analysis(file):

    samples = (0, -1)

    fs, aud = wavfile.read(file)
    if len(aud.shape) == 2:
        aud = aud.sum(axis=1) / 2

    sig_t = norm(aud[samples[0]: samples[1]])
    sig_f = rfft(sig_t/len(sig_t), workers=-1)
    freq = rfftfreq(len(sig_t), 1 / fs)
    sig_t_synth = irfft(sig_f, workers=-1)*len(sig_t)

    mag_db = 20*np.log10(np.abs(sig_f))
    phase = np.unwrap(np.angle(sig_f))

    return mag_db, phase, freq, sig_t, sig_t_synth
