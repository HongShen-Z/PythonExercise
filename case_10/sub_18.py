'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
'''

a = int(input('input a: '))
n = int(input('input n: '))

x = 0  # 各项值
l = []  # 值集合

for i in range(n):
    x += a * (10 ** i)
    l.append(x)

exp = ' + '.join(map(str, l))
res = sum(l)

print('%s = %d' % (exp, res))


'''
a = input('Input a')
n = int(input('Input n'))
result = 0
exp = []

for i in range(1, n+1):
    result += int(a*i)
    exp.append(a*i)
exp = ' + '.join(exp)
print('{} = {}'.format(exp, result))
'''
