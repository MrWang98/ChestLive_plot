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
# dataFile = 'D:\DataSet/ChestLiveTrainingSet.mat'

data0 = {'times':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
         'U1':[67.65,
82.87,
93.40,
96.42,
96.57,
98.01,
97.28,
97.67,
98.21,
98.32,
98.83,
98.02,
97.39,
98.97,
98.74,
97.42,
99.17,
99.15,
98.37,
99.08,
],
         'U2':[69.34,
81.06,
93.66,
94.49,
96.41,
95.98,
96.30,
93.89,
94.97,
96.38,
96.18,
96.96,
96.78,
97.32,
95.50,
96.34,
96.55,
96.00,
96.93,
96.00

],
         'U3':[60.15,
76.14,
93.16,
95.37,
97.48,
98.44,
97.71,
97.07,
98.44,
97.94,
97.93,
99.01,
98.29,
99.22,
98.78,
99.19,
99.66,
98.91,
98.84,
98.89

],
         'U4':[90.76,
96.87,
98.50,
97.10,
97.58,
97.99,
97.24,
97.17,
98.43,
97.78,
96.86,
97.49,
97.11,
98.29,
97.20,
97.49,
97.44,
98.00,
99.49,
98.40

],
         'U5':[78.55,
89.82,
97.94,
96.60,
96.64,
97.36,
98.22,
96.39,
97.17,
97.24,
97.60,
97.54,
98.20,
98.56,
98.40,
96.84,
98.19,
98.22,
99.07,
98.73,

]}

trace0= Scatter(x=data0['times'],
                y=data0['U1'],
                mode='lines',name='User1',
                line=dict(color='#AC9B91',width=2.2,dash='dash'))
trace1= Scatter(x=data0['times'],
                y=data0['U2'],
                mode='lines',name='User2',
                line=dict(color='#A85658',width=2.2,dash='dot'))
trace2= Scatter(x=data0['times'],
                y=data0['U3'],
                mode='lines',name='User3',
                line=dict(color='#8895B1',width=2.2,dash='dashdot'))
trace3= Scatter(x=data0['times'],
                y=data0['U4'],
                mode='lines',name='User4',
                line=dict(color='#546CBC',width=2.2,dash='longdash'))
trace4= Scatter(x=data0['times'],
                y=data0['U5'],
                mode='lines',name='User5',
                line=dict(color='#194568',width=2))
tick= list(range(0,21,2))
data=[trace0,trace1,trace2,trace3,trace4]
layout=go.Layout( height=500 ,width = 650,
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 28, # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     ),
xaxis= dict(
        range=[0,20],
        tickmode="array",
        ticktext=tick,
        tickvals=tick,
    ),
yaxis= dict(
        range=[50,100],
    ),
                  legend=dict(#orientation="h",  # 将legend改为横排放置
                              yanchor="bottom",
                              y=0.1,
                              xanchor="right",
                              x=1,
                              font=dict(
                                  size=26,
                                  color='black', )
                              )
                  )
fig = go.Figure(data=data,layout = layout)
fig["layout"]["xaxis"].update({"title": "Training Set Size","titlefont": {"size": 30}})
fig["layout"]["yaxis"].update({"title": "Accuracy (%)","titlefont": {"size": 30}})
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
# fig.write_image('images/ChestLiveTrainingSet.eps')
html_path = "../htmls/ImpactofTrainSetSize.html"
fig.write_image('../images/ImpactofTrainSetSize.eps')

pyplot(fig,filename=html_path)
