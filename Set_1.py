# 集合
num = {}
print('num is a', type(num))
num2 = {1, 2, 3, 4, 5, 6}
print('num2 is a', type(num2))
num2 = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1}
print(num2)
# 集合元素不重复，集合不可索引
# 还可以使用set()工厂函数创建集合
set1 = set([1, 2, 3, 4, 5, 3, 4, 5])
print(set1)
num1 = [1, 2, 3, 4, 5, 3, 2, 8, 9, 0, 4, 1]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)
print(temp)
temp2 = list(set(num1))  # 使用这个方法0会被自动放到前面
print(temp2)
# 判断集合中是否包含某个值
print(1 in num1)
# 增删集合中元素
num2 = set(num1)
num2.add(22)
print(num2)
num2.remove(22)
print(num2)
# 不可变集合frozen set
num3 = frozenset([1, 2, 3, 4, 5])
print(num3)
# num3.add()会报错
