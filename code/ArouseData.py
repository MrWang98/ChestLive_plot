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

Arousedata = {'Aourse Words': {'Alexa': 98.54, 'HeySiri': 99.86, 'Guess': 99.86,  'OkGoogle': 97.6, 'Choice': 98.2, 'Describe': 97.16}}
a = pd.DataFrame(Arousedata)

fig = go.Figure([go.Bar(x=['Alexa','Ok Google','Choice','Describe','Guess','Hey Siri'], y=[98.54,97.6,98.2,97.16,99.86,99.86],
                        hovertext=['27% market share', '24% market share', '19% market share'],
                        width=0.55)])
fig.update_traces(marker_color='rgb(25,69,104)', marker_line_color='rgb(8,48,107)',
                  marker_line_width=1.5, opacity=0.6)
fig['layout'].update(
height=630 ,width = 750,
font=dict(
family="Time New Roman",  # 所有标题文字的字体
size = 32, # 所有标题文字的大小
))
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
fig["layout"]["template"] = "simple_white"
#fig["layout"]["xaxis"].update({"title": "Different arouse words","titlefont": {"size": 36}})# "titlefont": {"color": "pink"}
fig["layout"]["yaxis"].update({"title": "Accuracy (%)","titlefont": {"size": 36}})
# fig.write_image('images/ArouseData.eps')
html_path = "../htmls/ImpactofArouseword.html"
fig.write_image('../images/ImpactofArouseword.eps')
pyplot(fig,filename=html_path)