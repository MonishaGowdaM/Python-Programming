str = input("Enter a string:")
i = 0
new_str = ' '
while i<= len(str) -1:
    data = str[i]
    ascii = ord(data)
    if(ascii >= 65 and ascii <= 90):
        newascii = ascii + 32
        convchar = chr(newascii)
        new_str = new_str + convchar
    i = i + 1
print('swapped case string is:',new_str)
print('Enter a string')
str = input()
str1 = str.lower()
print(str1)