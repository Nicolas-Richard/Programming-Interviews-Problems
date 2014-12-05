
# My ideas and their time complexities while I worked through the problem.

# n words at most per list. k lists.
# idea 1 : find the minimum of the k lists and append it to the result list, repeat untill all k lists are empty. O(n*k^2)
# idea 2 : merge the k lists to the first one which become the result. Problem this first list becomes larger and larger and each merge become more and more expensive.
# idea 3 : merge the lists by pair untill we have only 1 remaining list. We do log(k) merges. Each one is at most 2*n comparisons. Total time complexity : O(n*log(k)). Source : http://jelices.blogspot.com/2014/06/leetcode-python-merge-k-sorted-lists.html

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            nextLists = []
            for i in range(0,len(lists)-1,2): # The 0 here is important, otherwise you might have i == -1
                nextLists.append(self.merge2Lists(lists[i],lists[i+1]))
            if len(lists) % 2 == 1:
                nextLists.append(lists[len(lists)-1])
            lists = nextLists
        
        return lists[0]    
                

    def merge2Lists(self, list1, list2): # O(m+n)
        
        head = ListNode(-1)
        tail = head
    
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
            
            else:
                tail.next = list2
                tail = tail.next
                list2 = list2.next
        
        if list1 == None:
            tail.next  = list2        
    
        if list2 == None:
            tail.next  = list1 
    
        return head.next
            
            
            
            
            
