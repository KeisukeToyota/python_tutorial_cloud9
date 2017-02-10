'''
変数や値を比較しTrueかFalseを返します。
'''

a = 2
b = 1
c = [1, 2, 3, 4, 5]

print(a == b) #aはbと等しい
print(a != b) #aはbと等しくない
print(a < b) #aはbより小さい
print(a <= b) #aはb以下
print(a > b) #aはbより大きい
print(a >= b) #aはb以上

print('-------')

print(a is b) #aはbと等しい
print(a is not b) #aはbと等しくない
print(a in c) #aはcに含まれる
print(a not in c) #aはcに含まれる
