import os
import numpy as np
import plotly as py
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
pyplot = py.offline.plot

if os.path.exists("../images"):
    i_path = "../images"
else:
    i_path = "."
if os.path.exists("../htmls"):
    h_path = "../htmls"
else:
    h_path = "."

#处理数据
x=['Left','Right','Center']

file_name='direction.csv'
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
data_pre=np.array(data_pre).T
# idxs=[1,2,5,6,16,-2,-1]
idxs=[0,1,2,5,6,10,16,20]
# data=[[],[],[]]
# for i,line in enumerate(data_pre):
#     for idx in idxs:
#         data[i].append(line[idx])
average=[0 for i in range(data_pre.shape[1])]
data=[]
i=0
for idx in idxs:
    data.append(data_pre[idx][:])
    i = i + 1
    for v in range(data_pre.shape[1]):
        average[v] = average[v] + data_pre[idx][v]
average = [d / i for d in average]

with open('average.csv','a') as f:
    for avg in average:
        f.write('{},'.format(avg))

colors=['rgba(210,204,3,1)','rgba(247,183,112,1)','rgba(187,189,191,1)','rgba(233,155,122,1)',
        'rgba(236,111,70,1)','rgba(178,170,107,1)','rgba(143,238,146,1)','rgba(93,156,204,1)']
names=['User{}'.format(i+1) for i in range(len(data))]
#画图
fig = go.Figure()
for d,name,color in zip(data,names,colors):
    # x = ['U{}'.format(i+1) for i in range(len(d))]
    fig.add_trace(go.Bar(
                         # showlegend=False,
                         name=name,
                         x=x,
                         y=d,
                         marker=dict(
                             color=color,
                         )))
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
fig.update_xaxes(showgrid=False,#将网格去掉
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )
fig.update_yaxes(showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#dbddde',
                 title='Accuracy(%)'
                 )
html_path = os.path.join(h_path,"ImpactofDirection.html")
pio.write_image(fig,os.path.join(i_path,'ImpactofDirection.eps'))
pyplot(fig,filename=html_path)