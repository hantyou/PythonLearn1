# Problem of Hanoi
x = [1, 2, 3, 4, 5, 6]
y = []
z = []


def hanoi(n, x, y, z):  # 将x上的n个盘子移动到z上
    if n == 1:
        print(x, '-->', z)
    else:
        hanoi(n - 1, x, z, y)  # 将前n-1个从x移动到y
        print(x, '-->', z)
        hanoi(n - 1, y, x, z)  # 将y上的n-1个盘子移动到z上


n = int(input('请输入汉诺塔层数：'))
hanoi(n, 'x', 'y', 'z')
