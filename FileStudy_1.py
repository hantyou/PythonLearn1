# 首先：这一行是git的一个测试，忽略即可
# 输入-》处理-》输出
"""
    ========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
    ========= ===============================================================
"""
file = open("Filetest.txt", 'r')
print(file)
print(file.read(6))  # 里面是字符数而不是字节数
print(file.tell())
file.seek(4, 0)
str1 = file.read(4)
print(str1)
file.seek(0, 0)
for each_line in file:
    print(each_line)
file.close()
file = open("Filetest.txt", 'a')
file.seek(0, 2)
file.write('Append\n')
file.seek(0, 0)
file.close()
file = open("Filetest.txt", 'r')
for each_line in file:
    print(each_line)
# print(file.read(6))


file.close()
