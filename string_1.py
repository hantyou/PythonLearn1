str1 = 'Daniel Love Jade.'
print(str1[:3])
str2 = str1[:7]+'Really '+str1[7:]
print(str2)
str3 = str2.capitalize()
print(str3)
str4 = str2.center(40)
print(str4)
print(str4.count('a'))
str5 = 'Daniel\tLove\tJade'
print(str5)
str6 = str5.expandtabs()
print(str6)
print(str2.istitle())
print(str3.istitle())
str5 = str5.translate(str.maketrans('a', 'z'))
print(str5)
