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

file_name='pose.csv'
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
    for d in line[:-2]:
        if d=='':
            t.append(0)
        else:
            t.append(float(d)*100)
    data_pre.append(t)

# data=data_pre
# x=['U{}'.format(i+1) for i in range(len(data[0][:]))]
# names=['Sit on chair', 'Lying', 'Sit on sofa', 'Stand', 'Walk']

data_pre=np.array(data_pre)
data_pre=data_pre.T
idxs=[0,1,2,6,7,11,15,16]
average=[0 for i in range(data_pre.shape[1])]
data=[]
i=0
for idx in idxs:
    data.append(data_pre[idx][:])
    i=i+1
    for v in range(data_pre.shape[1]):
        average[v]=average[v]+data_pre[idx][v]
average=[d/i for d in average]

with open('average.csv','a') as f:
    for avg in average:
        f.write('{},'.format(avg))

x = ['Sit on chair', 'Lying', 'Sit on sofa', 'Stand', 'Walk']
names=['U{}'.format(i+1) for i in range(len(data))]

r=50;g=110;b=90
colors=['rgb({},{},{})'.format(r+(i+1)*8,g+(i+1)*18,b+(i+1)*6) for i in range(len(data))]

#画图
fig = go.Figure()
for d,name,color in zip(data,names,colors):
    fig.add_trace(go.Bar(showlegend=False,
                         x=x,
                         y=d,
                         name=name,
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
                height=590 ,width = 670,
                font=dict(
                    family="Time New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white',
                yaxis=dict(
                    range=[90,100],
                ),
                legend=dict(
                        orientation="h",  # 将legend改为横排放置
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1,
                        font=dict(
                            size=32,  # 25
                            color='black', )
                    ),
                )
fig.update_xaxes(showgrid=True,#将网格去掉
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(title='Accuracy(%)',
                 titlefont=dict(
                     size=34,
                 ),
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )
html_path = os.path.join(h_path,"Pose.html")
pio.write_image(fig,os.path.join(i_path,'Pose.eps'))
pyplot(fig,filename=html_path)