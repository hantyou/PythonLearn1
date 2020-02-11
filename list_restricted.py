# 元组
# 列表可以任意修改其中的元素，而元组不能随意插入或删除

# 创建一个元组
tuple=(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tuple[1])
print(tuple[:5])
temple1 = ( 1 )
print(type(temple1))
temple2 = 2, 3, 4
print(type(temple2))
print(temple2)
temple1 = 1,
print(type(temple1))
temple3 = 8 * (8, )
print(temple3)
# 如何往元组里增加元素（实际上是基于元组切片）
temp = ('Daniel', 'Jade', 'Chicken')
temp = temp[:1]+('Jack', )+temp[1:]
print(temp)
del temp
