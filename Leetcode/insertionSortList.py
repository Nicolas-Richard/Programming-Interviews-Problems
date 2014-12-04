# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
 		self.val = x
		self.next = None

class Solution:
# @param head, a ListNode
# @return a ListNode

	# Working solution but I'm not acutally swapping nodes, I'm just swapping their values which would be a a problem if the Nodes had more than just a value... 
	# Receive a TLE on Leetcode
	def insertionSortList(self, head):
		tmp =0
		i = head
		j = head
		count_i = 0
		count_j = 0

		try:
			head.next == None
		except:
			return head	

		while i != None:
			count_j = 0
			j = head
			while count_j < count_i :
				if i.val > j.val:
					pass
				else :
					tmp = j.val
					j.val = i.val
					i.val = tmp
				j = j.next
				count_j+=1				

			i = i.next
			count_i+=1
			print '%d %d %d %d' %(head.val,head.next.val, head.next.next.val, head.next.next.next.val)

		return head				 


	def insertionSort(self, lst):
		n = len(lst)
		tmp = 0
		for i in range(n):
			for j in range(i):
				if lst[i] > lst[j]:
					pass
				else :
					tmp = lst[j]
					lst[j] = lst[i]
					lst[i] = tmp
			#print lst
		return lst			


s= Solution()

'''
# test for insertionSort

import copy
import random

lst = []
for i in range(20):
	lst.append(random.randint(0,100))

lst_copy = copy.copy(lst)

lst_copy.sort()
s.insertionSort(lst)

print lst_copy == lst
'''

lst = ListNode(3)
lst.next = ListNode(2)
lst.next.next = ListNode(1)
lst.next.next.next = ListNode(0)

