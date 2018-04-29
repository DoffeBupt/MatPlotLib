# 本节主要讲如何动画~

import numpy as np
from matplotlib import pyplot as plt

# 动画的模块
from matplotlib import animation

# 快速产生表格坐标轴
fig, ax = plt.subplots()


x = np.arange(0, 2*np.pi, 0.01)
# 小图内plot,前边的教程中也有在plt(fig)里plot的
# 画了个正弦
line, = ax.plot(x, np.sin(x)) # 画的线实际上是列表,所以弄个逗号比较好


def animate(i): # 传入的是第i帧
    # 然后每一次我更新ydata的数据
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line, # 返回我要画的线


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.sin(x)) # 设置起始值啦~
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
# blit=True dose not work on Mac, set blit=False
# interval= update frequency

# 动画定义,FunAni...是plt中其中一种动画方式
ani = animation.FuncAnimation(fig=fig,          # 传入的figure
                              func=animate,     # 功能是animate(前边自己定义的那个)
                              frames=100,       # 一次循环总共帧数
                              init_func=init,   # 最开始那帧是哪个(前边自己定义函数init)
                              interval=20,      # 刷新时间20ms
                              blit=False)       # False,全部更新,True是只更新变化的点

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
# anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()