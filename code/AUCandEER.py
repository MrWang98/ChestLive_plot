import os
import numpy as np
import plotly as py
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

from matplotlib import pyplot as plt
import math

pyplot = py.offline.plot

if os.path.exists("../htmls"):
    h_path="../htmls"
else:
    h_path="."

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

fig = px.area(x=x2, y=y2,
              labels=dict(x='False Positive Rate', y='True Positive Rate'),
              )

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
                        )],
                    showlegend=False,
                    height=600, width=700,
                    font=dict(
                    family="Time New Roman",  # 所有标题文字的字体
                    size=23.5,  # 所有标题文字的大小
                    ),
)
fig.update_yaxes(scaleanchor="x", scaleratio=1)
fig.update_xaxes(constrain='domain')
html_path = os.path.join(h_path, "base_roc.html")
pyplot(fig, filename=html_path)

# r =plt.figure()
# plt.plot(x2[idx], y2[idx], 'ro')
# plt.plot(x1,y1,'-')
# plt.plot(x2,y2,'-',label='AUC = %0.4f\nEER = %0.4f' % (AUC_ROC, EER))
# plt.plot(x2,y2,'-')
# plt.text(0.3, 0.2,'AUC: %0.4f\nEER: %0.4f' % (AUC_ROC, EER),fontsize=20)
# plt.fill_between(x2, y2, interpolate=True, color='pink', alpha=0.5)
# plt.title('ROC curve')
# plt.xlabel("FPR (False Positive Rate)")
# plt.ylabel("TPR (True Positive Rate)")
# plt.legend(loc="lower right")
# plt.show()
# plt.savefig("../picture/ROCandAUC.eps",format="eps")
# print("{}:{}".format(idx,x2[idx]))

# with open("../data/result_47.txt", 'r') as f:
#     text=f.read()
#     person=eval(text)
# k_v=list(person.items())
# result=[]
# for i in range(len(k_v)):
#     t=k_v[i][1]
#     true_list=[]
#     score=[]
#     for tmp in t:
#         true_list.append(tmp[0])
#         score.append(tmp[1])
#
#     y_true = np.array(true_list)
#     y_score = np.array(score)
#     x2, y2, thresholds = roc_curve(y_true, y_score)
#     AUC_ROC = roc_auc_score(y_true, y_score)
#     l=len(x2)
#     i1=10000
#     y1 = [i/i1 for i in range(i1,0,-1)]
#     x1 = [i/i1 for i in range(i1)]
#     idx=0
#     diff=0.008
#     for j1 in range(i1):
#         for j2 in range(l):
#             flag1 = abs(x1[j1]-x2[j2])<diff
#             flag2 = abs(y1[j1]-y2[j2])<diff
#             if flag1 & flag2:
#                 idx=j2
#                 break
#         if flag1 & flag2:
#             break
#     EER = x2[idx]
#     result.append([AUC_ROC,EER])
#     # r =plt.figure()
#     # plt.plot(x2[idx], y2[idx], 'ro')
#     # plt.plot(x1,y1,'-')
#     # plt.plot(x2,y2,'-',label='AUC = %0.4f\nEER = %0.4f' % (AUC_ROC, EER))
#     # plt.plot(x2,y2,'-')
#     # plt.text(0.3, 0.2,'AUC: %0.4f\nEER: %0.4f' % (AUC_ROC, EER),fontsize=20)
#     # plt.fill_between(x2, y2, interpolate=True, color='pink', alpha=0.5)
#     # plt.title('ROC curve')
#     # plt.xlabel("FPR (False Positive Rate)")
#     # plt.ylabel("TPR (True Positive Rate)")
#     # plt.legend(loc="lower right")
#     # plt.show()
#     # plt.savefig("../picture/ROCandAUC.eps",format="eps")
#     # print("{}:{}".format(idx,x2[idx]))
#
# print()