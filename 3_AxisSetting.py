import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x +1
y2 = x**2 # x平方

# 图片大小
# 2号图片,到下一个图片声明之前都是它的内容,它的属性设置
# **限制的是开始放了多大的图片** modified 4.29
plt.figure(num=2,figsize=(8,5))
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

# 限制横纵坐标轴的显示的取值范围
# **限制的是我都算了哪些数字,出去了的我就不算了** modified 4.29
# 大小仿佛是在限制一个显示的格子的比例
plt.xlim((-1,2))
plt.ylim((-2,3))
# 设置X,Y轴显示的标签
plt.xlabel("I am X")
plt.ylabel("I am Y")

# 单位小标,比如说:-1=不好,0=一般,1=好
# tick 单位小标,用来替换坐标轴标度
new_ticks = np.linspace(-1,2,5) # -1到2分成5个单位
print(new_ticks)
plt.xticks(new_ticks)
# 一一对应的将值对应设置为标签
# 数学字符,用$$括起来
# $$不能读取空格,要用转义字符转义
# 一般加r,正则表达式,$$之间即为选取的内容
# 好像不加也可以诶
# 转义符号好像可以把字母的希腊文转义成希腊字母
plt.yticks([-2,-1.8,-1,1.2,3],[r"$very\ bad$",r"$bad\alpha$",r"$normal$",r"$good$",r"$very\ good$"])

# gca = 'get current axis'
ax = plt.gca() # 拿到现有的坐标轴
ax.spines['right'].set_color('none')  # spines,脊梁,即图片的四个边框
ax.spines['top'].set_color('none')
# 设置哪个脊梁是x,y轴
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',-1))
# data,通过值来选择,确认位置,使得左轴在底轴的-1处为两轴交界
# 还有其他的参数

plt.show()