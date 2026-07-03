# Composition example in Python

class OS:   #composed object
    def __init__(self):
        self.status = True
        print('OS is ready')

    def get_os(self):
        print('OS is still executing')


class Mobile:   #main object
    def __init__(self, name):
        self.mname = name
        self.os = OS()    # Composition
        print('Mobile is ready')
        print('with OS installed')


m = Mobile('MyPhone')
print(m.mname)
print(m.os.status)
m.os.get_os()

del m

print('Mobile is deleted')

# print(m.mname)      # This will raise an error since m is deleted
# print(m.os.status)  # This will also raise an error since m is deleted
# m.os.get_os()       # This will also raise an error since m is deleted