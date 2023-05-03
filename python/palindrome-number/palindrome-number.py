class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x)[::-1]==str(x)
    

    # Solution without using strings

    def isPalindrome_ver_2(self, x: int) -> bool:
        if x < 0:
            return False
        rev = 0
        orig = x
        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev == orig