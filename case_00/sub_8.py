'''
题目：输出 9*9 乘法口诀表。
'''

for i in range(1, 10):
    for j in range(1, 10):
        temp = '{0}*{1}={2}'.format(i, j, i*j)
        print(temp, end='\t')
    print('\n')
