#-*-coding:GBK -*- 

import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0.15,0.1,0.7,0.3])
line,=ax.plot([1,2,3],[1,2,1])
print(ax.lines)
print(line)