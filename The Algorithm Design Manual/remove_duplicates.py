#remove duplicates in a list


def remove_duplicates(lst):

	n=len(lst)
	if n<2:
		return lst

	i=0

	while i<n:
		for j in range(0,i):
			if lst[i]==lst[j]:
				lst.remove(lst[i])
				n-=1
				i-=1				
				break
		i+=1		

	return lst			


lst=[1,2]

remove_duplicates(lst)
