import numpy as np
import plotly.io as pio
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot as plt
import plotly as py
import plotly.express as px
import plotly.graph_objects as go
import os
pyplot = py.offline.plot



if os.path.exists("../images"):
    i_path="../images"
else:
    i_path="."
if os.path.exists("../htmls"):
    h_path = "../htmls"
else:
    h_path = "."

file_name='attacker_result.txt'
with open("../data/"+file_name) as f:
    text = f.read()
    text = eval(text)

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

fillcolors=['rgba(164,173,248,0.7)','rgba(255,209,196,0.7)','rgba(201,228,219,0.7)']
linecolors=['rgb(99,110,250)','rgb(247,143,116)','rgb(130,187,172)']


for true_list,score_list,key,fillcolor,linecolor in zip(true,score,keys,fillcolors,linecolors):
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

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=x2,
            y=y2,
            fill='tozeroy',
            fillcolor=fillcolor,

            line=dict(
                color=linecolor,
                width=4,
            )
        )
    )
    # fig = px.area(
    #     x=x2, y=y2,
    #     labels=dict(x='False Positive Rate', y='True Positive Rate'),
    #     width=1000,
    #     # color='pink'
    # )
    fig.update_yaxes(scaleanchor="x",
                     scaleratio=1,
                     title='True positive rate')
    fig.update_xaxes(constrain='domain',
                     title='False positive rate',)
    fig.update_layout(

        annotations=[
        go.layout.Annotation(
            showarrow=False,
            text='AUC: {:.4f}<br>EER: {:.2f}%'.format(AUC_ROC, EER*100),
            x=0.5,
            y=0.1,
            font=dict(
                size=22,
                color="black"
            ),)],
        font_size=24.5,
        polar_radialaxis_ticksuffix='%',
        polar_angularaxis_rotation=90,
        showlegend=False,
        height=600, width=700,
        font=dict(
            family="Times New Roman",  # 所有标题文字的字体
            size=23.5,  # 所有标题文字的大小
        ),
        yaxis=dict(
            range=[-0.04,1.04],
        ),
        xaxis=dict(
            range=[-0.04,1.04],
        ),
    )
    html_path = os.path.join(h_path, "{}_attacker.html".format(key))
    # pio.write_image(fig,os.path.join(i_path,"{}_attacker.eps".format(key)))
    pyplot(fig, filename=html_path)

