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
dataFile = '../data/NopersonTimedomain.mat'
data0 = scio.loadmat(dataFile)

trace= Scatter(x=np.squeeze(data0['xtic_Nopertim'].tolist(), axis=None),
                y=np.squeeze(data0['ytic_Nopertim'].tolist(), axis=None),
                mode='lines',
                line=dict(color='#2887C7',width=2))
data=[trace]
layout=go.Layout( height=500 ,width = 620,
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 27, # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     ),
                    xaxis=dict(range=[0,20]),
                    yaxis=dict(range=[-0.4,0.4])
                  )
fig = go.Figure(data=data,layout = layout)
fig["layout"]["xaxis"].update({"title": "Time (s)","titlefont": {"size": 27}})
fig["layout"]["yaxis"].update({"title": "Amplitude","titlefont": {"size": 27}})
fig["layout"]["template"] = "simple_white"
fig.update_xaxes(showgrid=True,#将网格去掉
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )
html_path = "../htmls/NopersonTimedomain.html"
fig.write_image('../images/NopersonTimedomain.eps')
pyplot(fig,filename=html_path)