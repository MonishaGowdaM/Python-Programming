def factors (num, i, count, cycles):
    cycles += 1
    if i * i > num:
        return count, cycles
    if num % i == 0:
        print(i, end = ' ')
        count += 1
        if i != num //i:
            count += 1
            print(num // i, end=' ')
    return factors(num, i + 1, count, cycles)
num = int(input('Enter a number:'))
count, cycles = factors(num, 1, 0, 0)
print(f'\nThe count of factrors is: {count}')
print(f'\nThe count of cycles is: {cycles}')