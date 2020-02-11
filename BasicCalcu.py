range(5)
list(range(5))
for i in range(1, 10, 2):
    print(i)
# append, extend, insert
member = ['Daniel', 'Jade', [1, 2, 3], ]
print(member)
newS = [member, 'test']
print(newS)
newS.append('test2')
print(newS)
newS.insert(0, 'test3')
A = newS[:]  # 这是直接复制
B = newS  # 这是指针
print("newS=")
print(newS)
print(len(newS))
del newS[1]
print(newS)
newS.pop()
print(newS)
print(A[:])
print(B[:])
A *= 2
print(A)
print('Daniel' in A[1])
print(A.count('test3'))
print(A.index('test3',0,1))