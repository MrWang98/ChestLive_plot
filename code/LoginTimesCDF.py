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



x_range=5
x=[i for i in range(x_range)]
average=[0 for i in range(x_range)]
# x=[0]
# for i in range(1,x_range):
#     x.append(i);x.append(i)
person=['FCK','ZJX','ChenHaoRan','LuoZiYu','WZY','HouJingWen','LongTing','LXR']
data=[]
person={}
with open('../data/log_CDF.csv','w') as f:
    for key in text.keys():
        f.write(key+',')
        person[key]={0:0}
        sum=0
        for n in text[key]:
            sum+=1
            if n+1 not in person[key]:
                person[key][n+1]=1
            else:
                person[key][n+1]+=1
        t_y=[0]
        f.write(str(0)+',')
        for t_k in range(1,x_range):
            if t_k not in person[key]:
                t_y.append(float(1))
                average[t_k]+=1
                f.write(str(1)+',')
            else:
                person[key][t_k]=person[key][t_k-1]+person[key][t_k]
                average[t_k]+=person[key][t_k]/sum
                t_y.append(person[key][t_k]/sum)
                f.write(str(person[key][t_k]/sum)+',')
        f.write('\n')
        if key in person:
            data.append(t_y)

    f.write('Overall'+',')
    for i in range(len(average)):
        average[i]=average[i]/len(data)
        f.write(str(average[i])+',')

names = ['User{}'.format(i+1) for i in range(len(data))]
#画图
dashes=['longdashdot', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot'] #所有的线条类型
colors=['rgba(247,183,112,1)','rgba(187,189,191,1)','rgba(233,155,122,1)',
        'rgba(236,111,70,1)','rgba(178,170,107,1)','rgba(143,238,146,1)','rgba(93,156,204,1)']
fig = go.Figure()
for d,name,dash,color in zip(data,names,dashes,colors):
    fig.add_trace(go.Scatter(
        x=x,
        y=d,
        name=name,
        mode='lines',
        line=dict(
            color=color,#线条颜色
            shape='hv',#线条先平画再竖直画
            dash=dash,#线条类型
            width=4,#线条粗细
        )
    ))

fig.add_trace(go.Scatter(
        x=x,
        y=average,
        name='Overall',
        mode='lines',
        line=dict(
            color='black',#线条颜色
            shape='hv',#线条先平画再竖直画
            # dash=dash,#线条类型
            width=4,#线条粗细
        )
    ))

#设置参数
fig.update_layout(

                height=630 ,width = 750,    #画布大小
                font=dict(
                    family="Times New Roman",  # 所有标题文字的字体
                    size = 32, # 所有标题文字的大小
                ),
                template='simple_white',
                legend=dict(orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1,
                            font=dict(
                              color='black',
                            )
                            ),
                yaxis=dict(
                    range=[0,1],
                ),
                xaxis=dict(
                    range=[0,x_range-1],
                    tickmode = 'array',
                    tickvals = list(range(x_range)),
                ),
                )
fig.update_xaxes(showgrid=True,#将网格去掉
                 title='Number of speeches',
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#dbddde',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(title='CDF',
                 titlefont=dict(
                   size=36,
                 ),
                 showgrid=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#dbddde',
                 )
html_path = os.path.join(h_path,"LoginTimesCDF.html")
# pio.write_image(fig,os.path.join(i_path,'LoginTimesCDF.eps'))
pyplot(fig,filename=html_path)