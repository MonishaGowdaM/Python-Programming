try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    result = a / b

    print("Result:", result)

except ValueError as e:
    print("It is a ValueError")

except ZeroDivisionError as e:
    print("It is a ZeroDivisionError")

except Exception as e:
    print("It is some other error")