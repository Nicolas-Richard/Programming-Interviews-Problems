'''
https://oj.leetcode.com/problems/remove-element/
This method doens't get accepted on Leetcode, it gets TLE on the first trivial test case, however works fine locally
Here, method that gets accepted using Python built-in functions : https://oj.leetcode.com/discuss/15084/python-code-does-not-works
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        
        # idea 1 : we only need the new length, go through the elements and +1 counter when we match.
        # then return length - counter
        # 3 mins
        # actually need to do the modification to the array.
            # doesn't matter where I put the elements
                # swaps with the last one ?
                
        # idea 2 : find the max
        #           replace this element by max +  1
        #           sort n then slice
        
        # idea 3 : when find element, swap it
            #like bubble sort, at the end all elements should be at the end of the array
            
         
        if A == []:
            return 0
            
        flag = True    
        i = 1
            
        while flag == True:
            for i in range(1,len(A)):
                flag = False
                if A[i-1] == elem:
                    A[i-1] = A[i]
                    A[i] = elem
                    flag = True

        for i in range(len(A)):
            if A[i] == elem:
                A = A[:i]
                print A
                return len(A[:i])

        return len(A)        
                    
s = Solution()

print s.removeElement([],2)   
                
           