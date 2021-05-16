import os
import plotly.graph_objs as go
from plotly.graph_objs import Scatter
from plotly.graph_objects import Line
import plotly as py
from datetime import datetime
import scipy.io as scio
from plotly.subplots import make_subplots
import numpy as np
import plotly.express as px
pyplot = py.offline.plot
dataFile = '../data/UserDemo.mat'

data0 = scio.loadmat(dataFile)
print(type(data0))
print(type(data0['U1_xtic']))

#date_end = datetime.today().strftime('%Y-%m-%d')
trace0= Scatter(x=np.squeeze(data0['U1_xtic'].tolist(), axis=None),
                y=np.squeeze(data0['MappedData1'].tolist(), axis=None),
                mode='lines', name='User1',
                line=dict(color='#A85658',width=2.5))  ##55DDDD
trace1= Scatter(x=np.squeeze(data0['U2_xtic'].tolist(), axis=None),
                y=np.squeeze(data0['MappedData2'].tolist(), axis=None),
                mode='lines', name='User2',
                line=dict(color='#CFC5BB',width=2.5))
trace2= Scatter(x=np.squeeze(data0['U3_xtic'].tolist(), axis=None),
                y=np.squeeze(data0['MappedData3'].tolist(), axis=None),
                mode='lines', name='User3',
                line=dict(color='#89726C',width=2.5),
                ) ##309D87
fig = make_subplots(rows=3,
                    cols=1,
                    #x_title='Time (s)',

                    #y_title="Normalized Amplitude"
                    )
fig.add_vline(x=2.5, line_width=3.5, line_dash="dash", line_color="blue")
fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 2, 1)
fig.append_trace(trace2, 3, 1)
tick= list(range(len(data0['U1_xtic'].tolist())))
ticky=list(np.linspace(0,1,5))
tick2= list(range(len(data0['U2_xtic'].tolist())))
tick3= list(range(len(data0['U3_xtic'].tolist())))
fig.update_yaxes(range=[0, 1])

fig['layout'].update(
                    height=800 ,width = 920,
                    font_family="Time New Roman",

                    #titlefont=dict(size=20),
       shapes=[
        dict(type="line",xref="x",yref="y",
            x0=5.451, y0=0,
            x1=5.451, y1=1,
             line=dict(color="#080808", width=2.5, dash="dashdot"),
        ),
        dict(type="line",xref="x",yref="y",
            x0=7.237, y0=0,
            x1=7.237, y1=1,
             line=dict(color="#080808", width=2.5, dash="dashdot"),
        ),
        dict(type="line",xref="x2",yref="y2",
            x0=3.416, y0=0,
            x1=3.416, y1=1,
            line=dict(color="#080808",width=2.5,dash="dashdot"),
        ),
        dict(type="line",xref="x2",yref="y2",
            x0=5.53, y0=0,
            x1=5.53, y1=1,
            line=dict(color="#080808", width=2.5, dash="dashdot"),
        ),
        dict(type="line",xref="x3",yref="y3",
            x0=8.204, y0=0,
            x1=8.204, y1=1,
            line=dict(color="#080808", width=2.5, dash="dashdot"),
        ),
        dict(type="line",xref="x3",yref="y3",
            x0=10.723, y0=0,
            x1=10.723, y1=1,
            line=dict(color="#080808", width=2.5, dash="dashdot"),
        ),

    ],

                     legend=dict(
                                  orientation="h",  # 将legend改为横排放置
                                  yanchor="bottom",
                                  y=1.02,
                                  xanchor="right",
                                  x=1,
                                 font=dict(
                         size =24,
                         color='black',)
                                 ),
                     xaxis= dict(
                                 showgrid=False ,#将网格去掉
                                 tickmode="array",
                                 ticktext=tick,
                                 tickvals=tick,
                                 linewidth=1.5,
                                 linecolor='black', # 将颜色设定为黑色
                                 mirror=True),
                     xaxis2= dict(
                                  showgrid=False,  # 将网格去掉
                                  tickmode="array",
                                  ticktext=tick2,
                                  tickvals=tick2,
                                  linewidth=1.5,
                                  linecolor='black',  # 将颜色设定为黑色
                                  mirror=True
                                  ),
                     xaxis3= dict(zeroline= False,
                                  showgrid=False,  # 将网格去掉
                                  tickmode="array",
                                  ticktext=tick3,
                                  tickvals=tick3,
                                  linewidth=1.5,
                                  linecolor='black',  # 将颜色设定为黑色
                                  mirror=True
                                  ),
                     yaxis= dict(
                                 showgrid=False ,#将网格去掉
                                 tickmode="array",
                                 ticktext=ticky,
                                 tickvals=ticky,
                                 linewidth=1.5,
                                 linecolor='black', # 将颜色设定为黑色
                                 mirror=True),
                     yaxis2= dict(
                                  showgrid=False,  # 将网格去掉
                                  tickmode="array",
                                  ticktext=ticky,
                                  tickvals=ticky,
                                  linewidth=1.5,
                                  linecolor='black',  # 将颜色设定为黑色
                                  mirror=True
                                  ),
                     yaxis3= dict(
                                  showgrid=False,  # 将网格去掉
                                 # showline=True,
                                  tickmode="array",
                                  ticktext=ticky,
                                  tickvals=ticky,
                                  linewidth=1.5,
                                  linecolor='black',  # 将颜色设定为黑色
                                  mirror=True
                                  ),
                     font=dict(
                         family="Time New Roman",  # 所有标题文字的字体
                         size = 29 , # 所有标题文字的大小
                         # color="RebeccaPurple" , # 所有标题的颜色
                     )




)  #zeroline显示的是零那条线,visible代表的就是竖着的线

