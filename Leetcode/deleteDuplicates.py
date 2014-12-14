'''
O(n) solution
https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        
        current = head
        previous = head
        counter = 0
        flag = False
        
        while current != None:
            
            if counter == 0: #The counter is at 0 when we just have deleted a node or at the start of the list
                            # when it's the case, it means we need to create a delay between the current and the previous node
                current = current.next
            else: # Otherwise we just move both nodes together
                current = current.next
                previous = previous.next

            # Let's check if these two nodes are duplicates
            if current != None and current.val == previous.val: # if wrote in the opposite order this test will break
                flag = True

            # Actually we only need to know if the counter is 0 or not. Could be replaced by a boolean flag
            counter +=1

            if flag == True:
                previous.next = previous.next.next
                counter = 0
                flag = False

        return head

      
test1 = ListNode(1)
test1.next = ListNode(1)
test1.next.next = ListNode(2)        

test2 = ListNode(1)
test2.next = ListNode(2)
test2.next.next = ListNode(2) 


test3 = ListNode(1)
test3.next = ListNode(1)
test3.next.next = ListNode(1) 


print '***'

s=Solution()
s.deleteDuplicates(test3)





