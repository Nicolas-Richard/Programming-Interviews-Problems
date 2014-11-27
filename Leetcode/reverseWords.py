#https://oj.leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        set=s.split()
        return ' '.join(set[::-1])    
        