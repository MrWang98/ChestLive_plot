import os
import numpy as np
import plotly as py
import plotly.io as pio
import plotly.express as px
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

font = {'family': 'Times new roman',
        'size': 24,
        }
if os.path.exists("../data"):
    true_list = np.load("../data/true.npy")
    score_list = np.load("../data/score.npy")
else:
    true_list = np.load("true.npy")
    score_list = np.load("score.npy")


true=[]
score=[]
for idx,y_t in enumerate(true_list):
  score.append(score_list[idx][1])
y_true = np.array(true_list)
y_score = np.array(score)
x2, y2, thresholds = roc_curve(y_true, y_score)
AUC_ROC = roc_auc_score(y_true, y_score)
l=x2.shape[0]
y1 = [i/l for i in range(l,0,-1)]
x1 = [i/l for i in range(l)]
idx=0
for j1 in range(l):
    for j2 in range(l):
        flag1 = abs(x1[j1]-x2[j2])<0.0005
        flag2 = abs(y1[j1]-y2[j2])<0.0005
        if flag1&flag2:
            idx=j2
EER = x2[idx]


fig=go.Figure()
fig.add_trace(go.Scatter(x=x2,
                         y=y2,
                         fill='tozeroy',
                         fillcolor='rgb(255,209,196)',
                         line=dict(width=3,
                                   color='rgba(247,143,116,0.7)',)
                        ))


fig.update_layout(annotations=[
                        go.layout.Annotation(
                            showarrow=False,
                            text='AUC: {:.4f}<br>EER: {:.2f}%'.format(AUC_ROC, EER*100),
                            x=0.5,
                            y=0.1,
                            font=dict(
                                size=18,
                                color="black"
                            )
                        )],
                    showlegend=False,
                    height=450, width=500,
                    font=dict(
                    family="Times New Roman",  # 所有标题文字的字体
                    size=20,  # 所有标题文字的大小
                    ),
                    yaxis=dict(
                        range=[-0.04,1.04],
                    ),
                    xaxis=dict(
                        range=[-0.04,1.04],
                        dtick=0.2,
                    ),
)
fig.update_yaxes(scaleanchor="x", scaleratio=1,title='True positive rate')
fig.update_xaxes(constrain='domain',title='False positive rate')
html_path = os.path.join(h_path, "BaseRoc.html")
# pio.write_image(fig,os.path.join(i_path,'BaseRoc.eps'))
pyplot(fig, filename=html_path)