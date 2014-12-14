'''

https://oj.leetcode.com/problems/intersection-of-two-linked-lists/ 

        idea 1 : bruteforce it
            find the sortest of both list, A in this exampe
            for each element of A, check if for each element of B a.next == b.next
            when equal return a.next 
            O(n**2)
            
        idea 2 : return both lists and look at when the start to be different
            can I return a list on O(n) ?
            create a new list and insert at the begining instead of appending
            kind of feel like cheating the problem by using Python lists...
            
            work on simple cases
            
            => in the end it's impossible to solve the problem this way because you lose the information of whether two nodes with the same values are actually the same (same block of memory) or not.
            test case : {1,2,3,4,5,6,7,8,9,10,11,12,13}, {1,2,3,4,5,6,7,8,9,10,11,12,13}
                Impossible to know where the intersection happens.
  
        idea 2 bis : return the lists using these same nodes. But this will damage the real lists.
            can't copy and do this, because I lose the infor wether nodes are the same block of memory

        idea 3 : from the forums  Hashtable. TLE on leetcode, my implementation is below.
            O(n) space and O(n) time
            Put the list A in a hashtable, then for every item of list B, check if the place they belong to in the hashtable s already occupied. 
            If yes, then return this item. If no, keep going. If  

        idea 4 : introduce a delay between the traversal of the 2 lists.
            O(n) time and O(1) space

        ideas from the forum : https://oj.leetcode.com/discuss/17267/python-solution-with-some-thoughts-analysis
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode

    # idea 4
    def getIntersectionNode(self, headA, headB):
        
        lenA = self.find_length(headA)
        lenB = self.find_length(headB)

        if lenB < lenA:
            return self.getIntersectionNode(headB, headA)

        delay = lenB - lenA

        currentB = headB    
        currentA = headA
        counter = 0

        while counter < delay:
            currentB = currentB.next
            counter +=1

        while currentA != None and currentB != None:
            if currentA == currentB:
                return currentA
            currentA = currentA.next
            currentB = currentB.next

        return None        
            

    def find_length(self, head):
        current = head
        counter = 0
        while current != None:
            current = current.next
            counter += 1
        return counter    
'''
headA = ListNode(2)
headA.next = ListNode(3)
#headA.next.next = ListNode(10)
  
headB = headA.next
#headB.next = ListNode(5)
#headB.next.next = headA.next.next
'''
headA = ListNode(2)
headA.next = ListNode(3)
headA.next.next = ListNode(10)
  
headB = ListNode(1)
headB.next = ListNode(5)
headB.next.next = headA.next.next


s = Solution()

inter = s.getIntersectionNode(headA, headB)

print inter.val

''' 
        # idea3 TLE on leetcode
        visitedA={}
        current = headA 
        while current != None:
            visitedA[current]=True
            current = current.next
        print visitedA    

        current = headB
        while current != None:
            if visitedA.has_key(current):
                return current
            current = current.next
        
        return None  
'''

