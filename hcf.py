x = int(input('Enter a number:'))
y = int(input('Enter a another number:'))
lower = x
if y < x:
    lower = y
HCF = 1
for i in range (2, lower + 1):
    if x % i == 0 and y % i == 0:
        HCF = i
print(f'The HCF of {x} and {y} is: {HCF}')