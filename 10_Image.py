import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379])\
    .reshape(3,3)
    #reshape成3*3的大小

"""
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
for the value of "origin"= ['upper', 'lower'], check this:
http://matplotlib.org/examples/pylab_examples/image_origin.html
"""
# 图片的输入
# 好像是默认最值点为黑白,然后在中间等分颜色
plt.imshow(a,                       # 传入的数组
           interpolation='nearest', # 在网站上有具体的,这个就是边界分明的
           cmap='bone',             # cmap=plt.cm.hot 也可以直接像这样子传入字符串
           origin='lower')          # 相对于upper,upper和上边那个一一对应

# 颜色标注
plt.colorbar(shrink=.92)            # shrink:压缩到了左边图片长度的90%

plt.xticks(())
plt.yticks(())
plt.show()