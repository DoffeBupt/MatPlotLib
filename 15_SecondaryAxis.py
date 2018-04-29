# 本节主要讲了如何共享一个X轴的情况下放两个Y轴

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 *y1

# 右边是生成对象,左边是接收传出的参数
fig = plt.figure()
ax1 = plt.subplot() # 传出了fig,和ax1坐标轴
## 原来的代码 fig, ax1 = plt.subplots(),这个东西默认传出两个参数,一个图,一个ax1
ax2 = ax1.twinx()    # twinx,x轴不动,做ax1的镜像,并且印到ax1上
ax1.plot(x, y1, 'g-') # ax1线的green
ax2.plot(x, y2, 'b-') # ax2线的blue

ax1.set_xlabel('X data')
ax1.set_ylabel('Y1 data', color='g')
ax2.set_ylabel('Y2 data', color='b')

plt.show()