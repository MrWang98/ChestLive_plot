import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot as plt
import math
import os
import plotly as py
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
pyplot = py.offline.plot

if os.path.exists("../data"):
    with open("../data/result_47.txt") as f:
        text=f.read()
        person=eval(text)
else:
    with open("result_47.txt") as f:
        text=f.read()
        person=eval(text)

if os.path.exists("../images"):
    i_path="../images"
else:
    i_path="."

if os.path.exists("../htmls"):
    h_path="../htmls"
else:
    h_path="."

auc_list=[]
result=[]
k_v=list(person.items())
for i in range(len(k_v)):
    t=k_v[i][1]
    true_list=[]
    score=[]
    for tmp in t:
        true_list.append(tmp[0])
        score.append(tmp[1])

    y_true = np.array(true_list)
    y_score = np.array(score)
    x2, y2, thresholds = roc_curve(y_true, y_score)
    AUC_ROC = roc_auc_score(y_true, y_score)
    auc_list.append(AUC_ROC)
    l=len(x2)
    i1=10000
    y1 = [i/i1 for i in range(i1,0,-1)]
    x1 = [i/i1 for i in range(i1)]
    idx=0
    diff=0.05
    for j1 in range(i1):
        for j2 in range(l):
            flag1 = abs(x1[j1]-x2[j2])<diff
            flag2 = abs(y1[j1]-y2[j2])<diff
            if flag1 & flag2:
                idx=j2
                break
        if flag1 & flag2:
            break
    EER = x2[idx]
    result.append(EER*100)
result.sort(reverse=True)

#带参数point会画出所有点，将point删掉的不会画出
# fig = px.box(result,points='all')
fig = px.box(result)

fig['layout'].update(
        showlegend=False,
        height=600 ,width = 650,
        font=dict(
            family="Time New Roman",  # 所有标题文字的字体
            size = 23.5, # 所有标题文字的大小
        ),
    )
fig["layout"]["xaxis"].update({"title": ""})
fig["layout"]["yaxis"].update({"title": "EER(%)","titlefont": {"size": 28}})
html_path = os.path.join(h_path,"EERs.html")
pio.write_image(fig,os.path.join(i_path,'boxplot.eps'))
pyplot(fig,filename=html_path)