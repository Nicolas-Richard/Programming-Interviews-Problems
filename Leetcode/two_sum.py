'''
https://oj.leetcode.com/problems/two-sum/
'''

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        
        hashtable = {}
        for n in num:
            hashtable[n] = n
        
        for i in range(len(num)):
            if hashtable.has_key(target - num[i]):
                if num.index(target-num[i]) == i:
                    continue
                if i+1 <=num.index(target-num[i])+1:
                    return (i+1, num.index(target-num[i])+1)
                else:
                    return (num.index(target-num[i])+1, i+1)
    