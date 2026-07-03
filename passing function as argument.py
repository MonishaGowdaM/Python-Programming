def fun1():
    print('Inside Function1')
def fun2(a,b):
    c = a + b
    print('The sum is:', c)
def display(ptr1, ptr2):
    ptr1()
    a = 10
    b = 20
    ptr2(a,b)
fun1()
fun2(20,40)
ptr3 = fun1
ptr4 = fun2
x = 7
y = 6
ptr3()
ptr4(x,y)
display(ptr3,ptr4)
    