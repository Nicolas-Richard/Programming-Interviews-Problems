'''
Write an algorithm which computes the number of trailing zeros in n factorial
'''

from random import randint

# The solution
def trailing_zero_factorial(num):
	'''Instead of computing the factorial we can simply count how many 5s are in its
	decomposition in prime numbers'''
	counter = 0
	for i in range(1,num+1):
		tmp = i
		while tmp % 5 == 0 :
			tmp = tmp /5
			counter +=1
	return counter
			
# Testing functions
def factorial(n):
	if n == 0:
		return 1
	result = 1
	for  i in range(1,n+1):
		result = result*i
	return result

def trailing_zero(num):
	''' This function won't work on numbers with 0 at the begining (ex : 012 instead of 12)
	because str() will not interpret them as integers
	'''
	n = len(str(num))
	num_str = str(num)
	counter = 0
	for i in range(n):
		if num_str[n-i-1] == '0':
			counter +=1
		else:
			break
	return counter

# Tests

num = randint(0,100)

fact = factorial(num)
number_of_trailing_zeros = trailing_zero(fact)
print num
print number_of_trailing_zeros == trailing_zero_factorial(num)
