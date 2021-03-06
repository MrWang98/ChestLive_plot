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

animals=['Sit on chair'	,'Sit on sofa','Lying',' Stand','Walk']
fig = go.Figure(data=[
    go.Bar(name='User1', x=animals, y=[ 99.58 ,95.09 ,   91.48 ,  93.78,     87],marker_color='#AFC7BF',width=0.6),


])
# Change the bar mode
fig.update_layout(barmode='group',
                  legend=dict(
                      #orientation="h",  # 将legend改为横排放置
                      yanchor="bottom",
                      y=0.1,
                      xanchor="right",
                      x=1,
                      bordercolor ="black",
                      borderwidth = 2,
                      font=dict(
                          size=26,
                          color='black', )
                  ),
                  )

fig['layout'].update(
height=590 ,width = 670,
font=dict(
family="Time New Roman",  # 所有标题文字的字体
size = 30, # 所有标题文字的大小
))
#fig["layout"]["xaxis"].update({"title": "Different Human Pose","titlefont": {"size": 34}})
fig["layout"]["yaxis"].update({"title": "Accuracy (%)","titlefont": {"size": 34}})
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
html_path = "../htmls/ImpactofHumanPose.html"
fig.write_image('../images/ImpactofHumanPose.jpg')
pyplot(fig,filename=html_path)