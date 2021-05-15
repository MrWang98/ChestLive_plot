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
file_name='noise.csv'
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

idxs=[1,2,3,6,7,9,11,12,]

data_pre=np.array(data_pre).T
average=[0 for i in range(data_pre.shape[1])]
data=[]
i=0
for idx in idxs:
    data.append(data_pre[idx][:])
    i = i + 1
    for v in range(data_pre.shape[1]):
        average[v] = average[v] + data_pre[idx][v]
average = [d / i for d in average]

names=['User{}'.format(i+1) for i in range(len(data))]
x=['50dB','55dB','65dB']

# colors=['rgb(126,20,86)','rgb(61,19,101)','rgb(0,19,114)','rgb(4,80,140)',
#         'rgb(0,135,147)','rgb(5,128,21)','rgb(96,150,4)','rgb(210,204,3)']

# colors=['rgb(142,76,140)','rgb(101,72,140)','rgb(36,48,130)','rgb(4,80,150)',
#          'rgb(0,135,147)','rgb(5,128,21)','rgb(96,150,4)','rgb(210,204,3)']

# colors=['rgb(0,146,211)','rgb(35,183,166)','rgb(18,148,56)','rgb(132,174,47)',
#         'rgb(211,194,8)','rgb(220,158,88)','rgb(222,133,31)','rgb(214,90,24)']

colors=['rgba(0,146,211,0.5)','rgba(35,183,166,0.5)','rgba(18,148,56,0.5)','rgba(132,174,47,0.5)',
        'rgba(211,194,8,0.5)','rgba(220,158,88,0.5)','rgba(222,133,31,0.5)','rgba(214,90,24,0.5)']

# colors=['rgb(3,182,205)','rgb(201,222,47)','rgb(255,177,6)']

# colors=['rgba(22,173,66,0.5)','rgba(147,197,46,0.5)','rgba(243,223,6,0.5)']

#画图
fig = go.Figure()
# for d,name,i in zip(data,names,range(len(data))):
#     fig.add_trace(go.Bar(
#                         x=x,
#                         y=d,
#                         name=name,
#                         showlegend=True,
#                         marker=dict(
#                             color=colors[i%3],
#                         )
#                         # boxpoints='all',
#                         ))
for d,name,color in zip(data,names,colors):
    fig.add_trace(go.Bar(
                        x=x,
                        y=d,
                        name=name,
                        showlegend=True,
                        marker=dict(
                            color=color,
                        )
                        # boxpoints='all',
                        ))
fig.add_scatter(x=x,
                y=average,
                name='Average',
                marker=dict(
                    color='black',
                )
                )
#设置参数
fig.update_layout(
                # showlegend=False,
                height=520 ,width = 620,
                font=dict(
                    family="Times New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white',
                yaxis=dict(
                    range=[90,100],
                )
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

# Change the bar mode
fig.update_layout(barmode='group',
                  legend=dict(
                      orientation="h",  # 将legend改为横排放置
                      yanchor="bottom",
                      y=1.02,
                      xanchor="right",
                      x=1,

                      font=dict(
                          size=26,
                          color='black', )
                  ),
                  )

html_path = os.path.join(h_path,"ImpactofNoise.html")
# pio.write_image(fig,os.path.join(i_path,'ImpactofNoise.eps'))
pyplot(fig,filename=html_path)