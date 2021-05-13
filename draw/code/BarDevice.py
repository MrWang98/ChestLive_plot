# -*- coding: UTF-8 -*-
import os
import numpy as np
import plotly as py
import plotly.io as pio
import plotly.graph_objects as go
pyplot = py.offline.plot

if os.path.exists("../images"):
    i_path="../images"
else:
    i_path="."
if os.path.exists("../htmls"):
    h_path = "../htmls"
else:
    h_path = "."

#处理数据
# names=['50db','55db','65db']
file_name='device.csv'
if os.path.exists("../data"):
    with open("../data/"+file_name) as f:
        text=f.readlines()
else:
    with open(file_name) as f:
        text=f.readlines()
x1=[]
x2=[]
y1=[]
y2=[]
for line in text:
    t=[]
    line=line.split(',')
    x1.append(line[0])
    x2.append(line[1])
    y1.append(float(line[2])*100)
    y2.append(float(line[3].replace('\n',''))*100)
x=['{}:{}'.format(d1,d2) for d1,d2 in zip(x1,x2)]

fig = go.Figure(data=[
    go.Bar(name='Enrollment', x=x, y=y1,marker_color='#CFC5BB',width=0.3),
    go.Bar(name='Login', x=x, y=y2,marker_color='#AC9B91',width=0.3),

])
#设置参数
fig.update_layout(
                legend=dict(
                    orientation="h",  # 将legend改为横排放置
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                    font=dict(
                        size=32,  # 22
                        color='black', )
                ),
                height=520 ,width = 1200,
                font=dict(
                    family="Times New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white',
                )
fig.update_xaxes(showgrid=True,#将网格去掉
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(title='Accuracy (%)',
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )


html_path = "../htmls/ImpactofDevice.html"
pio.write_image(fig,os.path.join(i_path,'ImpactofDevice.eps'))
pyplot(fig,filename=html_path)