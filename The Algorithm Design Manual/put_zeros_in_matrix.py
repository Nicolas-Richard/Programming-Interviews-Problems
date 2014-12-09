

A=[[1,0,3,4],[5,6,7,8],[9,10,11,12]]


def put_zeros_in_matrix(A):

	n=len(A)
	m = len(A[0])

	lst =[]

	for i in range(0,n):
		for j in range(0,m):
			if A[i][j] == 0:
				lst.append([i,j])

	for l in lst:
		p = l[0]
		q = l[1]

		for i in range(0,n):
			A[i][q] = 0

		for j in range(0,m):
			A[p][j] = 0				


put_zeros_in_matrix(A)			