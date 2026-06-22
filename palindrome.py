class Palindrome:
    def ispalindrome(self, x: int) -> int:
        original = x 
        rev = 0
        while x > 0:
            rem = x % 10
            rev = (rev * 10) + rem
            x //= 10
        return original == rev
p1 = Palindrome()
num = int(input('Enter a number'))
print(p1.ispalindrome(num))