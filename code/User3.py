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
data_path0 = "../data/User3.mat"

# data_path = os.path.join(data_path0,"data")
# data_file = os.path.join(data_path,"User3.mat")
data0 = scio.loadmat(data_path0)
# 如果项目路径下没有 "images" 文件夹，则创建该文件夹




fig = make_subplots(rows=1,
                    cols=2,
                    )
trace0= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,0].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#ADD8E6",width=2))  ##55DDDD
fig.add_trace(trace0,1,1)
trace1= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,1].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(240,235,229)",width=2))  ##55DDDD
fig.add_trace(trace1,1,1)
trace2= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,2].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(202,195,187)",width=2))  ##55DDDD
fig.add_trace(trace2,1,1)
trace3= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,3].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(216,202,175)",width=2))  ##55DDDD
fig.add_trace(trace3,1,1)
trace4= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,4].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(226,165,173)",width=2))  ##55DDDD
fig.add_trace(trace4,1,1)
trace5= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,5].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(246,246,246)",width=2))  ##55DDDD
fig.add_trace(trace5,1,1)
trace6= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,6].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(181,199,201)",width=2))  ##55DDDD
fig.add_trace(trace6,1,1)
trace7= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,7].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(201,192,181)",width=2))  ##55DDDD
fig.add_trace(trace7,1,1)
trace8= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,8].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#eee5f8",width=2))  ##55DDDD
fig.add_trace(trace8,1,1)
trace9= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,9].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(226,165,173)",width=2))  ##55DDDD
fig.add_trace(trace9,1,1)
trace10= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,10].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(175,199,191)",width=2))  ##55DDDD
fig.add_trace(trace10,1,1)

trace11= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,11].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(199,207,192)",width=2))  ##55DDDD
fig.add_trace(trace11,1,1)
trace12= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,12].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(221,214,202)",width=2))  ##55DDDD
fig.add_trace(trace12,1,1)
trace13= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,13].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(238,223,218)",width=2))  ##55DDDD
fig.add_trace(trace13,1,1)
trace14= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,14].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(234,208,209)",width=2))  ##55DDDD
fig.add_trace(trace14,1,1)
trace15= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,15].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(240,235,229)",width=2))  ##55DDDD
fig.add_trace(trace15,1,1)
trace16= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,16].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(224,205,207)",width=2))  ##55DDDD
fig.add_trace(trace16,1,1)
trace17= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,17].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(211,212,204)",width=2))  ##55DDDD
fig.add_trace(trace17,1,1)
trace18= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,18].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(223,214,215)",width=2))  ##55DDDD
fig.add_trace(trace18,1,1)
trace19= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,19].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(193,203,215)",width=2))  ##55DDDD
fig.add_trace(trace19,1,1)
trace20= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,10].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(137,114,108)",width=2))  ##55DDDD
fig.add_trace(trace20,1,1)


trace21= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,21].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(172,155,145)",width=2))  ##55DDDD
fig.add_trace(trace21,1,1)
trace22= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,22].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(207,197,187)",width=2))  ##55DDDD
fig.add_trace(trace22,1,1)
trace23= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,23].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(245,241,232)",width=2))  ##55DDDD
fig.add_trace(trace23,1,1)
trace24= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,24].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(196,218,230)",width=2))  ##55DDDD
fig.add_trace(trace24,1,1)
trace25= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,25].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(175,199,191)",width=2))  ##55DDDD
fig.add_trace(trace25,1,1)
trace26= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,26].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#D8BFD8",width=2))  ##55DDDD
fig.add_trace(trace26,1,1)
trace27= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,27].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CDCDB4",width=2))  ##55DDDD
fig.add_trace(trace27,1,1)
trace28= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,28].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CDC673",width=2))  ##55DDDD
fig.add_trace(trace28,1,1)
trace29= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,29].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CD8C95",width=2))  ##55DDDD
fig.add_trace(trace29,1,1)
trace30= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,30].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#B2DFEE",width=2))  ##55DDDD
fig.add_trace(trace30,1,1)

trace31= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,31].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#9FB6CD",width=2))  ##55DDDD
fig.add_trace(trace31,1,1)
trace32= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,32].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#96CDCD",width=2))  ##55DDDD
fig.add_trace(trace32,1,1)
trace33= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,33].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#8FBC8F",width=2))  ##55DDDD
fig.add_trace(trace33,1,1)
trace34= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,34].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#FFB5C5",width=2))  ##55DDDD
fig.add_trace(trace34,1,1)
trace35= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,35].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#E6E6FA",width=2))  ##55DDDD
fig.add_trace(trace35,1,1)
trace36= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,36].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CAE1FF",width=2))  ##55DDDD
fig.add_trace(trace36,1,1)
trace37= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,37].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CDC1C5",width=2))  ##55DDDD
fig.add_trace(trace37,1,1)
trace38= Scatter(x=np.squeeze(data0['subfig1_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig1_y'][:,38].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#C9C9C9",width=2))  ##55DDDD
fig.add_trace(trace38,1,1)

trace0= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,0].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#ADD8E6",width=2))  ##55DDDD
fig.add_trace(trace0,1,2)
trace1= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,1].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(240,235,229)",width=2))  ##55DDDD
fig.add_trace(trace1,1,2)
trace2= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,2].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(202,195,187)",width=2))  ##55DDDD
fig.add_trace(trace2,1,2)
trace3= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,3].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(216,202,175)",width=2))  ##55DDDD
fig.add_trace(trace3,1,2)
trace4= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,4].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(226,165,173)",width=2))  ##55DDDD
fig.add_trace(trace4,1,2)
trace5= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,5].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(246,246,246)",width=2))  ##55DDDD
fig.add_trace(trace5,1,2)
trace6= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,6].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(181,199,201)",width=2))  ##55DDDD
fig.add_trace(trace6,1,2)
trace7= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,7].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(201,192,181)",width=2))  ##55DDDD
fig.add_trace(trace7,1,2)
trace8= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,8].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#eee5f8",width=2))  ##55DDDD
fig.add_trace(trace8,1,2)
trace9= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,9].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(226,165,173)",width=2))  ##55DDDD
fig.add_trace(trace9,1,2)
trace10= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,10].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(175,199,191)",width=2))  ##55DDDD
fig.add_trace(trace10,1,2)

