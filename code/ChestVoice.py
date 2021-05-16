import os
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
import plotly as py
import scipy.io as scio
from plotly.subplots import make_subplots
import numpy as np
pyplot = py.offline.plot
data_file = "../data/ChestVoice.mat"
data0 = scio.loadmat(data_file)

fig = go.Figure()

trace0= Scatter(x=np.squeeze(data0['subfig1_xtic'].tolist(), axis=None),
                y=np.squeeze(data0['subfig1_y'].tolist(), axis=None),
                mode='lines',
                line=dict(color='royalblue',width=2))  ##55DDDD
trace1= Scatter(x=np.squeeze(data0['subfig2_xtic'].tolist(), axis=None),
                y=np.squeeze(data0['subfig2_y'].tolist(), axis=None),
                mode='lines',
                line=dict(color='royalblue',width=1))
fig = make_subplots(rows=2,
                    cols=1,
                    )
fig.add_trace(trace0,1,1)
fig.add_trace(trace1,2,1)

fig.update_layout(
    height=730 ,width = 710,
    xaxis= dict(
        linecolor='black', # 将颜色设定为黑色
        mirror=True,
        tick0=0,
        dtick=2,
        range=[5,14.1],
    ),
    xaxis2 = dict(
        title="Time (s)",
        linecolor="black",
        mirror=True,
        tick0=0,
        dtick=0.5,
        range=[7.9,11],
    ),
    yaxis= dict(
        mirror=True,
        linecolor='black',
        title = "Normalized ampitude",
        tick0=0,
        titlefont=dict(size = 28.5),
        dtick=0.1,
        range=[0.25,0.72],
    ),
    yaxis2=dict(
        mirror=True,

        linecolor="black",
        title = "Normalized ampitude",
titlefont=dict(size = 28.5),
        tick0=0,
        dtick=1,
        range=[-1,1],
    ),

    font=dict(
        family="Times New Roman",  # 所有标题文字的字体
        size = 34, # 所有标题文字的大小
    ),

    shapes=[
        dict(type="line",xref="x",yref="y",
            x0=np.squeeze(data0['subfig1_seg1_start'].tolist()), y0=0,
            x1=np.squeeze(data0['subfig1_seg1_start'].tolist()), y1=1,
            line=dict(color="red",width=2.5),
        ),
        dict(type="line",xref="x",yref="y",
            x0=np.squeeze(data0['subfig1_seg1_end'].tolist()), y0=0,
            x1=np.squeeze(data0['subfig1_seg1_end'].tolist()), y1=1,
            line=dict(color="darkblue",width=2.5,dash="dash"),
        ),
        dict(type="line",xref="x",yref="y",
            x0=np.squeeze(data0['subfig1_seg2_start'].tolist()), y0=0,
            x1=np.squeeze(data0['subfig1_seg2_start'].tolist()), y1=1,
            line=dict(color="red",width=2.5),
        ),
        dict(type="line",xref="x",yref="y",
            x0=np.squeeze(data0['subfig1_seg2_end'].tolist()), y0=0,
            x1=np.squeeze(data0['subfig1_seg2_end'].tolist()), y1=1,
            line=dict(color="darkblue",width=2.5,dash="dash"),
        ),
        dict(type="line",xref="x2",yref="y2",
            x0=np.squeeze(data0['subfig2_seg1_start'].tolist()), y0=-1,
            x1=np.squeeze(data0['subfig2_seg1_start'].tolist()), y1=1,
            line=dict(color="red",width=2.5),
        ),
        dict(type="line",xref="x2",yref="y2",
            x0=np.squeeze(data0['subfig2_seg1_end'].tolist()), y0=-1,
            x1=np.squeeze(data0['subfig2_seg1_end'].tolist()), y1=1,
            line=dict(color="darkblue",width=2.5,dash="dash"),
        ),
        dict(type="line",xref="x2",yref="y2",
            x0=np.squeeze(data0['subfig2_seg2_start'].tolist()), y0=-1,
            x1=np.squeeze(data0['subfig2_seg2_start'].tolist()), y1=1,
            line=dict(color="red",width=2.5),
        ),
        dict(type="line",xref="x2",yref="y2",
            x0=np.squeeze(data0['subfig2_seg2_end'].tolist()), y0=-1,
            x1=np.squeeze(data0['subfig2_seg2_end'].tolist()), y1=1,
            line=dict(color="darkblue",width=2.5,dash="dash"),
        ),
    ],

    showlegend=False,

)

fig.update_layout(font=dict(
        family="Times New Roman",  # 所有标题文字的字体
    ),)
fig.update_xaxes(showgrid=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#dbddde',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#dbddde',
                 )

x0=np.squeeze(data0['subfig1_seg1_end'].tolist())
html_path = "../htmls/ChestVoice.html"

fig.write_image('../images/ChestVoice.eps')
pyplot(fig,filename=html_path)
