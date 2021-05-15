import os
import numpy as np
import plotly as py
import plotly.io as pio
import plotly.graph_objects as go
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
pyplot = py.offline.plot

if os.path.exists("../images"):
    i_path="../images"
else:
    i_path="."
if os.path.exists("../htmls"):
    h_path = "../htmls"
else:
    h_path = "."

file_name='result_24.txt'
if os.path.exists("../data"):
    with open("../data/"+file_name) as f:
        text=f.read()
        text=eval(text)
else:
    with open(file_name) as f:
        text=f.read()
        text = eval(text)

all={}
average=0
# TP,TN,FP,FN
with open('../data/FRR.csv','w') as f:
    count=0
    for key in text.keys():
        TP=0
        TN=0
        FP=0
        FN=0
        f.write(key+',')
        for d in text[key]:
            if d[0]==0 and d[0]==d[1]:
                TN+=1
            elif d[0]==1 and d[0]==d[1]:
                TP+=1
            elif d[0]==0 and d[1]==1:
                FP+=1
            elif d[0]==1 and d[1]==0:
                FN+=1
        f.write('{},{},{},{}\n'.format(TP,TN,FP,FN))
        all[key]=FN/(TP+FN)
        average+=all[key]
        count+=1

average=average/count

person=['XiaTong','OuRunMin','GQY','ZJX','XuLian','LengChao']
# marker_shapes=['triangle-up-open','diamond-tall-open','circle-open','x-thin-open','y-up-open']
# line_shapes=[ 'dot', 'dash', 'longdash', 'dashdot','solid', 'longdashdot']
names=['User{}'.format(i) for i in range(len(person))]
fig = go.Figure()
for p,name in zip(person,names):
    fig.add_trace(go.Bar(y=[all[p]*100],
                    x=[name],
                    ))
fig.add_trace(go.Bar(y=[average*100],
                     x=['Overall'],
                     ))
#设置参数
fig.update_layout(
                height=500 ,width = 750,
                font=dict(
                    family="Times New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white',
                # xaxis=dict(
                #     angle=45,
                # ),
                yaxis=dict(
                    dtick=0.2,
                    range=[0,2],
                ),
                showlegend=False,
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
fig.update_yaxes(title='FRR(%)',
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )
html_path = os.path.join(h_path,"FRR.html")
# pio.write_image(fig,os.path.join(i_path,'FRR.eps'))
pyplot(fig,filename=html_path)
