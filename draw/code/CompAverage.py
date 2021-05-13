# -*- coding: UTF-8 -*-
import os
import numpy as np
import plotly as py
import plotly.io as pio
import plotly.express as px
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
file_name='CompAverage.csv'
if os.path.exists("../data"):
    with open("../data/"+file_name) as f:
        text=f.readlines()
else:
    with open(file_name) as f:
        text=f.readlines()
data_pre=[]
for line in text:
    t=[]
    line=line.split(',')
    for d in line:
        if d == '':
            pass
        else:
            t.append(float(d) * 100)
    data_pre.append(t)

data=data_pre
x=['50db','55db','65db']
colors=['#CFC5BB','#AC9B91']
names=['WeChat','ChestLive']

#画图
fig = go.Figure()
for d,color,name in zip(data,colors,names):
    fig.add_trace(go.Bar(
                        x=x,
                        y=d,
                        name=name,
                        marker=dict(
                            color=color,
                        )
                        ))

#设置参数
fig.update_layout(
                height=520 ,width = 620,
                font=dict(
                    family="Times New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white',
                legend=dict(
                      orientation="h",  # 将legend改为横排放置
                      yanchor="bottom",
                      y=1.02,
                      xanchor="right",
                      x=1,
                      font=dict(
                          size=32, #22
                          color='black',
                      )
                ),
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
html_path = os.path.join(h_path,"ImpactofMethod.html")
pio.write_image(fig,os.path.join(i_path,'ImpactofMethod.eps'))
pyplot(fig,filename=html_path)