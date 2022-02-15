# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:15:05 2022
@author: Parker
"""

import numpy as np
from scipy import signal
import scipy.fftpack
from plotly.offline import plot
from plotly.subplots import make_subplots
import plotly.graph_objects as go

x1 = np.linspace(0, 200, 10000)
x1a = np.linspace(0, 400, 20000)
x2 = np.linspace(0, 200, 10000)
x3 = np.linspace(0, 200, 10000)

y1 = np.sin(2*np.pi*x1)
y2 = np.sin(2*np.pi*2*x2)
y3 = 2*np.sin(2*np.pi*x3)

n = np.random.rand(10000)
y3 += n
y3 += 0.2*np.sin(12*2*np.pi*x3)
y3 -= np.mean(y3)

f1, pxx1 = signal.welch(y1, 10000/200, nperseg=len(y1))
f2, pxx2 = signal.welch(y2, 10000/200, nperseg=len(y2))
f3, pxx3 = signal.welch(y3, 10000/200, nperseg=len(y3))

y1f = scipy.fftpack.fft(y1)
x1f = np.linspace(0.0, 1.0/(2.0*0.02), int(10000/2))
y2f = scipy.fftpack.fft(y2)
x2f = np.linspace(0.0, 1.0/(2.0*0.02), int(10000/2))
y3f = scipy.fftpack.fft(y3)
x3f = np.linspace(0.0, 1.0/(2.0*0.02), int(10000/2))

fig = make_subplots(
        rows=2, cols=1,
        # subplot_titles=sub_titles,
        # column_widths=[0.65,0.35],
        # shared_xaxes='columns',
        # shared_yaxes='columns',
        vertical_spacing=0.01,
        horizontal_spacing=0.01)

fig.add_trace(go.Scatter(x=x1, y=y1,
                         mode='lines',
                         # line=dict(color='Green')
                         ),
              row=1, col=1)
fig.add_trace(go.Scatter(x=x2, y=y2,
                          mode='lines',
                          # line=dict(color='Green')
                          ),
              row=1, col=1)
fig.add_trace(go.Scatter(x=x3, y=y3,
                          mode='lines',
                          # line=dict(color='Green')
                          ),
              row=1, col=1)
fig.add_trace(go.Scatter(x=x1f, y=2.0/10000 * np.abs(y1f[:10000//2]),
                         mode='lines',
                         # line=dict(color='Green')
                         ),
              row=2, col=1)
fig.add_trace(go.Scatter(x=x2f, y=2.0/10000 * np.abs(y2f[:10000//2]),
                         mode='lines',
                         # line=dict(color='Green')
                         ),
              row=2, col=1)
fig.add_trace(go.Scatter(x=x3f, y=2.0/10000 * np.abs(y3f[:10000//2]),
                         mode='lines',
                         # line=dict(color='Green')
                         ),
              row=2, col=1)

# fig.update_layout(showlegend=False)
fig.update_layout(title_text='Dummy', title_x=0.5)

plot(fig, filename='Dummy.html')




