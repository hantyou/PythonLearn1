# with 语句学习
"""
try:
    f = open('data.txt', 'r')
    for each_line in f:
        print(each_line)
except OSError as reason:
    print('Error reason:' + str(reason))
finally:
    f.close()
"""

# 改成with语句


"""
try:
    with open('data.txt', 'w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错了：' + str(reason))
"""
try:
    with open('data.txt', 'r') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错了：' + str(reason))
