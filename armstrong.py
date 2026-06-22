def countdigits(n):
    count = 0
    while n > 0:
        n = n//10
        count += 1
    return count
def armstrong(n):
    temp = n
    if n < 0:
        n = n * -1
    power = countdigits(n)
    armstrong = 0
    while n > 0:
        base = n % 10
        armstrong = armstrong + (base ** power)
        n = n//10
    if temp < 0:
        armstrong = armstrong * -1
    return temp == armstrong
n = int(input('Enter a number:'))
series = 1
while n > 0:
    flag = armstrong(series)
    if flag:
        print(series,end = ' ')
        n -= 1
    series += 1