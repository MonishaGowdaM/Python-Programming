def countdigits(n):
    if n < 0:
        n = n * -1
    count = 0
    while n > 0:
        n = n//10
        count += 1
    return count
n = int(input('Enter a value:'))
digits = countdigits(n)
print(f'The digits in {n} is:',digits)