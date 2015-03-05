class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
    	pass
        # do 2 binzary searches. One to find the first occurence, one to find the last occurence of the target.
        # I want to search not for the target itself, but the position where the target appears with a smaller predecessor and the position where the target appears with a bigger sucessor

        if self.BsearchList_bool(lst, target) == True:
            self.BsearchList(lst, target)
        else:
            return [-1,-1]    

    def BsearchList_bool(self, lst, target):
    	i = len(lst)/2
    	if len(lst) == 1:
    		if target == lst[i]:
    			return True
    		else:
    			return False	

    	elif target >= lst[i]:
    		return self.BsearchList_bool(lst[i:], target)
    	else:
    		return self.BsearchList_bool(lst[:i], target)


    def BsearchList(self, lst, target):
    	print lst
        i = len(lst)/2
        if target == lst[i]:
            #print 'here 0'
            if i == 0:
                return i
            elif target > lst[i-1]: 
                return i
            else: # in this case lst[i] and lst[i-1] are = to the target 
                # slice to get rid of this last int (or keep on looking to make a better slice)
                return 'duplicates means trouble !'

        elif target > lst[i]:
            #print 'here 1'
            return i+1 + self.BsearchList(lst[i+1:], target)
        else:
            #print 'here 2'
            return self.BsearchList(lst[:i], target)    

            



s = Solution()

lst = [x**2 for x in range(10)]

print s.BsearchList_bool(lst, 16) == True
print s.BsearchList_bool(lst, 0) == True
print s.BsearchList_bool(lst, 81) == True
print s.BsearchList_bool(lst, 15) == False
print s.BsearchList_bool(lst, 2) == False

print s.BsearchList(lst, 16) == 4
print s.BsearchList(lst, 25) == 5
print s.BsearchList(lst, 81) == 9
print s.BsearchList(lst, 0) == 0

lst.insert(3, 4)
lst.insert(3, 4)

print s.BsearchList(lst, 4) 


