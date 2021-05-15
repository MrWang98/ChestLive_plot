#FAR [0.88,0.97,1.84]
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

y=[0.88,0.97,1.84]
# MimicData = {'Victim1': {'False accept rate': 0.88},
#              'Victim2': {'False accept rate': 0.97},
#              'Victim3': {'False accept rate': 1.84}}
# animals=['False accept rate','False reject rate']
x_a=["Victim{}".format(i+1) for i in range(len(y))]
colors=['#8895B1','#9791A0','#9ca8b8']
fig=go.Figure()
for x,d,color in zip(x_a,y,colors):
    fig.add_trace(go.Bar(y=[d],
                         x=[x],
                         marker_color=color,
                         width=0.5,
                         ))
# Change the bar mode
fig.update_layout(barmode='group',
                  showlegend=False,
                  legend=dict(
                      orientation="h",  # 将legend改为横排放置
                      yanchor="bottom",
                      y=1.02,
                      xanchor="right",
                      x=1,
                      font=dict(
                          size=32,
                          color='black', )
                  ),
                  )

fig['layout'].update(
height=600 ,width = 650,
font=dict(
    family="Times New Roman",  # 所有标题文字的字体
    size = 28 , # 所有标题文字的大小
))
fig["layout"]["yaxis"].update({"title": "False accept rate","titlefont": {"size": 30}})
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
html_path = "../htmls/MimicAttack.html"
# fig.write_image('../images/MimicAttack.jpg')
pyplot(fig,filename=html_path)