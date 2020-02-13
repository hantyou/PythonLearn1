# Object Oriented Programming
import datetime

# 一个类对象，还不能称作对象
"""========================"""


class Human(object):
    def __init__(self):
        self.name = input("请输入学生姓名")
        self.gender = input("请输入学生性别")
        self.Byear = int(input("请输入学生出生年份"))
        self.Bmonth = int(input("请输入学生出生月份"))
        self.Bday = int(input("请输入学生出生日"))

    def calcYear(self, birth):
        nowy = datetime.date.today()
        # print(nowy)
        y = nowy.year
        m = nowy.month
        d = nowy.day
        age = y - birth[0]
        if birth[1] < m:
            age += 1
        elif birth[1] > m:
            age -= 1
        else:
            if birth[2] < d:
                age += 1
            if birth[2] >= d:
                age -= 1
        return age

    def HumanInfo(self):
        print('姓名：%s' % self.name)
        print('性别：%s' % self.gender)
        StrBirthday = str(self.Byear) + '.' + str(self.Bmonth) + '.' + str(self.Bday)
        print('出生日期：' + StrBirthday)
        birthday = [self.Byear, self.Bmonth, self.Bday]
        age = self.calcYear(birthday)
        print('年龄：%d' % age)
        print('=' * 10)


"""========================"""
# 下面每次给SL append一次，就产生了一个实例
SL = []
for i in range(3):
    SL.append(Human())
    SL[i].HumanInfo()
