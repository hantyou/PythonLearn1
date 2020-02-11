# 斐波那契额数列
def fibonacci(x):
    if x == 1 or x == 2:
        return 1
    else:
        y = fibonacci(x - 2) + fibonacci(x - 1)
    return y


def fibonacci_a_range(x):
    y1 = 0
    y2 = 0
    for i in range(1, x):
        if i > 2:
            y = y1 + y2
            y2 = y1
            y1 = y
        else:
            y = fibonacci(i)
            y1 = y
            y2 = y1
        print(str(i) + ':\t' + str(y))


a = fibonacci(6)
print(a)
b = list(map(fibonacci, range(1, 10)))
print(b)
print(b)

fibonacci_a_range(100)
