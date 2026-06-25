def fibonacci(pos):
    x = 0
    y = 1
    for i in range(pos):
        print(x, end = ' ')
        z = x + y
        x = y
        y = z
        pos += 1
pos = int(input('Enter the position of fibonacci series:'))
print('Fibonacci numbers are:')
fibonacci (pos)