# 本节主要讲述了如何绘制等高线图

import matplotlib.pyplot as plt
import numpy as np

# 计算高度值的函数
# 反正就是一个乱七八糟的函数
def f(x,y):
    # the height function
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
# 把X,Y绑定成为网格的输入值
X,Y = np.meshgrid(x, y)

# use plt.contourf to filling contours
# X, Y and value for (X,Y) point
# contour等高线,f-filling,填充颜色
plt.contourf(X, Y,    # mesh过后的x,y作为XY轴
             f(X, Y), # f的蜜汁映射高度函数作为Z轴
             10,       # 等高色分为了几个等级 10+2=12部分
             alpha=.75, # 不透明度
             cmap=plt.cm.hot # cmap,颜色映射表,z映射为不同的颜色,hot暖色
             )

# use plt.contour to add contour lines
# 画等高线的线
C = plt.contour(X, Y,
                f(X, Y),
                10, # 登高黑线分为了几个部分,上下俩10尽量要对应
                colors='black', # 等高线设置为黑色
                linewidth=.5    # 宽度0.5
                )
# adding label
# c-contour 等高线标签
plt.clabel(C,       # 画在等高线C上
           inline=True, # 画在线里边
           fontsize=10  #字体大小10
           )

# 去掉X,Y两轴上的文字
plt.xticks(())
plt.yticks(())
plt.show()
