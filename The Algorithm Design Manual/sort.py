import random
import copy
from heapq import merge


def quick_sort(lst):
	
	pivot = lst[0]



def merge_sort(lst_input):

 	n = len(lst_input)

	if n < 2:
		return lst_input

	if n > 1:
		left = merge_sort(lst_input[:n/2])
		right = merge_sort(lst_input[n/2:])
		global lst 								# Little trick to avoid having to keep the test case the same for every sort function
		lst = list(merge(left,right)) # sort of avoiding half of the exercise difficulty by using an already implemented merge function
		return lst	


def selection_sort(lst):

	counter = 0
	flag = False

	for j in range(len(lst)):

		min_val = lst[j]
		min_position = j

		for i in range(j+1, len(lst)):

			if lst[i] < min_val:
				min_val = lst[i]
				min_position = i

		tmp = lst[j]
		lst[j] = min_val
		lst[min_position] = tmp

	return lst	


def bubble_sort(lst):

	tmp = 0
	has_changed_flag = True

	while has_changed_flag == True:
		has_changed_flag = False # This is kind of confusing. The while statement doesn't stp here bc the while condition is checked upon only when tlast line of code in the loop has been executed.
		for i in range(len(lst)-1):
				if lst[i] > lst[i+1]:
					tmp = lst[i]
					lst[i]=lst[i+1]
					lst[i+1] = tmp
					has_changed_flag = True
					# And here the while statement condition is checked.
	
	return lst
	
# Test case #

lst= []			
for i in range(10):
	lst.append(random.randint(-100,100))

lst_copy = copy.copy(lst)
lst_copy.sort()

print merge_sort(lst)

print lst_copy == lst