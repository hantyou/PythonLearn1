#
str1 = "{0} love {1}".format("Daniel", "Jade")
print(str1)
str2 = "{a} love {b}".format(a = "Daniel", b ="Jade")
print(str2)
str3 = "{{a}} love {{b}}".format(a = "Daniel", b ="Jade")
print(str3)
str4 = '{0:.2f}{1}'.format(27.658, 'GB')
print(str4)
str5 = "%c" % 97
print(str5)
str6 = "%c %c %c" % (97, 98, 99)
print(str6)
str7 = "%d + %d = %d" % (4, 5, 4+5)
print(str7)
str8 = "%o" % 10
print(str8)

