class Solution:
    def isPalindrome(self, x: int)-> bool:
        org = x
        revx = 0
        while x > 0:
            last = x % 10
            revx = revx * 10 + last
            x = x // 10
        return org == revx
