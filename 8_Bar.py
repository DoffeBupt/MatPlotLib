# 本节主要是如何展示柱状图

import matplotlib.pyplot as plt
import numpy as np

# 12个向上,12个向下的柱状图
n = 12
# X生成0,11的12个数字
X = np.arange(n)
# 均匀分布中随机采样,左闭右开
# 第三个数为size,代表个数,随机的个数
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,12)
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,12)
# 实际上X,Y都是数组

# 生成
plt.bar(X,+Y1,                  # 横纵坐标
        facecolor = '#9999ff', # 填充色
        edgecolor = 'white',   # 边框色
        )
plt.bar(X,-Y2,
        facecolor='#ff9999',
        edgecolor= 'white',
        )

# 加上上方标签

for x,y in zip(X,Y1): # x,y的二维循环
    plt.text(x+0.04,y+0.05, # text的位置的中心点!
             '%.2f' % y, # 对于传进来的数值保留两位小数,传入的是y
             # 下边两个参数是相对于上边设置的中心点的对齐方式!
             ha = 'center', # 横向对齐方式 horizontal alignment
             va = 'bottom' # 纵向的,那个点在那一坨字的底部
             )

for x,y in zip(X,Y2): # x,y的二维循环
    plt.text(x+0.04,-y-0.05, # text的位置
             '%.2f' % y, # 对于传进来的数值保留两位小数,传入的是y
             ha = 'center', # 横向对齐方式 horizontal alignment
             va = 'top' # 纵向的
             )

plt.xlim(-0.5,n)
plt.xticks(())
plt.ylim((-1.25,1.25))
plt.yticks(())

plt.show()