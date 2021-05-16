# -*- coding: UTF-8 -*-
import os
import random

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

colors=['rgba(210,204,3,1)','rgba(247,183,112,1)','rgba(187,189,191,1)','rgba(233,155,122,1)',
        'rgba(236,111,70,1)','rgba(178,170,107,1)','rgba(143,238,146,1)','rgba(93,156,204,1)']

# colors=['rgb(3,182,205)','rgb(201,222,47)','rgb(255,177,6)']
# colors=['rgba(22,173,66,0.5)','rgba(147,197,46,0.5)','rgba(243,223,6,0.5)']


#[185,122,86]

# with open('../data/colors.csv','a') as f:
#     colors=[]
#     r=50;g=56;b=154
#     for i in range(len(data)):
#         r_n=r+i*random.randint(5,20)
#         g_n=g+i*random.randint(5,15)
#         b_n=b-i*random.randint(5,15)
#         if r_n>255 or g_n>255 or b_n>255:
#             print('{},{},{}'.format(r_n,g_n,b_n))
#         elif r_n<0 or g_n<0 or b_n<0:
#             print('{},{},{}'.format(r_n,g_n,b_n))
#         colors.append('rgb({},{},{})'.format(r_n,g_n,b_n))
#         f.write('{}-{}-{},'.format(r_n,g_n,b_n))
#     f.write('\n')

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
                    range=[80,100],
                ),
                # bargroupgap=0.1,
                )
fig.update_xaxes(showgrid=False,#将网格去掉
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
                 # gridcolor='#F2F2F2',
                 gridcolor='#dbddde',
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
pio.write_image(fig,os.path.join(i_path,'ImpactofNoise.eps'))
pyplot(fig,filename=html_path)