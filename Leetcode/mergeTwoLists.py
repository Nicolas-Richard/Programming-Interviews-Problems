'''
https://oj.leetcode.com/problems/merge-two-sorted-lists/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None    

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):

        # idea 1 :
            # create a new list result
            # go through both l1 and l2
                # while poping the first element and appending it to the result list

            # could do recursively but need a + operations between lists    
        
        if l1 == None:
            return l2
        if l2 == None:
            return l1    

        

        # initialization of tail
        if l1.val <= l2.val:
            tail = ListNode(l1.val)
            self.pop_first_element(l1) 
        else:
            tail = ListNode(l2.val)
            self.pop_first_element(l2)

        head = tail

        while l1.val != None and l2.val != None:
            if l1.val <= l2.val:
                tail.next = ListNode(l1.val)
                tail = tail.next
                self.pop_first_element(l1) 
            else:
                tail.next = ListNode(l2.val)
                tail = tail.next
                self.pop_first_element(l2)            

        if l1.val == None:
            tail.next = l2
            return head
        elif l2.val == None:
            tail.next = l1
            return head    
        else:
            return head

         
    def pop_first_element(self, l1):
        
        tmp = l1.val

        if l1.next != None:
            l1.val = l1.next.val
            l1.next = l1.next.next
        else:
            l1.val = None
            l1.next = None  

        return tmp             




s = Solution()

print s.mergeTwoLists(ListNode(2),ListNode(1)).val == True
print s.mergeTwoLists(ListNode(1),ListNode(2)).val == True

print s.mergeTwoLists(ListNode(2),None).val == 2
print s.mergeTwoLists(None,None) == None 

l1 = ListNode(1)
l1.next = ListNode(3)
l2 = ListNode(2)


l3 = s.mergeTwoLists(l1,l2)
print l3.val
print l3.next.val
print l3.next.next.val
if l3.val == 1 and l3.next.val == 2 and l3.next.next.val == 3:
	print True
else:
	print False
