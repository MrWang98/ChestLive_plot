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
dataFile = '../data/ResultEsdPpca.mat'
data0 = scio.loadmat(dataFile)

trace0= Scatter(x=np.squeeze(data0['subfig1_xtic'].tolist(), axis=None),
                y=np.squeeze(data0['subfig1_ytic'].tolist(), axis=None),
                mode='lines',name='Chest motion extraction using ESD',
                line=dict(color='#C3B0D6',width=2.5))  ##55DDDD
trace1= Scatter(x=np.squeeze(data0['subfig2_xtic'].tolist(), axis=None),
                y=np.squeeze(data0['subfig2_ytic'].tolist(), axis=None),
                mode='lines',name='Chest motion extraction uisng ChestLive',
                line=dict(color='#194568',width=2.5))
fig = make_subplots(rows=2,
                    cols=1,)
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 2, 1)
fig["layout"]["template"] = "simple_white"
fig["layout"]["xaxis2"].update({"title": "Time (s)","titlefont": {"size": 30}})# "titlefont": {"color": "pink"}
fig["layout"]["yaxis1"].update({"title": "Amplitude","titlefont": {"size": 30}})
fig["layout"]["yaxis2"].update({"title": "Amplitude","titlefont": {"size": 30}})
fig.update_xaxes(showgrid=True,#将网格去掉
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#EDEDED',

                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(showgrid=True,
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#EDEDED',
                 )
fig['layout'].update(
                     height=720 ,width = 800,
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 30, # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     ),legend = dict(orientation="h",  # 将legend改为横排放置
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1,
                                  #traceorder="grouped",
                                  #tracegroupgap = 20,
                                  #bordercolor = "black",
                                  #borderwidth = 2,

                                  font=dict(
                                  size=23,
                                  color='black', )
))
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
html_path = "../htmls/ResultEsdPpca.html"
fig.write_image('../images/ResultEsdPpca.eps')
pyplot(fig,filename=html_path)
