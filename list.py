a = []
i = 0
while True:
    data = int(input('Enter the value:'))
    a.insert(i, data)
    i += 1
    print('Do you want to continue?')
    print('Press 1: Yes')
    print('Press 2: Yes')
    print('Press 3: No')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        continue
    if choice == 3:
        break
print(a)