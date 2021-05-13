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
dataFile = '../data/personFrequencydomain.mat'
data0 = scio.loadmat(dataFile)

trace0= Scatter(x=np.squeeze(data0['xtic_1_perFre'].tolist(), axis=None),
                y=np.squeeze(data0['ytic_1_perFre'].tolist(), axis=None),
                mode='lines', name='Belt-based frequency ',#legendgroup="group"
                line=dict(color='#9FBCC2', width=2.5, dash='dash'))  ##55DDDD

trace1= Scatter(x=np.squeeze(data0['xtic_2_perFre'].tolist(), axis=None),
                y=np.squeeze(data0['ytic_2_perFre'].tolist(), axis=None),
                mode='lines', name='Detected frequency',#legendgroup="group",
                line=dict(color='#AFC7BF',width=2))
data=[trace0,trace1]
layout=go.Layout( height=550 ,width = 650,
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 30, # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     ),
                    xaxis=dict(range=[0,1]),
                    legend = dict( # 将legend改为横排放置
                                orientation="h",
                                  yanchor="bottom",
                                  y=1.02 , # 1.02 0.75
                                  xanchor="center",
                                  x=0.5,
                      # bordercolor ="black",
                      # borderwidth = 2,
                        font=dict(
                            size=20,
                            color='black', )
                    )
                                 )

fig = go.Figure(data=data,layout = layout)
fig["layout"]["xaxis"].update({"title": "Frequency (Hz)","titlefont": {"size": 30}})
fig["layout"]["yaxis"].update({"title": "Amplitude","titlefont": {"size": 30}})
fig["layout"]["template"] = "simple_white"
fig.add_vline(x=0.275, line_width=3, line_dash="dash", line_color="#89726C")
fig.add_annotation({'x': 0.28, 'y': 8, 'text': "Frequency = 0.275", 'showarrow': True, 'font': dict(
    color="black",
    size=25
), 'arrowcolor': "black",  'arrowsize': 2, 'arrowwidth': 1, 'arrowhead': 1})
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
html_path = "../htmls/personFrequencydomain.html"
fig.write_image('../images/personFrequencydomain.eps')
pyplot(fig,filename=html_path)