# Object Oriented Programming
import datetime


class Human(object):
    def __init__(self, name, gender, Byear, Bmonth, Bday):
        self.name = name
        self.gender = gender
        self.Byear = Byear
        self.Bmonth = Bmonth
        self.Bday = Bday

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
        print('='*10)


daniel = Human('Daniel', '男', 1999, 6, 11)
SL = []
SL.append(Human('Jade', '女', 2000, 6, 12))
SL.append(daniel)
for i in range(len(SL)):
    SL[i].HumanInfo()


