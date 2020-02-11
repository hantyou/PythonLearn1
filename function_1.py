# 写函数（类似的还有对象和模块）
def func1():
    print('Hello, Jade~')


def func2(a):
    """这是函数文档：不会被打印。"""
    print('传递进来的' + str(a) + '是这个函数的参数')
    if a == 1:
        print('num=1')
    elif a == 2:
        print('num=2')
    else:
        print('num=other')


def SaySome(name, word):
    print(name + '->' + word)


def Collect(*par1):
    print('参数的长度是：', len(par1))
    print('第二个参数是:', par1[1])


def FuncBack():
    return [1, 2, 3, 'Daniel']


def func3(a, b):
    global gm
    c = a + b
    # print('m='+str(m))
    m = 50
    gm = m
    print('修改后的m值为', m)
    return c


func1()
func2(3)
print(func2.__doc__)
print.__doc__
m = 1
gm = 1
# 关键字调用
SaySome('Daniel', 'Jade')
SaySome('Jade', 'Daniel')
SaySome(name='Daniel', word='Jade')
# 收集参数
Collect(1, 'Daniel', 2)
# 函数多个返回值
print(FuncBack())
# 变量的作用域
c_out = func3(1, 2)
print('c_out=' + str(c_out))
print('修改后的m值在外面为', m)
print('修改后的gm值在外面为', gm)


# 闭包一种编程范式
def fun4(a):
    def fun5(b):
        return a - b

    return fun5


print(fun4(3)(5))
print(fun4(5)(3))


def fun6():
    a = 5

    def fun7():
        nonlocal a
        a *= a
        return a

    return fun7()


print(fun6())
