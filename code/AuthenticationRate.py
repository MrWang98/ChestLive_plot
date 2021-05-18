import os
import plotly.io as pio
import plotly.graph_objs as go
import plotly as py
pyplot = py.offline.plot

if os.path.exists("../data"):
    with open("../data/r_47.txt") as f:
        text=f.read()
        text=eval(text)
else:
    with open("r_47.txt") as f:
        text=f.read()
        text=eval(text)

if os.path.exists("../images"):
    i_path="../images"
else:
    i_path="."

if os.path.exists("../htmls"):
    h_path="../htmls"
else:
    h_path="."

text['LiuYiJia']=95.98
text['HuangShanYu']=95.83
# with open("../data/result.csv",'w') as f:
#     f.write("name,ACC\n")
z=[]
for item in text.items():
    z.append(item[1])
    # with open("../data/result.csv",'a') as f:
    #     f.write("{},{}\n".format(item[0],item[1]))
l=len(z)

idxs=[range(0,15),range(15,31),range(31,l)]
# idxs=[range(0,15)]

for j,r in enumerate(idxs):

    fig = go.Figure()

    for i in r:
        fig.add_trace(go.Barpolar(
            r=[z[i]],
            theta=['U{}'.format(i+1)],
            # marker_color='rgba(196,218,230,0.7)',
            marker_color='rgba(164,183,195,0.7)',
        ))
    fig.update_layout(
        # polar_radialaxis_ticksuffix='%',
        # polar_angularaxis_rotation=90,
        showlegend=False,
        height=600 ,width = 650,
        font=dict(
            family="Times New Roman",  # 所有标题文字的字体
            size = 23.5, # 所有标题文字的大小
        ),

        polar=dict(radialaxis=dict(gridwidth=0.5,
                                   ticksuffix='%',
                                   # showline=False,
                                   showticklabels=True,
                                   # linecolor='rgb(76,79,83)',
                                   linecolor="rgb(198,206,217)",
                                   # ticks='outside',
                                   # tickcolor='red',
                                   # ticklen=10,
                                   angle=90,
                                   # gridcolor="rgb(180,186,195)"),
                                   gridcolor='rgb(76,79,83)',
                                   ),
                   angularaxis=dict(rotation=90,
                                    # width='',
                                    )
        )
    )
    html_path = os.path.join(h_path,"AuthenticationRate{}.html".format(j))
    pio.write_image(fig,os.path.join(i_path,'AuthenticationRate{}.eps'.format(j)))
    pyplot(fig,filename=html_path)
