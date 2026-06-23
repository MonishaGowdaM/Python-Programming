num = int(input('Enter a number:'))
i = 1
while i * i <= num:
    if num % i == 0:
        print(i, end=' ')
    if i != num//i:
        print(num//i, end=' ')
    i += 1