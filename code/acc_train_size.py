import os
import numpy as np
import plotly as py
import plotly.io as pio
import plotly.graph_objects as go
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
pyplot = py.offline.plot

# with open("../data/size_result/eer_size_10.txt") as f:
#     text = f.read()
#     text = text.replace("<tf.Tensor: shape=(), dtype=float32, numpy=", '')
#     text = text.replace(">",'')
#     text = eval(text)
#
# person={}
# for size in range(1,21):
#     true_dict = {}
#     score_dict = {}
#     filepath="../data/size_result/eer_size_{}.txt".format(size)
#     with open(filepath,'r') as f:
#         text = f.read()
#         text = text.replace("<tf.Tensor: shape=(), dtype=float32, numpy=",'')
#         text = text.replace(">",'')
#     text = eval(text)
#     for key in text:
#
#         t_count=0
#         count=0
#         for r_p in text[key]:
#             if r_p[0]==0 and r_p[1]<0.5:
#                 t_count+=1
#             elif r_p[0]==1 and r_p[1]>0.5:
#                 t_count+=1
#             count+=1
#         if key not in person:
#             person[key]=[]
#         person[key].append(t_count/count)
# print()

# with open('../data/acc.csv','w') as f:
#     for key in person.keys():
#         f.write(key+',')
#         for v in person[key][:-1]:
#             f.write(str(v)+',')
#         f.write(str(person[key][-1])+'\n')

if os.path.exists("../images"):
    i_path="../images"
else:
    i_path="."
if os.path.exists("../htmls"):
    h_path = "../htmls"
else:
    h_path = "."

file_name='acc.csv'
if os.path.exists("../data"):
    with open("../data/"+file_name) as f:
        text=f.readlines()
else:
    with open(file_name) as f:
        text=f.readlines()

person=['HNC','OuRunMin','WuYuan','LTM','LiZuoLong']

data_pre=[]
names=[]
for line in text:
    line=line.split(',')
    if line[0] in person:
        t = []
        names.append(line[0])
        for d in line[1:-1]:
            if d=='':
                t.append(0)
            else:
                t.append(float(d)*100)
        data_pre.append(t)

data=np.array(data_pre)
x=[i+1 for i in range(data.shape[1])]
names=["User{}".format(i+1) for i in range(data.shape[0])]

dashes=['dot', 'dash', 'longdash', 'dashdot', 'longdashdot'] #所有的线条类型

fig = go.Figure()
for d,name,dash in zip(data,names,dashes):
    fig.add_trace(go.Scatter(x=x,
                             y=d,
                             name=name,
                             mode='lines',
                             line=dict(
                                 dash=dash,  # 线条类型
                             )
                    ))

#设置参数
fig.update_layout(
                height=500 ,width = 650,
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
                        size=32,  # 25
                        color='black', )
                ),
                xaxis=dict(
                    range=[0,20],
                ),
                yaxis=dict(
                    range=[0,100],
                ),
)

fig.update_xaxes(showgrid=True,#将网格去掉
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
html_path = os.path.join(h_path,"acc.html")
# pio.write_image(fig,os.path.join(i_path,'EERs.eps'))
pyplot(fig,filename=html_path)