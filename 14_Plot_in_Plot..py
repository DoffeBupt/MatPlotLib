# 本节主要在讲如何把小图丢到大的图里

import matplotlib.pyplot as plt

fig = plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# below are all percentage
# 设置上下左右边所处位置的百分比
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# 传进去,建立图1
ax1 = fig.add_axes([left, bottom, width, height])  # main axes
ax1.plot(x, y, 'r') # r-->线是红色的
ax1.set_xlabel('x') # x轴标签
ax1.set_ylabel('y') # y轴标签
ax1.set_title('title') # 标题

# 同理怼图二,定位好各个边所处的位置
ax2 = fig.add_axes([0.2, 0.6, 0.25, 0.25])  # inside axes
ax2.plot(y, x, 'b')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('title inside 1')

# 同理,图三,怼不同的小位置咯
# different method to add axes
####################################
plt.axes([0.6, 0.2, 0.25, 0.25])
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()