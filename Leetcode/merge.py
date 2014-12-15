# Not accepted by Leetcode : https://oj.leetcode.com/problems/merge-sorted-array/

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        

        # idea 1 : bruteforce
            # define an insert method that scans through A to put a new element at the right position
            # call this method on all elements of B by going through B linearly
            # O(nm) if insertion straight
            # O(logm * n ) if insertion uses binary search
                # search will take O(logm) but the insertion require to move around elments => O(logm)
         
        # 5 mins

        # 10 mins

        # idea 2 : glue together A and B, the sort O(log(n+m))
            # quick sort ?
            # merge sort ?
            # heap sort ?
            # bubble sort ? (thanks wiki !)
                # => was able to pull it off in time + 2 minuts.
                    # but won't pass the tests because don't take the same arguments
                    # impossible to default in this order the length...

                    # Ouch, big mistake bubble sort is not O(log n) it's O(n**2 in average)

        for element in B:
            A.append(element)

        return self.bubble_sort(A)        
        
    def bubble_sort(self,A):

        flag = True # will get false when no modifications

        while flag == True:
            flag = False
            print A
            for i in range(len(A)-1):
                if A[i] > A[i+1]:
                    tmp = A[i]
                    A[i] = A[i+1]
                    A[i+1] = tmp
                    flag = True

        return A            

s = Solution()

lst = [5,3,2,7]


            
        
            
            
            
            
            
            
        