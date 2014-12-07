

def fibo_rec(n):

	if n==0:
		return 0
	if n == 1:
		return 1

	else:
		return fibo_rec(n-1)+fibo_rec(n-2)

def fibo_it(n):

	result=0
	prv=1
	prvprv=0

	if n<2:
		return n

	for i in range(1,n):
		result= prv + prvprv
		prvprv=prv
		prv=result
		i+=1		
	return result




fibTable = {1:1, 2:1}

def fib_rec_hash(n):
	if n in fibTable:
		return fibTable[n]

	else:
		fibTable[n]=fib_rec_hash(n-1)+fib_rec_hash(n-2)
		return fibTable[n]
