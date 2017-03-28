'''
Pythonではインデントでブロックを作ります。
スペースとタブが混在したブロックを作るとエラーになるので気をつけて下さい。
'''


'''if文'''
a = 10
if(a < 10):
    print('aは10より小さい')
elif(a == 10):
    print('aは10と等しい')
else:
    print('aは10より大きい')

print('-------')


'''for文'''
a = [1, 2, 3, 4, 5]
for i in range(10):
    print(str(i)+'回目')

print('-------')

for i in a:
    print(i)

print('-------')


'''while文'''
a = 0
while(a < 10):
    print(str(a)+'回目')
    a = a + 1

#無限ループ
while(True):
    print('無限ループ')
