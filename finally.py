def fun1():
    print('fun1 conneced to DB')
    try:
        fun2()
    except Exception as e:
        print('Error in fun1', e)
        raise e
    finally:
        print('Fun1 disconnected from DB')
def fun2():
    print('Fun2 connected to DB')
    try:
        res = 10 / 0
        print(res)
    except Exception as e:
        print('Error in fun2', e)
        raise e
    finally:
        print('Fun2 disconnected from DB')
print('Program Started')
try:
    fun1()
except Exception as e:
    print('Error in main program', e)
print('Program Ended')