'''
https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/

The solution I was inspired by explained here : https://oj.leetcode.com/discuss/16391/python-o-n-solution-that-uses-a-dictionary

'''


class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        
        # idea 2
            # when encountering an element that is already in the set :
            # find where it is in the previous substring and restart from there
            # keep track of the head and tail of the current substring

            # pass through the string
                # add element to the set/ dict


        maxlength = 0
        templength = 0
        charused = {}
        head = 0

        for i in range(len(s)):
            if s[i] not in charused or charused[s[i]] < head:
                charused[s[i]] = i
                templength += 1
                maxlength = max(maxlength, templength)
            elif s[i] in charused:
                head = charused[s[i]] + 1
                charused[s[i]] = i
                templength = i - head + 1
                maxlength = max(maxlength, templength)

        return maxlength


    def lengthOfLongestSubstring_On2(self, s): #TLE on Leetcode
        
        # idea 1
            # for every char in the string : i
            # start going through the rest of the string (j) and build a dict while checking if the key is already there. 
            # If it's there stop, check the counter (i-j), if bigger than previous, assign string[i:j] to the result
            # O(n2) worst case, if the string has no duplicated char at all
        
        if not s:
            return 0

        longest = 0

        for i in range(len(s)): 

            char_set = set()
            char_set.add(s[i])
            for j in range(i+1, len(s)):
                if s[j] not in char_set:
                    char_set.add(s[j])
                else:
                    break
            if len(char_set) > longest:
                longest = len(char_set)

        return longest    



s = Solution()


