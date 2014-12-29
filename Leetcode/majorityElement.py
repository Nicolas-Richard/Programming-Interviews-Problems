'''
https://oj.leetcode.com/problems/majority-element/
'''

class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):

        # assuming that the majority element always exist is like saying. Find the element that appears the most often
        # use a dict to count the occurences of the elements, then find the biggest value in the dict
            # n to build the dict
            # n to fill the dict
            # n to find the biggest element

        # sort the table Onlogn
        # pass through the table while holding a counter of the number of occurences of the current elemnt,
            # if couter > [n/2] then return this element

        my_dict = {}

        for element in num:
            my_dict[element] = 0
        
        for element in num:
            my_dict[element] += 1


        for key in my_dict.keys():
            if my_dict[key] > len(num)/2:
                return key

s = Solution()