fig["layout"]["template"] = "simple_white"
fig["layout"]["xaxis3"].update({"title": "Time (s)","titlefont": {"size": 30}})# "titlefont": {"color": "pink"}
fig["layout"]["yaxis2"].update({"title": "Normalized Amplitude","titlefont": {"size": 30}})


fig.update_xaxes(showgrid=True,#将网格去掉
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black', # 将颜色设定为黑色
                 mirror=True,
                 gridcolor='#F2F2F2',

                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(showgrid=True,
                 #showline=True,
                 linewidth=1.5,
                 linecolor='black',
                 mirror=True,
                 gridcolor='#F2F2F2',

                 )
fig.update_layout(
    annotations=[
        dict(
            x=4.311,
            y=0.331,

            xref="x2",
            yref="y2",
            showarrow=True,
            arrowhead=2,
            arrowsize=3.5,

            #opacity=0.5,
            ax=0,
            ay=-376,
        ),
        dict(
            x=6.338,
            y=0.2618,

            xref="x1",
            yref="y1",
            showarrow=True,
            arrowhead=2,
            arrowsize=3.5,
            text='"Hey, Siri"',
            # opacity=0.5,
            ax=0,
            ay=-165,
        ),
        dict(
            x=9.502,
            y=0.243,

            xref="x3",
            yref="y3",
            showarrow=True,
            arrowhead=2,
            arrowsize=3.5,


            # opacity=0.5,
            ax=0,
            ay=-615,
        ),

    ]
)

fig.update_layout(font=dict(
        family="Times New Roman",  # 所有标题文字的字体
    ),)
fig.update_xaxes(showgrid=True,
                 gridcolor='#dbddde',
                 )     # 加上这个  四周都是黑色  ，不加的话只有左下两条线黑色  （就是镜像过去）
fig.update_yaxes(showgrid=True,
                 gridcolor='#dbddde',
                 )
fig.update_annotations(startarrowsize=20)
fig.update_annotations(arrowcolor='#194568')
#fig.update_annotations(arrowcolor='#7b8b6f')
#fig.update_annotations(borderwidth=60)
#fig.update_annotations(width=50)
#fig.add_vline(x=2.5, line_width=3.5, line_dash="dash", line_color="#BDBDBD")
html_path="../htmls/ChestExample.html"
fig.write_image('../images/ChestExample.eps') #ChestExample
#fig.write_image('../images/ChestExample.jpg') #ChestExample

pyplot(fig,filename=html_path)



# x1 = np.array(x1)
# y1 = np.array(y1)
# print(type(x1),type(y1))
# print(x1,y1)
# x1 = np.squeeze(x1,axis = None)
# y1 = np.squeeze(y1,axis = None)
# print(x1,y1)
# fig = px.line(x=x1, y=y1)
# fig.show()