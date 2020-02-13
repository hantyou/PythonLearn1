# try + else
try:
    print(int('12啊3'))
except ValueError as reason:
    print('有错误产生，原因是：' + str(reason))
else:
    print('无错误产生')
