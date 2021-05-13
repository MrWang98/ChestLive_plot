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
dataFile = '../data/personTimedomain.mat'
data0 = scio.loadmat(dataFile)

trace0= Scatter(x=np.squeeze(data0['xtic_1_pertime'].tolist(), axis=None),
                y=np.squeeze(data0['ytic_1_pertime'].tolist(), axis=None),
                mode='lines', name='Belt-based estimation ',#legendgroup="group"
                line=dict(color='#C9C0B5', width=2.5, dash='dash'))  ##55DDDD

trace1= Scatter(x=np.squeeze(data0['xtic_2_pertime'].tolist(), axis=None),
                y=np.squeeze(data0['ytic_2_pertime'].tolist(), axis=None),
                mode='lines', name='Detected estimation',#legendgroup="group",
                line=dict(color='#8895B1',width=2))
data=[trace0,trace1]
layout=go.Layout( height=600 ,width = 720,
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 25, # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     ),

                    legend = dict( # 将legend改为横排放置
                                orientation="h",
                                yanchor="bottom",
                                y=1.02, #0.82
                                xanchor="center",
                                x=0.5,
                      # bordercolor ="black",
                      # borderwidth = 2,
                        font=dict(
                            size=22,
                            color='black', )
                    )
                                 )

fig = go.Figure(data=data,layout = layout)
fig["layout"]["xaxis"].update({"title": "Time (s)", "titlefont": {"size": 30}})
fig["layout"]["yaxis"].update({"title": "Nomarlized amplitude", "titlefont": {"size": 30}})
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
html_path = "../htmls/personTimedomain.html"
fig.write_image('../images/personTimedomain.jpg')
pyplot(fig,filename=html_path)
