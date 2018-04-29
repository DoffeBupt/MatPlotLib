# 本节主要讲述其他几种分格子的方法
# 第一种方法要算跨度
# 第二种方法直接坐标怼,不过要引入库
# 第三种方法不能调整大小,但是可以共享坐标轴(中间不会画个花花的十字)

import matplotlib.pyplot as plt
# 第二种方法的时候要用的
import matplotlib.gridspec as gridspec

# method 1: subplot2grid
# grid 单元的小格子
##########################
# 第一个窗口
plt.figure()

# 第一张子图
# 图片都从(0,0)开始计数
ax1 = plt.subplot2grid((3, 3), # 一共分成了3*3
                       (0, 0), # 从(0,0)作为起点
                       colspan=3 # 横跨度为3(与之对应,还有rowspan,纵跨度,默认都是1)
                       )  # stands for axes
ax1.plot([1, 2], [1, 2])
# 注意,这里不能单纯的走plt.xlable了,要指定到每个小图
# 并且,原来的plt.XXX现在统一改成 ax1.set_XXX
ax1.set_title('ax1_title')

# 第二三四五张子图
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax4.scatter([1, 2], [2, 2])
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')
ax5 = plt.subplot2grid((3, 3), (2, 1))

# 第二个窗口
# method 2: gridspec
#########################
plt.figure()
# 相当于定义了一个3*3的格子
gs = gridspec.GridSpec(3, 3)
# use index from 0
ax6 = plt.subplot(gs[0, :])     # 第0行,所有的列
ax7 = plt.subplot(gs[1, :2])    # 第一行,第二列(不含)之前
ax8 = plt.subplot(gs[1:, 2])    # 第一行(含)往后,第二列
ax9 = plt.subplot(gs[-1, 0])    # 从后往前数第一个那行,第0列
ax10 = plt.subplot(gs[-1, -2])  # 倒数第一行,从后往前数倒数第二列

# method 3: easy to define structure
# 这个可以共享,但是仿佛,不可以进行小图的大小操作
####################################
f, ((ax11, ax12),               # 第一行所有的axs
    (ax13, ax14)                # 第二行所有的axs
    ) = \
    plt.subplots(2, 2,          # 2*2
                 sharex=True,   # 共享X轴,直接在最边上画了
                 sharey=True    # 共享Y轴,在边上画就不会在中间插了
                 )
ax11.scatter([1,2], [1,2])      # 一个散点

plt.tight_layout()
plt.show()