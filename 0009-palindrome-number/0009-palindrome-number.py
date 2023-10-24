class Solution:
    def isPalindrome(self, x):

        s=str(x)
        r=s[::-1]
        if s==r:
            return True
        else:
            return False

        