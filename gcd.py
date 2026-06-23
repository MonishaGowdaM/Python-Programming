def gcd ( a, b, c, HCF, lower):
    if c > lower:
        return HCF
    if a % c == 0 and b % c == 0:
        HCF = c
    return gcd (a, b, c+1, HCF, lower)
a = int(input('Enter first number:'))
b = int(input('Enter second number:'))
lower = a
if b < a:
    lower = b
HCF = gcd (a,b,1,1,lower)
print(f'The gcd of {a} and {b} is:{HCF}')