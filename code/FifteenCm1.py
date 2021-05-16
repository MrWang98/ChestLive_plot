import os
import plotly.io as pio
import plotly.graph_objs as go
from plotly.graph_objects import Line
import plotly as py
from datetime import datetime
import scipy.io as scio
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px
pyplot = py.offline.plot
# dataFile = 'D:\DataSet/FifteenCm1.mat'
dataFile = '../data/FifteenCm1.mat'
data0 = scio.loadmat(dataFile)


z = [99.02,
99.57,
99.58,
97.96,
98.39,
99.08,
98.2,
98.15,
96.86,
98.69,
98.78,
98.79,
99.07,
97.73,
98.5,
97.02,
98.35,
99.71,
98.87,
99.02,
98.75,
97.11,
98.36,
99.42,
96.64,
95.29,
96.98]

fig = go.Figure()

fig.add_trace(go.Barpolar(
    r=[z[0]],
    theta=['U1'],
# marker_color='rgb(253,249,238)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[1]],
    theta=['U2'],
# marker_color='rgb(240,235,229)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[2]],
    theta=['U3'],
# marker_color='rgb(202,195,187)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[3]],
    theta=['U4'],
# marker_color='rgb(216,202,175)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[4]],
    theta=['U5'],
# marker_color='rgb(226,165,173)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[5]],
    theta=['U6'],
# marker_color='rgb(237,205,206)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[6]],
    theta=['U7'],
# marker_color='rgb(246,246,246)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[7]],
   theta=['U8'],
# marker_color='rgb(181,199,201)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[8]],
    theta=['U9'],
# marker_color='rgb(201,192,181)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[9]],
    theta=['U10'],
# marker_color='rgb(168,86,88)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[10]],
    theta=['U11'],
# marker_color='rgb(25,69,104)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[11]],
    theta=['U12'],
# marker_color='rgb(175,199,191)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[12]],
    theta=['U13'],
# marker_color='rgb(199,207,192)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[13]],
    theta=['U14'],
# marker_color='rgb(221,214,202)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[14]],
    theta=['U15'],
# marker_color='rgb(238,223,218)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[15]],
    theta=['U16'],
# marker_color='rgb(234,208,209)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[16]],
    theta=['U17'],
# marker_color='rgb(240,235,229)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[17]],
    theta=['U18'],
# marker_color='rgb(224,205,207)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[18]],
    theta=['U19'],
# marker_color='rgb(211,212,204)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[19]],
    theta=['U20'],
# marker_color='rgb(223,214,215)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[20]],
    theta=['U21'],
# marker_color='rgb(193,203,215)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[21]],
    theta=['U22'],
# marker_color='rgb(137,114,108)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[22]],
   theta=['U23'],
# marker_color='rgb(172,155,145)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[23]],
    theta=['U24'],
marker_color='rgb(196,218,230)'
# marker_color='rgb(207,197,187)'
))
fig.add_trace(go.Barpolar(
    r=[z[24]],
    theta=['U25'],
# marker_color='rgb(245,241,232)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[25]],
    theta=['U26'],
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[z[26]],
    theta=['U27'],
# marker_color='rgb(175,199,191)'
marker_color='rgb(196,218,230)'
))

fig.add_trace(go.Barpolar(
    r=[97.26],
    theta=['U28'],
marker_color='rgb(196,218,230)'
# marker_color='rgb(216,201,174)'
))
fig.add_trace(go.Barpolar(
    r=[99.35],
    theta=['U29'],
# marker_color='rgb(210,214,137)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[99.8],
    theta=['U30'],
# marker_color='rgb(226,224,223)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[99.51],
    theta=['U31'],
# marker_color='rgb(226,224,223)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[99.23],
    theta=['U32'],
# marker_color='rgb(226,224,223)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[98.06],
    theta=['U33'],
# marker_color='rgb(226,224,223)'
marker_color='rgb(196,218,230)'
))
fig.add_trace(go.Barpolar(
    r=[99.38],
    theta=['U34'],
# marker_color='rgb(226,224,223)'
marker_color='rgb(196,218,230)'
))
fig.update_layout(
    #title='Wind Speed Distribution in Laurel, NE',
    font_size=24.5,
    legend_font_size=24,
    polar_radialaxis_ticksuffix='%',
    polar_angularaxis_rotation=90,
showlegend = False,
)

#fig["layout"]["template"] = "plotly_dark"
fig["layout"]["xaxis"].update({"title": "Authenticate result","titlefont": {"size": 28}})
fig["layout"]["yaxis"].update({"title": "Ground truth","titlefont": {"size": 28}})
fig['layout'].update(
height=600 ,width = 650,
font=dict(
family="Time New Roman",  # 所有标题文字的字体
size = 23.5, # 所有标题文字的大小
))
# fig.write_image('images/FifteenCm1.eps')
html_path = "../htmls/AuthenticationRate.html"
fig.write_image('../images/AuthenticationRate.eps')
pyplot(fig,filename=html_path)