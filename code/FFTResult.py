import os
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
from plotly.graph_objects import Line
import plotly as py
from datetime import datetime
import scipy.io as scio
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import plotly.express as px
pyplot = py.offline.plot
dataFile = '../data/FFTResult.mat'
data0 = scio.loadmat(dataFile)
x=np.squeeze(data0['XVarNames'].tolist(), axis=None)
y=np.squeeze(data0['YVarNames'].tolist(), axis=None)
z=np.squeeze(data0['FFT_Store'].tolist(), axis=None)
fig = go.Figure(data=go.Heatmap(
                   z=z,
                   x=x,
                   y=y,
                  ))

fig['layout'].update(
                     height=800,width = 920,
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 17 , # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     ),

)
fig.update_xaxes(showgrid=True,#将网格去掉
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F0F8FD',
                 #range = [0,24]


                 )
fig.update_yaxes(showgrid=True,
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F0F8FD',
                 )

fig.add_vline(x=0.5, line_width=3,line_color="#FAFAFA")
fig.add_vline(x=1.5, line_width=3,line_color="#FAFAFA")
fig.add_vline(x=2.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=3.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=4.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=5.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=6.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=7.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=8.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=9.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=10.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=11.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=12.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=13.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=14.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=15.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=16.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=17.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=18.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=19.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=20.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=21.5, line_width=3,line_color="#FCFCFC")
fig.add_vline(x=22.5, line_width=3,line_color="#FCFCFC")
#fig.add_vline(x=23.5, line_width=3,line_color="#FCFCFC")



fig["layout"]["template"] = "simple_white"
fig["layout"]["xaxis"].update({"title": "Time (s)","titlefont": {"size": 30}})# "titlefont": {"color": "pink"}
fig["layout"]["yaxis"].update({"title": "Frequency","titlefont": {"size": 30}})
html_path="../htmls/FFTResult.html"
fig.write_image('../images/FFTResult.eps')
pyplot(fig,filename=html_path)