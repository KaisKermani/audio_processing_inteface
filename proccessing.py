import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.io.wavfile as wavfile
from scipy.fft import rfft, rfftfreq, irfft
from normalization import norm
import math


def analyse_file(filename, title):
    samples = (0, -1)

    fs, aud = wavfile.read(filename)
    if len(aud.shape) == 2:
        aud = aud.sum(axis=1) / 2
    sig_t = norm(aud[samples[0]: fs])

    sig_f = rfft(sig_t, workers=-1)
    freq = rfftfreq(len(sig_t), 1 / fs)
    sig_tout = irfft(sig_f, workers=-1)

    fig = make_subplots(rows=4,
                        subplot_titles=("Raw Audio: x",
                                        "Re-synthesised audio (IDFT)",
                                        "Magnitude spectrum: mX",
                                        "Phase Spectrum: pX",
                                        ),
                        shared_xaxes=True,
                        )

    fig.append_trace(go.Scatter(
        y=sig_t,
        showlegend=False,
    ), row=1, col=1,)

    fig.append_trace(go.Scatter(
        x=freq,
        y=np.abs(sig_f),
        showlegend=False,
    ), row=3, col=1)
    fig.update_yaxes(type="log", row=3, col=1)

    fig.append_trace(go.Scatter(
        x=freq,
        y=np.unwrap(np.angle(sig_f)),
        showlegend=False,
    ), row=4, col=1)

    fig.append_trace(go.Scatter(
        y=sig_tout,
        showlegend=False,
    ), row=2, col=1,)

    fig.update_layout(title_text="DFT Analysis: " + title,
                      xaxis_showticklabels=True, xaxis2_showticklabels=True, xaxis3_showticklabels=True,
                      xaxis_matches='x2', xaxis2_matches=None)

    fig.write_html('templates/report.html')
    return 0
