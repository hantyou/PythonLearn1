# exception
l1 = ['Daniel']
assert (len(l1))
try:
    # int('abc')  # 这一句没有在except里面，所以会报红色错误
    file = open('Why I am a file.txt', 'w')
    file.write('I exissssssts.')
    sum = 1 + '1'  # 一个语句出现异常，剩下的语句不会执行，故后面的不报错
except OSError as reason:
    print('出错警告：文件出错OSError')
    print('原因是：' + str(reason))
except TypeError as reason:
    print('类型出错')
    print('原因是：' + str(reason))
except:  # 不建议使用
    print('出错了')
# try finally 语句
finally:
    file.close() # 这里跟小甲鱼的教程好像有差别，这里运行后，没有finally，文件也被修改了
