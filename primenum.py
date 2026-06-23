def isPrime(num):
    i = 1
    count = 0
    while i * i <= num:
        if num % i == 0:
            count += 1
        if i != num//i:
            count += 1
        i += 1
    return count == 2
num = int(input('Enter a number:'))
flag = isPrime(num)
if flag:
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')