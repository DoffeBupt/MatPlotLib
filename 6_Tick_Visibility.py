# 本节主要讲述把ticks（坐标轴的标签）的一些参数进行设置

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1*x

plt.figure()
# 画线，其中zorder为z轴方向的排序，相当于谁在上边
# 数字大的在上边，从1开始数
plt.plot(x, y, linewidth=10, zorder=1)      # set zorder for ordering the plot in plt 2.0.2 or higher
plt.ylim(-2, 2)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 相当于把x，y内部的所有的ticklable全部取出来了
for label in ax.get_xticklabels() + ax.get_yticklabels():
    # 把字号变大
    label.set_fontsize(12)
    # set zorder for ordering the plot in plt 2.0.2 or higher
    # 把背景颜色更改一些，bbox即文字后边的那个小框的背景色
    label.set_bbox(dict(facecolor='white',# 背景色
                        edgecolor='k', # 边缘色
                        alpha=0.8,        # 不透明度，在其他地方如划线也可以有
                        zorder=2))        # 相当于在上边
plt.show()