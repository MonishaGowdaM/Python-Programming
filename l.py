num = int(input('Enter a number'))
if num >= 0:
    if num % 2 == 0:
        print(num,'It is positive even number')
    else:
        print(num,'It is a negative odd number')
elif num < 0:
    if num % 2 == 0:
        print(num,'It is a positive even number')
    else:
        print(num,'It is a negative odd number')
    