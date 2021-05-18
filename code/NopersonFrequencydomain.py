import os
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
from plotly.graph_objects import Line
import plotly as py
from datetime import datetime
import scipy.io as scio
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px
pyplot = py.offline.plot
dataFile = '../data/NopersonFrequencydomain.mat'
data0 = scio.loadmat(dataFile)

trace= Scatter(x=np.squeeze(data0['xtic_Noperfre'].tolist(), axis=None),
                y=np.squeeze(data0['ytic_Noperfre'].tolist(), axis=None),
                mode='lines',
                line=dict(color='#2887C7',width=2))
data=[trace]
layout=go.Layout( height=500 ,width = 620,
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 30, # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     ),
                    xaxis=dict(range=[0,0.8])
                  )
fig = go.Figure(data=data,layout = layout)
fig["layout"]["xaxis"].update({"title": "Frequency (Hz)","titlefont": {"size": 30}})
fig["layout"]["yaxis"].update({"title": "Amplitude","titlefont": {"size": 30}})
fig["layout"]["template"] = "simple_white"
fig.update_layout(font=dict(
        family="Times New Roman",  # 所有标题文字的字体
    ),)
fig.update_xaxes(showgrid=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#dbddde',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#dbddde',
                 )
html_path = "../htmls/NopersonFrequencydomain.html"
fig.write_image('../images/NopersonFrequencydomain.eps')
pyplot(fig,filename=html_path)