def factors(n, i, countfact):
    if i > n:
        return countfact
    if n % i == 0:
        countfact += 1
        print(i,end = ' ')
    return factors(n,i+1,countfact)
n = int(input('Enter a number:'))
count = factors(n,1,0)
print(f'\n The count of factors is {count}')