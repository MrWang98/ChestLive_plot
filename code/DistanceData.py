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




DistanceData = pd.DataFrame([98.44,	98.52	,97.58,	97.3,	98.12	,97.0],
                            columns=['Distance'],
                            index=np.arange(5, 35, 5))
fig = go.Figure([
                 go.Bar(name='User1', x=DistanceData.index, y=[98.44,98.52,97.58,97.3,98.37,97.72], marker_color='#9FBCC2',width=2),
                 go.Bar(name='User2', x=DistanceData.index, y=[97.86,98.33,97.71,97.5,97.14,92.92], marker_color='rgb(175,199,191)',width=2),
                 ]
                )


fig['layout'].update(
height=520 ,width = 620,
font=dict(
family="Time New Roman",  # 所有标题文字的字体
size = 32 , # 所有标题文字的大小
),
    legend=dict(
        orientation="h",  # 将legend改为横排放置
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1,
        # bordercolor ="black",
        # borderwidth = 2,
        font=dict(
            size=32,  # 25
            color='black', )
    ),
)
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
fig["layout"]["xaxis"].update({"title": "Distance (cm)","titlefont": {"size": 32}})# "titlefont": {"color": "pink"}
fig["layout"]["yaxis"].update({"title": "Accuracy (%)","titlefont": {"size": 32}})
fig["layout"]["template"] = "simple_white"
# fig.write_image('images/DiatanceData.eps')
html_path = "../htmls/ImpactofDistance.html"
fig.write_image('../images/ImpactofDistance.eps')
pyplot(fig,filename=html_path)