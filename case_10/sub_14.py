'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''

arr = []
x = int(input('请输入一个正整数：'))
temp = x

pri = 2
while pri != (x + 1):
    if temp % pri == 0:
        arr.append(pri)
        temp /= pri
    else:
        pri += 1
exp = '*'.join(map(str, arr))
print('{}={}'.format(x, exp))
