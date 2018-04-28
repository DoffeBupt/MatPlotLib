# 本节主要讲述如何添加标注
# 一个是在曲线上添加,一个是在空白处添加

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x + 1

plt.figure(num=1, figsize=(8, 5),)
plt.plot(x, y,)

# 这一摊是去掉右上角
# 然后规定横纵坐标的起始值
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2*x0 + 1
# 用虚线画出(x0,0)到(x0,y0),k--=blacK以及虚线
plt.plot([x0, x0,], [0, y0,], 'k--', linewidth=2.5)
# scatter 主要用于展示散点,s=size,b=blue
plt.scatter([x0, ], [y0, ], s=50, color='b')


# method 1:
#####################
#
plt.annotate(r'$2x+1=%s$' % y0, # $$ 表示用的是正则式
             # %s 表示之后传入一个字符串
             # 后边 %y0 代表传入的字符串是 y0
             xy=(x0, y0),
             # xy从哪个点开始打印这个
             xycoords='data',
             # xy传入的那个x0，y0是以data的作为基准的
             xytext=(+30, -30),
             # 基于下边那个坐标进行30，,30的偏移
             textcoords='offset points',
             # 上边30-30是基于offset points的坐标的
             fontsize=16,
             # 字体大小
             arrowprops=dict(arrowstyle='->',
                             # 箭头的描述，风格是箭头
                             connectionstyle="arc3,rad=.2"))
                             # 链接线的相关参数
# method 2:
########################
plt.text(-3.7, 3, # text类型标注，开始位置-3.7，3
         r'$This\ is\ the\ some\ text. \mu\ \sigma_i\ \alpha_t$',
         # 文字，转义符，空格要加，希腊文要加
         # 反正加了正则式字体就蜜汁好看了...
         fontdict={'size': 16, 'color': 'r'})
         # 字体以及颜色

plt.show()