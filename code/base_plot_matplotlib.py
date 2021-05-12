import matplotlib
from matplotlib import pyplot as plt
import os
import numpy as np

with open("../data/r_47.txt") as f:
    text=f.read()
    text=eval(text)
text['LiuYiJia']=95.98
text['HuangShanYu']=95.83
z=[]
for item in text.items():
    z.append(item[1])
l=len(z)
labels=['U{}'.format(i+1) for i in range(l)]
theta = np.linspace(0.0, 2 * np.pi, l, endpoint=False)
radii = z
width = (2 * np.pi / l) - 0.01
colors = [(196/255,218/255,230/255) for i in range(l)]
ax = plt.subplot(projection='polar')
# labels = matplotlib.artist.Artist.set_label((labels))
ax.bar(theta, radii, width=width, label=labels,bottom=0.0, color=colors, alpha=1)

plt.xlabel("acc")
fig=plt.gcf()
plt.show()