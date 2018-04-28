import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x +1
y2 = x**2 # x平方

plt.figure(num=3,figsize=(8,5))
# 第一张图,序号为3,大小为8,5
plt.plot(x,y1)
# 第一张图里边的参数

plt.figure(num=2,figsize=(4,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')
# 可以画多条线,此外,可以设置颜色,线宽度,类型(虚线)等参数
# 第二张图以及其内部的参数
# 两张图,是两个窗口

plt.show()

