class Solution:
    def reverse(self, x:int)-> int:
        temp = x
        rev = 0
        if x < 0:
            x *= -1
        while x > 0:
            rem = x % 10
            rev = (rev * 10) + rem
            x = x//10
        if temp < 0:
            rev *= -1
        if rev < -(2**31) or rev > (2**31) -1:
            return 0
        return rev
s1 = Solution()
num = int(input('Enter a number:'))
print(s1.reverse(num))