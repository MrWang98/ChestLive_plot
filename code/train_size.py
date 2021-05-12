import numpy as np
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from matplotlib import pyplot as plt
from matplotlib.pyplot import MultipleLocator

# result = []
# for size in range(1,21):
#     true_list = []
#     score_list = []
#     filepath="../data/size_result/eer_size_{}.txt".format(size)
#     with open(filepath,'r') as f:
#         text = f.read()
#         text = text.replace("<tf.Tensor: shape=(), dtype=float32, numpy=",'')
#         text = text.replace(">",'')
#     text = eval(text)
#     for key in text.keys():
#         for t_s in text[key]:
#             true_list.append(t_s[0])
#             score_list.append(t_s[1])
#     y_true = np.array(true_list)
#     y_score = np.array(score_list)
#     x2, y2, thresholds = roc_curve(y_true, y_score)
#     AUC_ROC = roc_auc_score(y_true, y_score)
#     l = len(x2)
#     i1 = 10000
#     y1 = [i / i1 for i in range(i1, 0, -1)]
#     x1 = [i / i1 for i in range(i1)]
#     idx = 0
#     diff = 0.008
#     for j1 in range(i1):
#         for j2 in range(l):
#             flag1 = abs(x1[j1] - x2[j2]) < diff
#             flag2 = abs(y1[j1] - y2[j2]) < diff
#             if flag1 & flag2:
#                 idx = j2
#                 break
#         if flag1 & flag2:
#             break
#     EER = x2[idx]
#     result.append(EER)
# result = np.array(result)
# np.save("../data/size_result/EERs.npy",result)

font = {'family': 'Times new roman',
        'size': 24,
        }

result = np.load("../data/size_result/EERs.npy")
result = [i*100 for i in result]


# r =plt.figure(figsize=(10,7))
#
# x_major_locator=MultipleLocator(5)
# y_major_locator=MultipleLocator(5)
# plt.plot(range(1,21),result)
#
# ax=plt.gca()
# #ax为两条坐标轴的实例
# ax.xaxis.set_major_locator(x_major_locator)
# #把x轴的主刻度设置为1的倍数
# ax.yaxis.set_major_locator(y_major_locator)
# #把y轴的主刻度设置为10的倍数
#
# plt.ylim((0,30))
# plt.xlabel("Train Size",fontdict=font)
# plt.ylabel("EER",fontdict=font)
# plt.yticks(fontproperties='Times New Roman', size=22, weight='light')
# plt.xticks(fontproperties='Times New Roman', size=22)
# out_fig=plt.gcf()
# out_fig.savefig('../images/train_size_eer.eps',format='eps',dpi=1000)
# plt.show()