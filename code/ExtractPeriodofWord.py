import os
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
import plotly as py
import scipy.io as scio
import numpy as np
pyplot = py.offline.plot
data_file = "../data/ExtractPeriodofWord.mat"
data0 = scio.loadmat(data_file)

x_range = list(range(data0['subfig_y1'].shape[1]))
tick = list(range(int(data0['subfig_y1'].shape[1]/10000)))


fig = go.Figure()

trace0= Scatter(x=np.squeeze(data0['xtic'].tolist(), axis=None),
                y=np.squeeze(data0['subfig_y1'].tolist(), axis=None),
                mode='lines', name='Arouse words',
                line=dict(color='blue',width=1))  ##55DDDD
trace1= Scatter(x=np.squeeze(data0['xtic'].tolist(), axis=None),
                y=np.squeeze(data0['subfig_y2'].tolist(), axis=None),
                mode='lines', name='Prediction',
                line=dict(color='red',width=2.5))
fig.add_trace(trace0)
fig.add_trace(trace1)

fig["layout"].update(
    height=730 ,width = 710,
    font_family="Time New Roman",
    legend=dict(
        # bordercolor="black",
        # borderwidth=2,
        orientation="h",#将legend改为横排放置 v
        y=1.125,
        x=0.1,
        font=dict(
            size =30,
            color='black'
        )
    ),
    xaxis= dict(
        linecolor='black', # 将颜色设定为黑色
        mirror=True,
        range=[6.9,12.1]
    ),
    yaxis= dict(
        linecolor='black',
        mirror=True),

    xaxis_title = "Time (s)",
    yaxis_title = "Normalized ampitude",

    font=dict(
        family="Times New Roman",  # 所有标题文字的字体
        size = 34 , # 所有标题文字的大小
    )
)

fig.update_xaxes(showgrid=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#dbddde',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(title='Accuracy(%)',
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#dbddde',
                 )
html_path = "../htmls/ExtractPeriodofWord.html"

# fig.write_image('../images/ExtractPeriodofWord.eps')
pyplot(fig,filename=html_path)