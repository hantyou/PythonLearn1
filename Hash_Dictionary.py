# 字典
brand = ['Nike', 'Addidas', 'New Balance']
slogan = ['Just do it', 'Impossible is nothing', 'Not Known']
print('The slogan of Addidas is ' + '\'' + slogan[brand.index('Addidas')] + '\'')
# 创造和访问字典
dict1 = {'Nike': 'Just do it', 'Addidas': 'Impossible is nothing', 'New Balance': 'Not Known'}
# 冒号后是前面Key的Value
print('The slogan of Addidas is ' + '\'' + dict1['Addidas'] + '\'')
# 另一个例子
dict2 = {1: 'one', 2: 'two', 3: 'three'}
print(dict2)
dict3 = dict((('Daniel', 'ShenZhen'), ('Jade', 'TaiYuan'), ('XJTU', 'Xi\'An')))
print(dict3)
# 可以用下面这种方法直接向字典中添加
dict3['Jack'] = 'Not Known'
print(dict3)
# 当索引不好用时
# from keys
dict4 = {}
print(dict4)
print(dict4.fromkeys((1, 2, 3)))
print(dict4.fromkeys((1, 2, 3), 'numbers'))
print(dict4.fromkeys((1, 3), 'NaN'))  # 并不会直接修改1，3的值，而是新创建了一个字典
print(dict4.fromkeys(range(32), 'Thumb'))
dict5 = {}
dict5 = dict5.fromkeys(range(32), 'Thumb')
for eachKey in dict5.keys():
    print(eachKey)

for eachValue in dict5.values():
    print(eachValue)

for eachItem in dict5.items():
    print(eachItem)

print(dict5.get(32))
print(dict5.get(32, 'Nothing Found'))
print(dict5.get(31, 'Nothing Found'))
print(31 in dict5)
print(32 in dict5)
# 如何清空字典
dict5.clear()
print(dict5)
dict1.clear()
dict2.clear()
dict1 = {'a': 'A', 'b': 'B'}
dict2 = dict1
print(dict1)
print(dict2)
dict1 = {}  # 实际上dict1和dict2在之前都是指向同一个数据的，所以这里相当于将dict1重新指向，所以dict2依然指向原来的数据
print(dict1)
print(dict2)
dict1 = dict2
dict1.clear()  # 用clear才会真正清空数据
print(dict1)
print(dict2)
# copy
dict1 = {'a': 'A', 'b': 'B'}
dict2 = dict1.copy()  # 浅拷贝
dict3 = dict1  #
print('-----dict1~3-----')
print(dict1)
print(dict2)
print(dict3)
print('Their ID')
print(id(dict1))
print(id(dict2))
print(id(dict3))
dict1['c'] = 'C'
print(dict1)
print(dict2)
print(dict3)
dict2 = dict1.copy()
# pop
print(dict1.pop('a'))
print(dict1)
print(dict2)
print(dict3)
dict1 = dict2.copy()
print(dict1.popitem())  # popitem随机弹，字典没有顺序的概念
print(dict1)
# update
print('------------------------')
dict1 = dict2.copy()

dict1.update({'a': 'AA'})
print(dict1)
b = {'b': 'BB'}
dict1.update(b)
print(dict1)
# setdefault
dict1
