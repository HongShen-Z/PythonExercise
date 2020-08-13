'''
题目：打印出所有的"水仙花数"
'''

arr = list()

for i in range(100, 1000):
    a = int(i / 100) % 10
    b = int(i / 10) % 10
    c = int(i / 1) % 10
    if i == a ** 3 + b ** 3 + c ** 3:
        arr.append(i)

print('水仙花数：' + str(arr))


# daff = []
# for i in range(100, 1000):
#     if i == (i//100)**3 + (i//10%10)**3 + (i%10)**3:
#         daff.append(i)
# print(daff)
