import numpy as np

'''Numpy配列の生成'''
a = np.array([1, 2, 3, 4, 5], dtype=np.float32) #Numpy配列の生成
b = np.zeros(10) #0が10個ある配列
c = np.ones(10) #1が10個ある配列
d = np.arange(10) #1ずつ増える配列
e = np.arange(10, step=2) #2ずつ増える配列
f = np.random.randn(10) #正規分布に従う乱数を10個生成
e = np.random.randint(10) #ある範囲の整数をランダムで生成(0からhigh-1が生成されう範囲)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(e)


'''Numpy配列の形状変換'''
a = np.arange(9)
print(a)

a = a.reshape(3, 3)
print(a)

print(a.shape) #形状(各次元の要素数)


'''Numpy配列の連結'''
a = np.arange(9)
print(a)

print(np.vstack([a, a])) #行追加
print(np.hstack([a, a])) #列追加


'''
        Numpy配列の計算
Numpyではブロードキャストの機能により、
for文などを使って要素を1つ1つ取り出さずに計算できます。
'''
a = np.arange(9).reshape(3, 3)
print(a)

print(a + a) #同次元の配列の加算
print(a - a) #同次元の配列の減算
print(a * a) #同次元の配列の乗算
print(a * 3) #配列の全ての要素を3倍
print(np.dot(a, a)) #内積


'''Numpy配列の集計'''
a = np.arange(9).reshape(3, 3)
print(a)
print(a.sum()) #合計(np.sum(a)でも同じ)
print(a.mean()) #平均(np.mean(a)でも同じ)
print(a.var()) #分散(np.var(a)でも同じ)
print(a.std()) #標準偏差(np.std(a)でも同じ)
print(np.mean(a, axis=1)) #行方向の平均
print(np.mean(a, axis=0)) #列方向の平均


'''Numpy配列のソート'''
a = np.arange(9)
print(a)
np.random.shuffle(a) #シャッフル
print(a)

print(np.sort(a)) #昇順にソート
print(np.sort(a)[::-1]) #降順にソート
