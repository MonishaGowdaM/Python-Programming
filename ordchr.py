m = input('Enter a string:')
result = " "

for ch in m:
    if ord(ch) >= 65 and ord(ch) <= 90:
        result += chr(ord(ch) + 32)
    if ord(ch) >= 97 and ord(ch) <= 122:
        result += chr(ord(ch) - 32)
    else:
        result += ch
    print(result)