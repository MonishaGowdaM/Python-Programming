print('Enter a string:')
str = input()
i = 0
new_str = ' '
while (i <= len(str) - 1):
    data = str[i]
    ascii = ord(data)
    if (ascii >= 65 and ascii <= 90):
        newascii = ascii + 32
        convchar = chr(newascii)
        new_str = new_str + convchar
    else:
        newascii = ascii - 32
        convchar = chr(newascii)
        new_str = new_str + convchar
    i = i + 1
print(new_str)