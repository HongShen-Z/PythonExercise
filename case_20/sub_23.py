'''
题目：利用循环打印菱形
'''

SIZE = 5
SHOW = ' *'
HIDE = '  '

# 坐标系构建法
for y in range(SIZE - 1, -SIZE, -1):
    for x in range(-SIZE + 1, SIZE, 1):
        if (y > x - SIZE) and (y < x + SIZE) and \
                (y > -x - SIZE) and (y < -x + SIZE):
            print(SHOW, end='')
        else:
            print(HIDE, end='')
    print()


'''
size = 5
print()
for i in range(1, 2*size, 2):
    print((' *'*i).center(4*size))
for j in range(2*size-3, 0, -2):
    print((' *'*j).center(4*size))
'''
