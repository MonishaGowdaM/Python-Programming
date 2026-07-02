# str = ' '
# print('Original string:',str)
# str1 = str.lstrip()
# print('left stripped string:',str1)
# str2 = str.rstrip()
# print('right stripped string:',str2)
# str3 = str.strip()
# print('fully stripped string:',str3)

str = input('Enter a string:')
i = 0
new_str = ' '
while(i <= len(str)-1):
    data = str[i]
if (data == ' '):
    i += 1
else:
    new_str += data
    i += 1
print('String without spaces:', new_str)