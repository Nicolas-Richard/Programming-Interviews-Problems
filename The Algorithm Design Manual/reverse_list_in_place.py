#reverse list in place

def reverse_list_in_place(lst):

	tmp=[]
	n=len(lst)

	if n<=1:
		return lst

	for i in range(0,int(n/2)):
		tmp=lst[n-i-1]
		lst[n-i-1]=lst[i]
		lst[i]=tmp

	print lst	
		

lst = [1,2,3,3.5,4,5]

reverse_list_in_place(lst)		