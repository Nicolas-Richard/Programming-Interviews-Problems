#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):

        # idea 1 : function to swap two and return the next one
        	# then I can this fuction on head
        
    	new_head = head.next

    	while head != None:
	    	head = self.swapTwo(head)

    	return new_head

    def swapTwo(self, head):
    
    	# 1->2->3

    	tmp = head # tmp = 1
    	tmp2 = head.next # tmp2 = 2

    	head, head.next = head.next, head # 2-> 1 -> 2



    	return head

s = Solution()

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c

print '#'*10
print a.val
print a.next.val

tmp = a #1->2
'''
a = a.next

print '#'*10
print a.val
print b.val

a.next = tmp

print '#'*10
print a.val
print a.next.val 
print a.next.next.val   
print a.next.next.next.val   
'''

tmp0 = ListNode(0)

tmp0 = b
b = c
c = c.next

tmp0.next = c
b.next = c.next
c.next = b

