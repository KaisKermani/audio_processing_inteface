import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.io import to_html


def dft_plot(mag_db, phase, freq, sig_t, sig_t_synth):

    # TODO: Colors + aesthetics of the charts
    fig = make_subplots(rows=4,
                        subplot_titles=("Magnitude spectrum: mX",
                                        "Phase Spectrum: pX",
                                        "Raw Audio: x",
                                        "Re-synthesised audio (IDFT)",
                                        ),
                        shared_xaxes=True,
                        )

    fig.append_trace(go.Scatter(
        x=freq,
        y=mag_db,
        showlegend=False,
    ), row=1, col=1)
    fig.update_yaxes(row=3, col=1)

    fig.append_trace(go.Scatter(
        x=freq,
        y=phase,
        showlegend=False,
    ), row=2, col=1)

    fig.append_trace(go.Scatter(
        y=sig_t,
        showlegend=False,
    ), row=3, col=1,)

    fig.append_trace(go.Scatter(
        y=sig_t_synth,
        showlegend=False,
    ), row=4, col=1,)

    fig.update_layout(title_text="DFT Analysis: ",
                      xaxis_showticklabels=True, xaxis2_showticklabels=True, xaxis3_showticklabels=True,
                      xaxis_matches='x2', xaxis2_matches=None)

    # fig.write_html('templates/report.html')
    return to_html(fig, auto_play=False, full_html=False, default_height=920)
