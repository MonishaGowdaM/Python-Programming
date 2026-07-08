# def fun1():
#     a = 10
#     print('from fun1 a:',a)
#     def fun2():
#         b = 20
#         print('From fun2 b:',b)
#         print('From fun1 a:',a)
#     fun2()
#     print('from fun1 a:',a)
# fun1()

# def fun1():
#     a = 999
#     print('From fun1 a:',a)
#     def fun2():
#         a = 10
#         b = 20
#         print('From fun2 b:',b)
#         print('From fun1 a:',a)
#     fun2()
#     print('From fun1 a:',a)
# fun1()

# def fun1():
#     a = 999
#     print('From fun1 a:',a)
#     def fun2():
#         nonlocal a
#         a = 10
#         b = 20
#         print('From fun2 b:',b)
#         print('From fun1 a:',a)
#     fun2()
#     print('From fun1 a:',a)
# fun1()

# a = 10 
# def fun1():
#     global a
#     a = 100
#     b = 20
#     print(a)
#     print(b)
#     def fun2():
#         global a 
#         nonlocal b
#         a = 10000
#         b = 200
#         c = 30
#         print(a)
#         print(b)
#         print(c)
#     fun2()
#     print(a)
# fun1()

# class Demo:
#     x = 11

#     def __init__(self):
#         self.y = 22
#         self.z = 33

#     def disp(self):
#         print(self.y)
#         print(self.z)
#         a = 10
#         b = 20
#         c = a + b
#         print(c)

# d = Demo()
# print(Demo.x)
# d.disp()

def fun(sina,sinb,cosa,cosb):
    x = (sina * cosb) + (cosa * sinb)
    return x
res = fun(10, 20, 30, 40)
print(res)