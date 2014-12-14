'''
Accepted solution in one pass

        # if I can do 2 pass : 
            # 1st pass : find the length
            # 2nd pass : stop at the right node to do surgery
            
        # if I can do one pass only :
            # go through the list while keeping track of the node that comes in n position before the actual node
        

https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/

'''


# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        

        
        tail = head
        counter = 0
        target = head
        before_target = head

        while tail != None:
        
            if counter > n-1:
                target = target.next

            if counter > n:
                before_target = before_target.next

            tail = tail.next
            counter += 1
            print counter  
            
        if counter == n:
            return head.next   

        before_target.next = target.next  
     
        return head    
            
test1 = ListNode(1)
test1.next = ListNode(2)
test1.next.next = ListNode(3)        
test1.next.next.next = ListNode(4)        

s=Solution()
s.removeNthFromEnd(test1, 4)

print '######'
print test1.val
print test1.next.val
print test1.next.next.val
print test1.next.next.next == None