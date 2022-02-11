import matplotlib
import numpy as np
import matplotlib.pyplot as plt

fig=plt.figure('The Spread of covid-19 per county')
rect=fig.patch
rect=rect.set_color('grey')# try to set both the edge and face color

chart=fig.add_subplot(1,1,1, projection='3d')
x=[1,2,3,4,5,6,7,8,9,10,13]# 
y=[2,3,4,6,1,9,2,7,15,18,8]
z=[0,0,0,0,0,0,0,0,0,0,0]#this code show from what level will the bars start from

dx=np.ones(11)# generates an array of 11 ones, can aslso be coded asdx=[1,1,1,1,1,1,1,1,1,1]
dy=np.ones(11)# this generates the width size of the bars
dz=[1,2,3,4,5,6,7,8,9,10,11]#this is the various heights of the ten block

chart.set_xlabel('People-X-axis',color='blue')
chart.set_ylabel('Counties-Y-axis',color='blue')
chart.set_zlabel('Rate of Infection-Z-axis',color='blue')
chart.set_title('Covid-19-Kenya',color='red')
labels=['Nyeri','Muranga','Kirinyaga','Kitui','Machakose','Likipia','Nairobi','Kisumu','Homabay','Kilifi','Mombasa']
colors=['yellow','orange','cyan','magenta','red','cyan','black','orange','green']

#chart.bar3d(x,y,z,dx,dy,dz,color='magenta')
chart.bar(x,y,z,dx,dy,dz,color='cyan')
#chart.bar_label(labels=labels,colors=colors)
#chart.bar3d(xyzcolors=colors,labels=labels)

plt.show()#display the graph
