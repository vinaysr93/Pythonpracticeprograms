#To check if an integer is a palindrome

class Solution:
    def isPalindrome(self, x):

        s1=str(x)


        if s1[::-1]==s1:
            return True
        else:
            return False

q=Solution()
q1=q.isPalindrome(121)
print(q1)