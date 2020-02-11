# 递归算法
def factorial(a):
    if a > 1:
        b = a * factorial(a - 1)
    elif a < 1:
        return 1
    else:
        b = a * 1
    return b


print(list(map(factorial, range(10))))