trace11= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,11].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(199,207,192)",width=2))  ##55DDDD
fig.add_trace(trace11,1,2)
trace12= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,12].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(221,214,202)",width=2))  ##55DDDD
fig.add_trace(trace12,1,2)
trace13= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,13].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(238,223,218)",width=2))  ##55DDDD
fig.add_trace(trace13,1,2)
trace14= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,14].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(234,208,209)",width=2))  ##55DDDD
fig.add_trace(trace14,1,2)
trace15= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,15].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(240,235,229)",width=2))  ##55DDDD
fig.add_trace(trace15,1,2)
trace16= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,16].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(224,205,207)",width=2))  ##55DDDD
fig.add_trace(trace16,1,2)
trace17= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,17].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(211,212,204)",width=2))  ##55DDDD
fig.add_trace(trace17,1,2)
trace18= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,18].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(223,214,215)",width=2))  ##55DDDD
fig.add_trace(trace18,1,2)
trace19= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,19].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(193,203,215)",width=2))  ##55DDDD
fig.add_trace(trace19,1,2)
trace20= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,10].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(137,114,108)",width=2))  ##55DDDD
fig.add_trace(trace20,1,2)


trace21= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,21].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(172,155,145)",width=2))  ##55DDDD
fig.add_trace(trace21,1,2)
trace22= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,22].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(207,197,187)",width=2))  ##55DDDD
fig.add_trace(trace22,1,2)
trace23= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,23].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(245,241,232)",width=2))  ##55DDDD
fig.add_trace(trace23,1,2)
trace24= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,24].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(196,218,230)",width=2))  ##55DDDD
fig.add_trace(trace24,1,2)
trace25= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,25].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="rgb(175,199,191)",width=2))  ##55DDDD
fig.add_trace(trace25,1,2)
trace26= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,26].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#D8BFD8",width=2))  ##55DDDD
fig.add_trace(trace26,1,2)
trace27= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,27].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CDCDB4",width=2))  ##55DDDD
fig.add_trace(trace27,1,2)
trace28= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,28].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CDC673",width=2))  ##55DDDD
fig.add_trace(trace28,1,2)
trace29= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,29].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CD8C95",width=2))  ##55DDDD
fig.add_trace(trace29,1,2)
trace30= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,30].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#B2DFEE",width=2))  ##55DDDD
fig.add_trace(trace30,1,2)

trace31= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,31].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#9FB6CD",width=2))  ##55DDDD
fig.add_trace(trace31,1,2)
trace32= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,32].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#96CDCD",width=2))  ##55DDDD
fig.add_trace(trace32,1,2)
trace33= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,33].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#8FBC8F",width=2))  ##55DDDD
fig.add_trace(trace33,1,2)
trace34= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,34].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#FFB5C5",width=2))  ##55DDDD
fig.add_trace(trace34,1,2)
trace35= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,35].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#E6E6FA",width=2))  ##55DDDD
fig.add_trace(trace35,1,2)
trace36= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,36].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CAE1FF",width=2))  ##55DDDD
fig.add_trace(trace36,1,2)
trace37= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,37].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#CDC1C5",width=2))  ##55DDDD
fig.add_trace(trace37,1,2)
trace38= Scatter(x=np.squeeze(data0['subfig2_x'].tolist(), axis=None),
                    y=np.squeeze(data0['subfig2_y'][:,38].tolist(), axis=None),
                    mode='lines',
                    line=dict(color="#C9C9C9",width=2))  ##55DDDD
fig.add_trace(trace38,1,2)

fig["layout"].update(
    height=670 ,width = 1400,

    showlegend=False,

    xaxis= dict(
        linecolor='black', # 将颜色设定为黑色
        mirror=True,
        title="Time (s)",
        range=[0,0.3],
    ),
    xaxis2= dict(
        linecolor='black', # 将颜色设定为黑色
        mirror=True,
        title="Time (s)",

    ),
    yaxis= dict(
        linecolor='black',
        mirror=True,
        title="Amplitude"
    ),
yaxis2= dict(
        linecolor='black',
        mirror=True,
        title="Amplitude"
    ),
    font=dict(
        family="Time New Roman",  # 所有标题文字的字体
        size = 29 , # 所有标题文字的大小
    )
)
fig["layout"]["template"] = "simple_white"
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
html_path = '../htmls/User3.html'
fig.write_image('../images/User3.eps')
pyplot(fig,filename=html_path)