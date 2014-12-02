# The linear time solution is to use a suffix tree : http://en.wikipedia.org/wiki/Suffix_tree
# Another solution is the Manacher's algo : http://en.wikipedia.org/wiki/Longest_palindromic_substring
# This is O(n^2) solution that I've optimized on the spot without too much thought.

# Doesn't pass the tests but works: https://oj.leetcode.com/problems/longest-palindromic-substring/

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        # O(n^3) because of the two for loops + it takes O(n) to compare the substrings together
        s = [l.lower() for l in s if l.isalnum()]
        longest=''
        
        for i in range(len(s)): # Two loops, this is essentially a bruteforce approach
            for j in range(i+1,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if j-i+1 > len(longest):
                        longest = ''.join(s[i:j+1])

        return longest
        
    def allPalindrome(self, s): # return all palindroms, used for debugging.
    
        s = [l.lower() for l in s if l.isalnum()]
        allPalindroms=[]
        
        for i in range(len(s)): # Two loops, this is essentially a bruteforce approach
            for j in range(i+1,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    allPalindroms.append(''.join(s[i:j+1]))
        return allPalindroms                         


s = Solution()        