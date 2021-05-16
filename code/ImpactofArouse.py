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
colors=['rgba(247,183,112,1)','rgba(187,189,191,1)','rgba(233,155,122,1)',
        'rgba(236,111,70,1)','rgba(178,170,107,1)','rgba(143,238,146,1)','rgba(93,156,204,1)']
#画图
fig = go.Figure()
for d,name,color in zip(data,names,colors):
    fig.add_trace(go.Box(y=d,
                         name=name,
                         fillcolor=color,
                         # line_color=color,
                         boxpoints='all'))

#设置参数
fig.update_layout(
                showlegend=False,
                height=630 ,width = 750,    #画布大小
                font=dict(
                    family="Times New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white',
                yaxis=dict(
                    range=[90,100]
                )
                )
fig.update_xaxes(showgrid=True,#将网格去掉
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#dbddde',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(title='Accuracy(%)',
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#dbddde',
                 )
html_path = os.path.join(h_path,"ImpactofArouse.html")
pio.write_image(fig,os.path.join(i_path,'ImpactofArouse.eps'))
pyplot(fig,filename=html_path)