#-*-coding:GBK -*- 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


print(matplotlib.get_configdir())
print(matplotlib.matplotlib_fname())

import os
print(os.getcwd())

print(matplotlib.rc_params())

matplotlib.rcParams["lines.marker"]="o"
import pylab
pylab.plot([1,2,3])
pylab.show()