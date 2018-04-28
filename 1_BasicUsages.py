import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50) # -1,1中均匀分布的50个点
y = 2*x +1
plt.plot(x,y) # 展示内容丢进去,注意传参顺序
plt.show() # 有这句话上一个图才会蹦出来

# 上方几个图标的用法
# 回到主界面,撤销,恢复,移动,放大,改一些参数,保存到png