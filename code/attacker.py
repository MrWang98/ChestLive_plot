import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot as plt
import plotly as py
import plotly.express as px
import plotly.graph_objects as go
import os
pyplot = py.offline.plot

with open("../data/attacker_result.txt") as f:
    text = f.read()
    text = eval(text)

if os.path.exists("../htmls"):
    h_path="../htmls"
else:
    h_path="."

font = {'family': 'Times new roman',
        'size': 24,
        }

true=[]
score=[]
keys=[]
for key in text.keys():
    s=key.split("_")
    if(len(s)>1):
        true_list = []
        score_list = []
        keys.append(s[0])
        for x in text[s[0]]:
            true_list.append(x[0][1])
            score_list.append(x[1][1])
        for x in text[key]:
            true_list.append(x[0][1])
            score_list.append(x[1][1])
        true.append(true_list)
        score.append(score_list)

for true_list,score_list,key in zip(true,score,keys):
    y_true = np.array(true_list)
    y_score = np.array(score_list)
    x2, y2, thresholds = roc_curve(y_true, y_score)
    AUC_ROC = roc_auc_score(y_true, y_score)
    l=len(x2)
    i1=10000
    y1 = [i/i1 for i in range(i1,0,-1)]
    x1 = [i/i1 for i in range(i1)]
    idx=0
    diff=0.01
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

    fig = px.area(
        x=x2, y=y2,
        labels=dict(x='False Positive Rate', y='True Positive Rate'),
        color='pink'
    )
    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    fig.update_xaxes(constrain='domain')
    fig.update_layout(annotations=[
        go.layout.Annotation(
            showarrow=False,
            text='AUC: {:.4f}<br>EER: {:.2f}%'.format(AUC_ROC, EER*100),
            x=0.5,
            y=0.1,
            font=dict(
                size=22,
                color="black"
            )

        )])
    fig['layout'].update(
        font_size=24.5,
        polar_radialaxis_ticksuffix='%',
        polar_angularaxis_rotation=90,
        showlegend=False,
        height=600, width=700,
        font=dict(
            family="Time New Roman",  # 所有标题文字的字体
            size=23.5,  # 所有标题文字的大小
        ),
        # grid=False
    )
    # fig.show()
    html_path = os.path.join(h_path, "{}_attacker.html".format(key))
    pyplot(fig, filename=html_path)
    # break

    # r =plt.figure(figsize=(8,7))
    # plt.plot(x2,y2,'-')
    # plt.text(0.3, 0.2,'AUC: %0.4f\nEER: %0.4f' % (AUC_ROC, EER),fontsize=20)
    # plt.fill_between(x2, y2, interpolate=True, color='pink', alpha=0.5)
    # plt.xlabel("False Positive Rate",fontdict=font)
    # plt.ylabel("True Positive Rate",fontdict=font)
    # plt.yticks(fontproperties='Times New Roman', size=22, weight='ultralight')
    # plt.xticks(fontproperties='Times New Roman', size=22, weight='ultralight')
    # ax=plt.gca()
    # ax.spines['bottom'].set_linewidth(1);  ###设置底部坐标轴的粗细
    # ax.spines['left'].set_linewidth(1);  ####设置左边坐标轴的粗细
    # ax.spines['right'].set_linewidth(1);  ###设置右边坐标轴的粗细
    # ax.spines['top'].set_linewidth(1);  ####设置上部坐标轴的粗细
    # out_fig = plt.gcf()
    # out_fig.savefig("../images/{}_attacker.eps".format(key),format="eps",dpi=1000)
    # plt.show()
    # break

