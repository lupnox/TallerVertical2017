import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

import plotly
import plotly.plotly as py
import plotly.graph_objs as go

plotly.tools.set_credentials_file(username='lupnox', api_key='x62h72KzUDVCWu6uzKGY')
plot_url='https://plot.ly/~lupnox/5/datosdeimagen/'

col=[]
for file in os.listdir("C:\Users\user\Dropbox\DropsyncFiles"):
	if file.startswith("Muestra"):
		col.append(os.path.join("C:\Users\user\Dropbox\DropsyncFiles",file))

img = cv2.imread(col[-1],0)

histr = cv2.calcHist([img],[0],None,[256],[0,256])

x=[]
for i,col in enumerate(histr):
	x.extend(histr[i])
List = open("C:\Users\user\Dropbox\DropsyncFiles\Location_log.txt").readlines()
title=List[-1]
title.replace("\n","")

data=[go.Histogram(x=x)]

layout = go.Layout(
    title=title
)
fig = go.Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename='Turbidez del sensor1')
