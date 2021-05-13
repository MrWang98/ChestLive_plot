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

animals=['4E:P30','Mi10:S30','Mi6:4E']
fig = go.Figure(data=[
    go.Bar(name='Enrollment', x=animals, y=[99.58,96.86,98.2],marker_color='#CFC5BB',width=0.3),
    go.Bar(name='Login', x=animals, y=[98.5,92.51,91.87],marker_color='#AC9B91',width=0.3),

])
# Change the bar mode
fig.update_layout(barmode='group',
                  legend=dict(
                      orientation="h",  # 将legend改为横排放置
                      yanchor="bottom",
                      y=1.02,
                      xanchor="right",
                      x=1,
                     # bordercolor ="black",
                      #borderwidth = 2,
                      font=dict(
                          size=32, #22
                          color='black', )
                  ),
                  )

fig['layout'].update(
height=520 ,width = 620,
font=dict(
family="Time New Roman",  # 所有标题文字的字体
size = 32 , # 所有标题文字的大小
))
# fig["layout"]["xaxis"].update({"title": "Different device","titlefont": {"size": 32}})
fig["layout"]["yaxis"].update({"title": "Accuracy (%)","titlefont": {"size": 32}})
fig["layout"]["template"] = "simple_white"
fig.update_xaxes(showgrid=True,#将网格去掉
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',

                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(showgrid=True,
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',

                 )
html_path = "../htmls/ImpactofDevice.html"
fig.write_image('../images/ImpactofDevice.eps')
pyplot(fig,filename=html_path)