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
dataFile = '../data/StaticNoise.mat'
data0 = scio.loadmat(dataFile)

trace0= Scatter(x=np.squeeze(data0['xtic_static'].tolist(), axis=None),
                y=np.squeeze(data0['subfig1_y1'].tolist(), axis=None),
                mode='lines', name='Original chest motions',#legendgroup="group",
                line=dict(color='#9791AD',width=2))  ##55DDDD

trace1= Scatter(x=np.squeeze(data0['xtic_static'].tolist(), axis=None),
                y=np.squeeze(data0['subfig1_y2'].tolist(), axis=None),
                mode='lines', name='Moving average of original chest motions ',#legendgroup="group",
                line=dict(color='#DBAEAE', width=2.5, dash='dash'))

trace2= Scatter(x=np.squeeze(data0['xtic_static'].tolist(), axis=None),
                y=np.squeeze(data0['subfig2_y1'].tolist(), axis=None),
                mode='lines', name='Chest motions after static cancellation',#legendgroup="group1",
                line=dict(color='#B5C7C9',width=2))  ##55DDDD

trace3= Scatter(x=np.squeeze(data0['xtic_static'].tolist(), axis=None),
                y=np.squeeze(data0['subfig2_y2'].tolist(), axis=None),
                mode='lines', name='Moving average of original chest motions after static cancellation',#legendgroup="group1",
                line=dict(color='#89726C', width=2.5, dash='dash'))

fig = make_subplots(rows=2,
                    cols=1)
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 1)
fig["layout"]["template"] = "simple_white"
tick= list(range(0,len(data0['xtic_static'].tolist()),2))
fig["layout"]["xaxis2"].update({"title": "Time (s)","titlefont": {"size": 30}})
fig["layout"]["yaxis"].update({"title": "Amplitude","titlefont": {"size": 30}})
fig["layout"]["yaxis2"].update({"title": "Amplitude","titlefont": {"size": 30}})

fig['layout'].update(
                     height=700 ,width = 820,
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 30 , # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     ),
                    yaxis=dict(range=[2.75,3.25]),
                    legend = dict(orientation="h",  # 将legend改为横排放置
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1,
                                  #traceorder="grouped",
                                  #tracegroupgap = 20,
                                  #bordercolor = "black",
                                  #borderwidth = 2,

                                  font=dict(
                                  size=21,
                                  color='black', )
)
)
fig.update_xaxes(showgrid=True,#将网格去掉
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',
                 tickmode="array",
                 ticktext=tick,
                 tickvals=tick,
                 )
fig.update_yaxes(showgrid=True,
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )
html_path = "../htmls/static_noise.html"
fig.write_image('../images/static_noise.eps')
pyplot(fig,filename=html_path)