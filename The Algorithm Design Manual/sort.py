import random
import copy
from heapq import merge


def quicksort_0(lst):
	
	if len(lst) < 1:
		return lst

	# pick randomly a pivot

	pivot_index = len(lst)/2

	# need to put everything that's bigger than pivot to it's right
	# everything that is smaller to its left

	i = 0

	while i < pivot_index:
		if lst[i] > lst[pivot_index]:
			tmp = lst[i]
			lst.remove(tmp)
			lst.insert(pivot_index,tmp)
			pivot_index -=1
			i -= 1
		i += 1

	i = len(lst) -1

	while i > pivot_index:
		if lst[i] < lst[pivot_index]:
			tmp = lst[i]
			lst.remove(tmp)
			lst.insert(0,tmp)
			pivot_index += 1
			i +=1
		i -=1	

	print str(lst[:pivot_index]) + '*' + str([lst[pivot_index]]) + '*' + str(lst[pivot_index+1:])

	return quick_sort(lst[:pivot_index]) + [lst[pivot_index]] + quick_sort(lst[pivot_index+1:])

def quicksort(lst):
    
    if len(lst) < 2 : 
        return lst 
    
    pivot = lst[0]
    
    greater = [x for x in lst[1:] if x > pivot ]
    lesser = [x for x in lst[1:] if x <= pivot]
    
    print quicksort(lesser) + [pivot] + quicksort(greater)
    

def merge_perso(A,B):
    
    for b in B:
        i = 0
        while i < len(A) and A[i]< b:
            i += 1
        A.insert(i,b)
    return A

def merge_sort(A):
    if len(A) <2:
        return A
    elif len(A) == 2:
        if A[0] <= A[1]:
            return A
        else:
            return [A[1],A[0]]
    elif len(A) > 2:
        return merge_perso(merge_sort(A[:len(A)/2]), merge_sort(A[len(A)/2:]))
    
print merge_sort([4,10,5,2,1])    


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

print quick_sort(lst)

print lst_copy == lst