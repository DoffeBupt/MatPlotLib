import numpy as np
import matplotlib.pyplot as plt
# 3D坐标轴的显示
from mpl_toolkits.mplot3d import Axes3D

# 定义一个图片的窗口,只是一个框框
fig = plt.figure()
# 在fig里加入一个3D坐标轴
ax = Axes3D(fig)
# X, Y value
# X,Y的设置
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
# 把X,Y mesh起来
# meshgrid,在另外一个轴的方向进行升维
# 这样子不至于最后出来是一条线
X, Y = np.meshgrid(X, Y)
# R用来计算高度值
R = np.sqrt(X ** 2 + Y ** 2)
# height value
Z = np.sin(R)

# 扔3D坐标轴的方式
# stride 中文: 步幅
ax.plot_surface(X, Y, Z,        # 三轴坐标
                rstride=1,      # 横纵的跨度值,值越小越密集
                cstride=1,      # 同一个格子里一般是一个颜色

                cmap=plt.get_cmap('rainbow'), # 颜色映射方式:z轴映射到彩虹
                )


"""
============= ================================================
        Argument      Description
        ============= ================================================
        *X*, *Y*, *Z* Data values as 2D arrays
        *rstride*     Array row stride (step size), defaults to 10
        *cstride*     Array column stride (step size), defaults to 10
        *color*       Color of the surface patches
        *cmap*        A colormap for the surface patches.
        *facecolors*  Face colors for the individual patches
        *norm*        An instance of Normalize to map values to colors
        *vmin*        Minimum value to map
        *vmax*        Maximum value to map
        *shade*       Whether to shade the facecolors
        ============= ================================================
"""

# I think this is different from plt12_contours
ax.contourf(X, Y, Z,
            zdir='z', # 沿Z轴往下做投影
            offset=-2, # 往下再放放,丢到z坐标平面上去
            cmap=plt.get_cmap('rainbow') # 颜色范围
            )

# 等高线千万不要忘了加上offset和zdir
C = ax.contour(X,Y,Z,
               10, # 等高黑线分为了几个部分,上下俩10尽量要对应
               zdir='z', # 这俩千万别忘了加
               offset= -2, # 同上
               colors='black', # 等高线设置为黑色
               linewidth=.5    # 宽度0.5
               )
# 不知道为啥clabel放不上去,有时间再看看啦
# plt.clabel(C,       # 画在等高线C上
#            inline=True, # 画在线里边
#            fontsize=10  #字体大小10
#            )

ax.contourf(X, Y, Z,
            zdir='x', # 沿Z轴往下做投影
            offset=-4, # 往下再放放,丢到z坐标平面上去
            cmap=plt.get_cmap('rainbow') # 颜色范围
            )
"""
==========  ================================================
        Argument    Description
        ==========  ================================================
        *X*, *Y*,   Data values as numpy.arrays
        *Z*
        *zdir*      The direction to use: x, y or z (default)
        *offset*    If specified plot a projection of the filled contour
                    on this position in plane normal to zdir
        ==========  ================================================
"""

## 这俩限制的是我都算了那些数
## 其他的可能是限制的是图片大小
ax.set_zlim(-2, 2) # z轴范围限制
ax.set_xlim(-4, 4)
plt.show()
