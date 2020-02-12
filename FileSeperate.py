# This is to seperate the dialog in the file.
file = open('Filetest.txt', 'r', encoding='UTF-8')
Users = []
print('Users is a ', type(Users))
for each_line in file:
    ReadL = each_line
    print(ReadL)
    if ReadL[:6] == '======':
        print('该段对话结束\n')
        for i in range(len(Users)):
            exec(Users[i] + ".write('======')")
            exec(Users[i] + ".write('''\\n''')")
    else:
        SpLine = ReadL.split(sep=':', maxsplit=2)
        print(SpLine)
        Flag_1 = SpLine[0] not in Users and SpLine[0] != '\n'
        if Flag_1:
            Users.append(SpLine[0])
            tempStr = SpLine[0] + '.txt'
            exec(SpLine[0] + "=open("'tempStr'",'w')")
            exec(SpLine[0] + ".write("'str(SpLine[1])'")")
            # exec(SpLine[0] + ".write('''\\n''')")
        else:
            if len(SpLine) > 1:
                exec(SpLine[0] + ".write("'str(SpLine[1])'")")
                # exec(SpLine[0] + ".write('''\\n''')")
print('Users include:', Users)
file.close()
