import os
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
names=['Alex','Ok Google','Choice','Describe','Guess','Hey Siri']
file_name='arouse.csv'
if os.path.exists("../data"):
    with open("../data/"+file_name) as f:
        text=f.readlines()
else:
    with open(file_name) as f:
        text=f.readlines()
data=[]
for line in text:
    t=[]
    line=line.split(',')
    for d in line[:-2]:
        if d=='':
            pass
        else:
            t.append(float(d)*100)
    data.append(t)

#画图
fig = go.Figure()
for d,name in zip(data,names):
    fig.add_trace(go.Box(y=d, name=name, boxpoints='all'))

#设置参数
fig.update_layout(
                showlegend=False,
                height=630 ,width = 750,    #画布大小
                font=dict(
                    family="Time New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white'
                )
fig.update_xaxes(showgrid=True,#将网格去掉
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(title='Accuracy(%)',
                 titlefont=dict(
                   size=36,
                 ),
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )
html_path = os.path.join(h_path,"Arouse.html")
# pio.write_image(fig,os.path.join(i_path,'Arouse.eps'))
pyplot(fig,filename=html_path)