
# My solution is straight forward. I loop through both lists at the same time while keeping track of the carry.
# Another solution tackles the problem differently by converting the lists to ints, summing them, and later building the list to be ouptuted, see here : https://oj.leetcode.com/discuss/16912/python-solution-please-share-your-opinions-about-improving

#https://oj.leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
    # Takes 2 ints represented as list in the reversed reading order, returns the sum represented as a list in the reversed reading order   
        
        carry=0
        tail=ListNode(0)
        result=tail
        
        while l1!=None or l2!=None:
            print 'here l1 or l2 !=0' 

            if l1!=None and l2!=None:    
                tail.next = ListNode((l1.val+l2.val+carry)%10)
                tail=tail.next
                print 'here equal'
                carry = (l1.val+l2.val+carry)/10
                l1=l1.next
                l2=l2.next
                
            elif l1!=None and l2==None:
                print 'here l1 !=None'                
                tail.next = ListNode((l1.val + carry)%10) 
                carry = (l1.val+carry)/10   
                tail=tail.next
                l1=l1.next
            
            elif l1==None and l2!=None:
                print 'here l2 !=None'                
                tail.next = ListNode((l2.val + carry)%10)
                carry = (l2.val+carry)/10 
                tail = tail.next
                l2=l2.next
            
        if carry !=0:
            tail.next=ListNode(carry)
        
        return result.next   

s=Solution()


l1 = ListNode(3) 
l1.next = ListNode(7)
#l1.next.next = ListNode(3)


l2 = ListNode(9) 
l2.next = ListNode(2)
#l2.next.next = ListNode(9)

'''
l1=ListNode(5)
l2=l1'''


result = s.addTwoNumbers(l1,l2)