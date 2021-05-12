import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot as plt

size_list=[5,10,15,20,25,30,35,40,44]
result = []
for size in size_list:
    true_list = []
    score_list = []
    filepath="../data/result_{}.txt".format(size)
    with open(filepath) as f:
        text = f.read()
        text = eval(text)
    for key in text.keys():
        for t_s in text[key]:
            true_list.append(t_s[0])
            score_list.append(t_s[1])
    y_true = np.array(true_list)
    y_score = np.array(score_list)
    x2, y2, thresholds = roc_curve(y_true, y_score)
    AUC_ROC = roc_auc_score(y_true, y_score)
    l = len(x2)
    i1 = 10000
    y1 = [i / i1 for i in range(i1, 0, -1)]
    x1 = [i / i1 for i in range(i1)]
    idx = 0
    diff = 0.008
    for j1 in range(i1):
        for j2 in range(l):
            flag1 = abs(x1[j1] - x2[j2]) < diff
            flag2 = abs(y1[j1] - y2[j2]) < diff
            if flag1 & flag2:
                idx = j2
                break
        if flag1 & flag2:
            break
    EER = x2[idx]
    result.append(EER)
plt.plot(size_list,result)
plt.ylim((0,0.1))
plt.xlabel("size")
plt.ylabel("EER")
out_fig=plt.gcf()
out_fig.savefig('../images/EERs.eps',format='eps',dpi=1000)
plt.show()