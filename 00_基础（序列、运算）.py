# 03序列练习

s1 = (2, 1.3, 'love', 5.6, 9, 12, False)         # s1是一个tuple

s2 = [True, 5, 'smile']                          # s2是一个list

s3 = [1,[3,4,5]]

print(s1,type(s1))

print(s2,type(s2))

print(s1[0])

print(s2[2])

print(s3[1][2])

s2[1] = 3.0

print(s2)

print('---------')

print(s1[:5])             # 从开始到下标4 （下标5的元素 不包括在内）

print(s1[2:])             # 从下标2到最后

print(s1[0:5:2])          # 从下标0到下标4 (下标5不包括在内)，每隔2取一个元素 （下标为0，2，4的元素）

print(s1[2:0:-1])

print(s1[-1])             # 序列最后一个元素

print(s1[-3])

print(s1[0:-1])           #最后一个元素不会被引用（不包括上限元素本身）

str = 'abcdef'

print(str[2:4])

print('---------')

#04 运算

print(1+9)        # 加法

print(1.3-4)      # 减法

print(3*5)        # 乘法

print(4.5/1.5)    # 除法

print(3**2)       # 乘方

print(10%3)       # 求余数

print('---------')

print(5==6)               # =， 相等

print(8.0!=8.0)           # !=, 不等

print(3<3, 3<=3)          # <, 小于; <=, 小于等于

print(4>5, 4>=0)          # >, 大于; >=, 大于等于

print(5 in [1,3,5])       # 5是list [1,3,5]的一个元素

print('---------')

print(True and True, True and False)      # and, “与”运算， 两者都为真才是真

print(True or False)                      # or, "或"运算， 其中之一为真即为真

print(not True)                           # not, “非”运算， 取反