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

with open('../data/log_EER_size.csv','w') as f:
    average=[0 for i in range(20)]
    data_pre=[]
    names=[]
    for line in text:
        line=line.replace('\n','').split(',')
        t = []
        names.append(line[0])
        f.write(line[0]+',')
        for idx,d in enumerate(line[1:]):
            if d=='':
                t.append(0)
                f.write(str(0)+',')
            else:
                t.append(float(d)*100)
                f.write(str(float(d)*100)+',')
                average[idx]+=float(d)*100
        data_pre.append(t)
        f.write('\n')
    l=len(data_pre)
    f.write('Overall'+',')
    for idx in range(20):
        average[idx]=average[idx]/len(data_pre)
        f.write(str(average[idx])+',')

# person=['HNC','ChenJiaShun','QinDang','OuRunMin','MMH2','XiaTong',
#           'BianYaWei','ChenChangXin','HuangZhiHui','WuYuan','LiuSiYing',
#           'ZJX','LTM','LiZuoLong','ZCY']
person=['XuLian','HNC','OuRunMin','HuangJingWen','WuYuan','LTM','LiZuoLong']

data_pre=[]
names=[]
for line in text:
    line=line.replace('\n','').split(',')
    if line[0] in person:
        t = []
        names.append(line[0])
        for idx,d in enumerate(line[1:]):
            if d=='':
                t.append(0)
            else:
                t.append(float(d)*100)
        data_pre.append(t)

# with open('EERs.csv','w') as f:
#     for line in text:
#         line=line.replace('\n','').split(',')
#         t = []
#         names.append(line[0])
#         f.write(line[0]+',')
#         for idx,d in enumerate(line[1:]):
#             if d=='':
#                 t.append(0)
#             else:
#                 t.append(float(d)*100)
#                 f.write(str(float(d)*100)+',')
#         data_pre.append(t)
#         f.write('\n')

data=np.array(data_pre)
x=[i+1 for i in range(data.shape[1])]

names=["User{}".format(i+1) for i in range(data.shape[0])]

marker_shapes=['triangle-up-open','diamond-tall-open','circle-open','x-thin-open','y-up-open']
line_shapes=[ 'dot', 'dash', 'longdash', 'dashdot','solid', 'longdashdot']

fig = go.Figure()
for d,name,marker_shape,line_shape in zip(data,names,marker_shapes,line_shapes):
    fig.add_trace(go.Scatter(x=x,
                    y=d,
                    name=name,
                    mode='lines+markers',
                    marker=dict(
                        size=15,
                      symbol=marker_shape,
                    ),
                    line=dict(
                        width=3
                    )
                    ))
# for d,name in zip(data,names):
#     fig.add_trace(go.Scatter(x=x,
#                     y=d,
#                     name=name,
#                     # mode='lines+markers',
#                     marker=dict(
#                         size=15,
#                     ),
#                     line=dict(
#                         width=3,
#                               )
#                              ),
#                   )
fig.add_trace(go.Scatter(x=x,
                         y=average,
                         name='Overall',
                         mode='lines+markers',
                         marker=dict(
                             size=10,
                             symbol='line-ns-open',
                         ),
                         line=dict(
                             # dash=line_shape,
                             width=3
                         )
                ))
#????????????
fig.update_layout(
                height=500 ,width = 1000,
                font=dict(
                    family="Times New Roman",  # ???????????????????????????
                    size = 32, # ???????????????????????????
                ),
                template='simple_white',
                yaxis=dict(
                    # range=[0,50],
                    range=[0,70],
                ),
                xaxis=dict(
                    range=[0,20],
                    dtick=1,
                ),
                legend=dict(
                    orientation="h",  # ???legend??????????????????
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                    font=dict(
                        size=32,  # 25
                        color='black', )
                ),
)

fig.update_xaxes(showgrid=True,#???????????????
                 linewidth=1.5,
                 linecolor='black', # ????????????????????????
                 mirror=True,
                 gridcolor='#dbddde',
                 )     # ????????????  ??????????????????  ??????????????????????????????????????????  ????????????????????????
fig.update_yaxes(title='EER(%)',
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#dbddde',
                 )
html_path = os.path.join(h_path,"TrainSizeEer.html")
pio.write_image(fig,os.path.join(i_path,'TrainSizeEer.eps'))
pyplot(fig,filename=html_path)
