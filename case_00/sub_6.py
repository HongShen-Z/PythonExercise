'''
题目：斐波那契数列。
'''

m, n = 0, 1
li = []
x = int(input('请输入数列个数：'))
for i in range(x):
    li.append(m)
    m, n = n, m + n
print(li)
