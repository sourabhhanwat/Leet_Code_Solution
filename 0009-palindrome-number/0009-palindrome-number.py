class Solution:
    def isPalindrome(self, x: int) -> bool:
        real, rev_x = x, 0

        while x > 0:
            digit = x % 10
            rev_x = rev_x * 10 + digit
            x = x//10

        return True if rev_x == real else False
