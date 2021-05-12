import os
import numpy as np
import plotly as py
import plotly.io as pio
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
file_name='distance.csv'
if os.path.exists("../data"):
    with open("../data/"+file_name) as f:
        text=f.readlines()
else:
    with open(file_name) as f:
        text=f.readlines()
data_pre=[]
average=[]
for line in text:
    t=[]
    a=0
    i=0
    line=line.split(',')
    for d in line:
        if d == '':
            pass
        else:
            a=a+float(d)*100
            i=i+1
            t.append(float(d) * 100)
    data_pre.append(t)
    average.append(a/i)

# idxs=[0,3,10,12,14,17]


# idxs=[0]
# data=[[],[],[]]
# for i,line in enumerate(data_pre):
#     for idx in idxs:
#         data[i].append(line[idx])
data=data_pre
names=['5','10','15','20','25','30']
x=['U{}'.format(i+1) for i in range(len(data[0][:]))]

# data_pre=np.array(data_pre).T
# data=[]
# for idx in idxs:
#     data.append(data_pre[idx][:])
# names=['U{}'.format(i+1) for i in range(len(data))]
# x=['5','10','15','20','25','30']

#画图
fig = go.Figure()
for d,name in zip(data,names):
    fig.add_trace(go.Bar(
                         x=x,
                         y=d,
                         name=name,
                         # boxpoints='all',
                         ))

#设置参数
fig.update_layout(
                # showlegend=False,
                height=520 ,width = 1000,
                font=dict(
                    family="Time New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white',
                yaxis=dict(
                    range=[80,100],
                ),
                )
fig.update_xaxes(title='Distance(cm)',
                 showgrid=True,#将网格去掉
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(title='Accuracy(%)',
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )
html_path = os.path.join(h_path,"Distance.html")
# pio.write_image(fig,os.path.join(i_path,'Distance.eps'))
pyplot(fig,filename=html_path)