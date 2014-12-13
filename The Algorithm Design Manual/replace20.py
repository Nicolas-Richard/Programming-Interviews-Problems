# replace spaces with %20

def replace20(str):

	n = len(str)
	lst = list(str)

	for i in range(0,n):
		if lst[i] == ' ':
			lst[i] = '%20'

	print "".join(lst)	
	return "".join(lst)		

replace20('my name is Nicolas')