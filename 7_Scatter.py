import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n) # 中位数为0，方差为1,生成n（1024）个
Y = np.random.normal(0,1,n) # 同上
T = np.arctan2(Y,X) # 用公式怼出颜色的值
# arctan2 相当于拓展值域到[-π,π],好像还是个二维的

# 生成散点图
plt.scatter(X,Y,
            s = 75, # 大小设置为75
            c = T, # 颜色设置为了T
            # 这里还有个colormap,是颜色的映射,这里采用了默认的
            alpha = 0.5, # 不透明度设置为0.5
            )
# plt.scatter(np.arange(5),np.arange(5)) # 一根线的散点

# 限制X,Y的范围
plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))

#
plt.xticks(()) # x轴的ticks设置为空
plt.yticks(()) # y的

plt.show()