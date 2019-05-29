#-*-coding:GBK -*- 

import numpy as np
import matplotlib.pyplot as plt

for idx,color in enumerate("rgbyck"):
    plt.subplot(320+idx+1,axisbg=color)
plt.show()