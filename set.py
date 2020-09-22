# set

#a = set([5,4,8,5])
# a = {5, 4, 8, 5}  # 8,4,5 同じものは区別されない
# print(a)
# print(5 in a)  # True
# print(len(a))  # 3

a = {1, 2, 4}
b = {2, 4, 5, 6}

print(a | b)  # 和集合
print(a & b)  # 積集合
print(b - a)  # bにあってaにないもの
