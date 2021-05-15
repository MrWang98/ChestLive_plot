#FAR [0.88,0.97,1.84]
import plotly.graph_objs as go
import plotly as py
import plotly.io as pio
pyplot = py.offline.plot

y=[0.88,0.97,1.84]
x_a=["Victim{}".format(i+1) for i in range(len(y))]
colors=['#8895B1','#9791A0','#9ca8b8']
fig=go.Figure()
for x,d,color in zip(x_a,y,colors):
    fig.add_trace(go.Bar(y=[d],
                         x=[x],
                         marker_color=color,
                         width=0.5,
                         ))
# Change the bar mode
fig.update_layout(height=600 ,width = 650,
                  font=dict(
                        family="Times New Roman",  # 所有标题文字的字体
                        size = 28 , # 所有标题文字的大小
                  ),
                  barmode='group',
                  showlegend=False,
                  template="simple_white",
                  )

fig.update_xaxes(showgrid=True,#将网格去掉
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(showgrid=True,
                 title="False accept rate",
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',

                 )
html_path = "../htmls/MimicAttack.html"
# pio.write_image(fig,'../images/MimicAttack.eps')
pyplot(fig,filename=html_path)