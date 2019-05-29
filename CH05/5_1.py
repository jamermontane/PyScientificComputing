#-*-coding:GBK -*- 

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example.")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()

x = np.arange(0,5,0.1)
line, = plt.plot(x,x*x)# plot返回一个列表，通过line,获取其第一个元素
# 调用Line2D对象的set_*方法设置属性值
line.set_antialiased(False)
# 同时绘制sin和cos两条曲线，lines是一个有两个Line2D对象的列表
lines = plt.plot(x,np.sin(x),x,np.cos(x))
# 调用setp函数同时配置多个Line2D对象的多个属性值
plt.setp(lines,color="r",linewidth=2.0)

print(line.get_linewidth())
print(plt.getp(lines[0],"color"))
print(plt.getp(lines[1]))

f = plt.gcf()
print("f",f)