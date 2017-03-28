import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

'''sinカーブ'''
x = np.arange(-3, 3, 0.1) #-3から3まで、0.1刻みの数字の列
y = np.sin(x)
plt.plot(x, y)
# plt.show()


'''正規分布のヒストグラム'''
x = np.random.randn(1000) #正規分布に従う乱数を1000個生成
plt.hist(x, bins=50)
# plt.show()


'''シグモイド関数'''
x = np.arange(-5, 5, 0.1)
y = 1.0 / (1.0 + np.exp(-x)) #シグモイド関数
plt.plot(x, y)
# plt.show()
