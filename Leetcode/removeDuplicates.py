'''
Accepted on leetcode, smart idea : instead of removing duplicates, count uniques.
The methods that are commented got TLE on leetcode
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

class Solution:
    # @param a list of integers
    # @return an integer

    def removeDuplicates(self, A):

        # idea3 : from leetcode forum. Double index, just save elements when they are different, then slice;

        i = 1
        j = 1

        while j < len(A):
            if A[j-1] != A[j]:
                A[i] = A[j]
                i += 1
            j +=1

        print A[:i]            
        return i

s = Solution()

print s.removeDuplicates([])       

'''
    def removeDuplicates_using_pop(self, A):
        
        # idea 1 : move along the array with 1 pointer
        #    check if current - 1 = current, if true raise flag
        #            if flag raised remove one of the element
        
        
        #        else : keep going
        # 
        # how to travel a list of changing length ?
            # => while i < len(A)
            # 
        # how to 
        #   delete the duplicate
            # list.remove(A[i]) 
                
        # note : it is sorted => duplicates are consecutive    
        
        i = 1
        while i < len(A): # every time need to go through the list to find it's length O(n)
            if A[i-1] == A[i]:
                A.pop(i-1) # O(n) because needs to search => O(n**2). But I have the position of the element to remove, probably can do better using that
                                # using pop you don't have to do a search. But still need to go to the element. Less expensive but still O(n), actually if it was an array, it would be O(1).
                i -=1
                print i 
            i +=1
        print A
        return len(A)

    def removeDuplicates_no_pop(self, A):

        # idea 2 :
            # when 2 consecutives numbers (or not ordered), find the next one that is bigger, 
            # and put it there
            # when run out of bigger numbers to insert => finish. return a slice that stops there
            # while with flag for 'no big numbers'

        n = len(A)
        i = 1

        while i < n: # O(n)
            if A[i-1] == A[i]:
                j = i
                while j < n: #O(n) => O(n**2)
                    if A[j] <= A [i-1]: 
                        j += 1
                    else:
                        tmp = A[i]
                        A[j-1] = A[j]
                        i = 1 # this is very expensive, every time I restart from the begining of the list 
                        break
                if j == n:
                    return A[1:i]
            i += 1

'''        