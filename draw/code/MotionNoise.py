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
# dataFile = 'D:\DataSet/MotionNoise.mat'
dataFile = '../data/MotionNoise.mat'

data0 = scio.loadmat(dataFile)

trace0= Scatter(x=np.squeeze(data0['subfig_x'].tolist(), axis=None),
                y=np.squeeze(data0['subfig1_y1'].tolist(), axis=None),
                mode='lines',
                line=dict(color='#BCC2D7',width=2))
trace1= Scatter(x=np.squeeze(data0['subfig_x'].tolist(), axis=None),
                y=np.squeeze(data0['subfig2_y2'].tolist(), axis=None),
                mode='lines',
                line=dict(color='#8895B1',width=2))
trace2= Scatter(x=np.squeeze(data0['subfig_x'].tolist(), axis=None),
                y=np.squeeze(data0['subfig3_y3'].tolist(), axis=None),
                mode='lines',
                line=dict(color='#546CBC',width=2))
trace3= Scatter(x=np.squeeze(data0['subfig_x'].tolist(), axis=None),
                y=np.squeeze(data0['subfig4_y4'].tolist(), axis=None),
                mode='lines',
                line=dict(color='#194568',width=2))

fig = make_subplots(rows=4,
                    cols=1)
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 2, 1)
fig.append_trace(trace2, 3, 1)
fig.append_trace(trace3, 4, 1)
fig['layout'].update(showlegend = False,
                     height=800 ,width = 880,
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 30, # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     ),)
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
fig["layout"]["xaxis4"].update({"title": "Time (s)","titlefont": {"size": 30}})
fig["layout"]["yaxis"].update({"title": "Origin","titlefont": {"size": 30}})
fig["layout"]["yaxis2"].update({"title": "Ewt-C1","titlefont": {"size": 30}})
fig["layout"]["yaxis3"].update({"title": "Ewt-C2","titlefont": {"size": 30}})
fig["layout"]["yaxis4"].update({"title": "Ewt-C3","titlefont": {"size": 30}})
# fig.write_image('images/MotionNoise.eps')
html_path = "../htmls/Ewt_Performance.html"
fig.write_image('../images/Ewt_Performance.eps')
pyplot(fig,filename=html_path)


