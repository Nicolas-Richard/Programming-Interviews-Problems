
'''Merge two sorted arrays'''

def merge(A,B):

	# loop from the start of B
		# insert b at the right position 


	for j in range(len(B)):
		i = 0
		while B[j] > A[i]:
			i += 1
		A.insert(i,B[j])	

	return A		


A =	[1]
B = [0.5]

print merge(A,B)