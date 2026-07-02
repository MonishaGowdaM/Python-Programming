# def printnum(n):
#     if n <= 0:
#         return
#     printnum(n-1)
#     print(n, end = ' ')
# n = int(input('Enter a number:'))
# printnum(n)

def printnum4(n):
    print(n)
    printnum3(n-1)
def printnum3(n):
    print(n)
    printnum2(n-1)
def printnum2(n):
    print(n)
    printnum1(n-1)
def printnum1(n):
    print(n)
printnum4(4)