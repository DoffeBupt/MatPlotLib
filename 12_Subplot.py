# 本节讲述如何一张图画多个表格

import matplotlib.pyplot as plt

# example 1:
###############################
# figure:几个窗口
plt.figure(figsize=(6, 4))
# plt.subplot(n_rows, n_cols, plot_num)

# 创建小图
# 分成了2行2列,并且在第一个位置画东西~
plt.subplot(2, 2, 1)
# plot默认直接连上线
plt.plot([0, 1], [0, 1])

# 222=2,2,2
plt.subplot(222)
plt.plot([0, 1], [0, 2])

plt.subplot(223)
plt.plot([0, 1], [0, 3])

plt.subplot(224)
plt.plot([0, 1], [0, 4])

# 自动的紧凑显示图片
plt.tight_layout()

# example 2:
###############################
# 第二个figure-->两个窗口
plt.figure(figsize=(6, 4))
# plt.subplot(n_rows, n_cols, plot_num)
# 强行分成两行一列,我走第一个
plt.subplot(2, 1, 1)
# figure splits into 2 rows, 1 col, plot to the 1st sub-fig
plt.plot([0, 1], [0, 1])

## 下边是画剩下的
plt.subplot(234)
# figure splits into 2 rows, 3 col, plot to the 4th sub-fig
plt.plot([0, 1], [0, 2])

plt.subplot(235)
# figure splits into 2 rows, 3 col, plot to the 5th sub-fig
plt.plot([0, 1], [0, 3])

plt.subplot(236)
# figure splits into 2 rows, 3 col, plot to the 6th sub-fig
plt.plot([0, 1], [0, 4])


plt.tight_layout()
plt.show()