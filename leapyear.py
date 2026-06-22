def leapyear(year):
    if year <= 0:
        return False

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    return False


start = int(input("Enter a start year: "))
end = int(input("Enter an end year: "))

if start > end:
    print("Give proper range")
else:
    print("Leap years:")
    for year in range(start, end + 1):
        if leapyear(year):
            print(year, end=" ")

    print("\nNot leap years:")
    for year in range(start, end + 1):
        if not leapyear(year):
            print(year, end=" ")