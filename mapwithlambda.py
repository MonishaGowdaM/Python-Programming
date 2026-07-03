l = []
i = 0
while i <= 4:
    print('Enter the value')
    data = int(input())
    l.insert(i,data)
    i = i + 1
print(l)
k = list(map(lambda data: (data + data), l))
print(k)