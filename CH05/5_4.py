#-*-coding:GBK -*- 

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0.15,0.1,0.7,0.3])
line,=ax.plot([1,2,3],[1,2,1])
print(ax.lines)
print(line)

from matplotlib.lines import Line2D
import matplotlib
fig = plt.figure()
line1 = Line2D([0,1],[0,1],transform=fig.transFigure,figure=fig,color="r")
line2 = Line2D([0,1],[0,1],transform=fig.transFigure,figure=fig,color="g")
fig.lines.extend([line1,line2])
fig.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.patch.set_facecolor("green")

x,y = np.random.rand(2,100)
line,=ax.plot(x,y,"-",color="blue",linewidth=2)
print("line")
print("ax.lines",ax.lines)
ax = fig.add_subplot(111)
n,bins,rects=ax.hist(np.random.rand(1000),50,facecolor="blue")
print("rects",rects)
print("rects[0]",rects[0])
print("ax.patches[0]",ax.patches[0])

fig = plt.figure()
ax = fig.add_subplot(111)
rect = matplotlib.patches.Rectangle((1,1),width=5,height=12)
#print(rect.get_axes())
print(rect.get_transform())
print(ax.transData)


import pylab as pl

axis = pl.gca().xaxis
print(axis.get_ticklocs())
for label in axis.get_ticklabels():
    label.set_color("red")
    label.set_rotation(45)
    label.set_fontsize(16)
    
for line in axis.get_ticklines():
    line.set_color("green")
    line.set_markersize(25)
    line.set_markeredgewidth(3)


pl.plot([1,2,3],[4,5,6])
pl.show()


    

