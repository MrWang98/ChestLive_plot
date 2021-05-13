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

animals=['1','2','3','4','5']
fig = go.Figure(data=[
    go.Bar(name='Victim1', x=animals, y=[2.50,1.25,1.21,0.68,2.08],marker_color='#8895B1',width=0.27),
    go.Bar(name='Victim2', x=animals, y=[0.77,0.69,1.59,0.37,1.04],marker_color='#9791A0',width=0.27),
    go.Bar(name='Victim3', x=animals, y=[2.07,1.41,0.92,2.7,1.91],marker_color='#9ca8b8',width=0.27),
])
# Change the bar mode
fig.update_layout(barmode='group',
                  legend=dict(
                      orientation="h",  # 将legend改为横排放置
                      yanchor="bottom",
                      y=1.02, #0.8
                      xanchor="right",
                      x=1,
                      # bordercolor ="black",
                      # borderwidth = 2,
                      font=dict(
                          size=32,
                          color='black', )
                  ),
                  )

fig['layout'].update(
height=600 ,width = 650,
font=dict(
family="Time New Roman",  # 所有标题文字的字体
size = 30 , # 所有标题文字的大小
))
fig["layout"]["yaxis"].update({"title": "False accept rate","titlefont": {"size": 30}})
fig["layout"]["xaxis"].update({"title": "Attacker","titlefont": {"size": 30}})
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
html_path = "../htmls/FAR.html"
fig.write_image('../images/FAR.eps')
pyplot(fig,filename=html_path)