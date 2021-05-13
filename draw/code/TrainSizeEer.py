# -*- coding: UTF-8 -*-
import os
import numpy as np
import plotly as py
import plotly.io as pio
import plotly.graph_objects as go
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
pyplot = py.offline.plot

# result = {}
# for size in range(1,21):
#     true_dict = {}
#     score_dict = {}
#     filepath="../data/size_result/eer_size_{}.txt".format(size)
#     with open(filepath,'r') as f:
#         text = f.read()
#         text = text.replace("<tf.Tensor: shape=(), dtype=float32, numpy=",'')
#         text = text.replace(">",'')
#     text = eval(text)
#     for key in text.keys():
#         true_list=[]
#         score_list=[]
#         for t_s in text[key]:
#             true_list.append(t_s[0])
#             score_list.append(t_s[1])
#         y_true = np.array(true_list)
#         y_score = np.array(score_list)
#         x2, y2, thresholds = roc_curve(y_true, y_score)
#         AUC_ROC = roc_auc_score(y_true, y_score)
#         l = len(x2)
#         i1 = 10000
#         y1 = [i / i1 for i in range(i1, 0, -1)]
#         x1 = [i / i1 for i in range(i1)]
#         idx = 0
#         diff = 0.01
#         for j1 in range(i1):
#             for j2 in range(l):
#                 flag1 = abs(x1[j1] - x2[j2]) < diff
#                 flag2 = abs(y1[j1] - y2[j2]) < diff
#                 if flag1 & flag2:
#                     idx = j2
#                     break
#             if flag1 & flag2:
#                 break
#         EER = x2[idx]
#         if key not in result:
#             result[key]=[]
#         result[key].append(EER)
# with open('../data/size_result/EERs.txt','w') as f:
#     f.write(str(result))
# with open('../data/size_result/EERs.txt','r') as f:
#     text=f.read()
#     text=eval(text)
# with open('../data/EERs.csv','a') as f:
#     for key in result.keys():
#         f.write(key+',')
#         for value in result[key]:
#             f.write(str(value)+',')
#         f.write('\n')



if os.path.exists("../images"):
    i_path="../images"
else:
    i_path="."
if os.path.exists("../htmls"):
    h_path = "../htmls"
else:
    h_path = "."

file_name='EERs.csv'
if os.path.exists("../data"):
    with open("../data/"+file_name) as f:
        text=f.readlines()
else:
    with open(file_name) as f:
        text=f.readlines()

person=['HNC','ChenJiaShun','QinDang','OuRunMin','MMH2','XiaTong',
          'BianYaWei','ChenChangXin','HuangZhiHui','WuYuan','LiuSiYing',
          'ZJX','LTM','LiZuoLong','ZCY']

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

# Over ride the legend. and at the same time save the name of data.
names =['User{}'.format(i+1) for i in range(15)]

fig = go.Figure()
for d,name in zip(data, names):
    fig.add_scatter(x=x,
                    y=d,
                    name=name,
                    showlegend=True,
                    )

#设置参数
fig.update_layout(
                height=520 ,width = 1000,
                font=dict(
                    family="Times New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white',
                yaxis=dict(
                    range=[0,50],
                ),
)

fig.update_yaxes(title='EER (%)',
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )

fig.update_xaxes(title='Training set size',
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

html_path = os.path.join(h_path,"TrainSizeEer.html")
pio.write_image(fig,os.path.join(i_path,'TrainSizeEer.eps'))
pyplot(fig,filename=html_path)
