# The linear time solution is to use a suffix tree : http://en.wikipedia.org/wiki/Suffix_tree
# Another solution is the Manacher's algo : http://en.wikipedia.org/wiki/Longest_palindromic_substring
# Good explanations on Leetcode blog : leetcode.com/2011/11/longest-palindromic-substring-part-i.html

# The only method that pass Leetcode tests is the one names longestPalindrome with the helper expandAroundCenter

class Solution:
    # @return a string

    def longestPalindrome(self,s):
        #Expanding around the centers => O(n^2) time and O(1) space
        n = len(s)
        longest = ''
        for i in range(0,n):
            if len(self.expandAroundCenter(s,i,i)) > len(longest):
                longest = self.expandAroundCenter(s,i,i)
            if len(self.expandAroundCenter(s,i,i+1)) > len(longest):
                longest = self.expandAroundCenter(s,i,i+1)                
        return longest


    def expandAroundCenter(self,s,c1,c2):
        l = c1
        r = c2
        n = len(s)
        while (l>=0 and r<=n-1 and s[l] == s[r]):
            l -= 1
            r += 1
        return s[l+1:r]    



    def longestPalindrome_DP(self,s):
        # Dynamic programming solution that require O(n^2) space and time
        # You'll get memory exceeded error on Leetcode
        True_False_Table = {} # True_False_Table[i,j] = 1 if s[i:j+1] is a Palindrome
        # Bulilding as a dict is a poor idea because it's hard to visualize the table when debugging
        n = len(s)
        max_len = 0
        longest_begin = 0

        for i in range(n):
            True_False_Table[i,i] = True
        max_len = 1

        for i in range(n-1):
            if s[i] == s[i+1]:
                True_False_Table[i,i+1] = True
                max_len = 2
                longest_begin = i
            else:
                True_False_Table[i,i+1] = False

        for length in range(3,n+1):
            for i in range(0,n-length+1):
                j =  length + i -1
                if True_False_Table[i+1,j-1] and (s[i] == s[j]) :  
                    True_False_Table[i,j]= True
                    max_len = length
                    longest_begin = i
                else:
                    True_False_Table[i,j]= False

        return max_len, s[i:i+max_len]            
                                    


    def longestPalindrome_brute_force(self, s):
        # O(n^3) because of the two for loops + it takes O(n) to compare the substrings together
        s = [l.lower() for l in s if l.isalnum()]
        longest=''
        
        for i in range(len(s)): # Two loops, this is a bruteforce approach
            for j in range(i+1,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    if j-i+1 > len(longest):
                        longest = ''.join(s[i:j+1])

        return longest
        
    def allPalindrome_brute_force(self, s): # return all palindroms, used for debugging.
    
        s = [l.lower() for l in s if l.isalnum()]
        allPalindroms=[]
        
        for i in range(len(s)): # Two loops, this is a bruteforce approach
            for j in range(i+1,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    allPalindroms.append(''.join(s[i:j+1]))
        return allPalindroms                         


s = Solution()        