import numpy as np

def binomialCoefficient(n,k):

	# Let's build the Pascal triangle

	triangle = np.zeros((n+1,n+1))
	triangle[0][1]=1
	for i in range(1,n+1):
		for j in range(1,n+1):
			triangle[i][j]=triangle[i-1][j-1] + triangle[i-1][j]
	#print triangle
	return triangle[n][k+2]	

result= 0

for i in range(1,19):
	result += binomialCoefficient(20,i)
print result	