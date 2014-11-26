#https://oj.leetcode.com/problems/valid-palindrome/

# The point of this problem is to learn how to handle non alnum character
# Good overview of possible solution in Python : http://stackoverflow.com/questions/1276764/stripping-everything-but-alphanumeric-chars-from-a-string-in-python


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, x):
        y = [i.lower() for i in x if i.isalnum()]
        return y == y[::-1]
