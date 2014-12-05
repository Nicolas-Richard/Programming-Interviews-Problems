
class ListNode():
	def __init__(self, val):
		self.val = val
		self.next = None

	def __str__(self):
		result=''
		while self :
			result += ' ' + str(self.val)
			self = self.next
		return result


def merge2Lists_by_swapping_values(lst1,lst2): 

	head = ListNode(None)
	result = head

	while lst1 and lst2:
		if lst1.val < lst2.val:
			result.next = ListNode(lst1.val)
			result = result.next
			lst1 = lst1.next
		else:	 
			result.next = ListNode(lst2.val)
			result = result.next
			lst2 = lst2.next

	if lst1 == None:
		result.next = lst2

	if lst2 == None:
		result.next = lst1

	return head.next
	

def merge2Lists(list1, list2):
    
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


lst1 = ListNode(1)
lst1.next = ListNode(5)


lst2 = ListNode(4)
lst2.next = ListNode(6)					