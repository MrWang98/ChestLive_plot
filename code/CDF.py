import os
import numpy as np
import plotly as py
import plotly.io as pio
import plotly.graph_objects as go
pyplot = py.offline.plot

if os.path.exists("../images"):
    i_path="../images"
else:
    i_path="."
if os.path.exists("../htmls"):
    h_path = "../htmls"
else:
    h_path = "."

#处理数据
# names=['50db','55db','65db']
file_name='CDF.txt'
if os.path.exists("../data"):
    with open("../data/"+file_name) as f:
        text=f.read()
        text=eval(text)
else:
    with open(file_name) as f:
        text = f.read()
        text = eval(text)
names = []
x=[]
data=[]
person={}
for key in text.keys():
    names.append(key)
    person[key]={}
    sum=0
    for n in text[key]:
        sum+=1
        if n+1 not in person[key]:
            person[key][n+1]=1
        else:
            person[key][n+1]+=1
    t_y=[]
    t_x=[]
    for t_k in person[key]:
        t_x.append(t_k)
        t_y.append(person[key][t_k]/sum)
    x.append(t_x)
    data.append(t_y)
print()