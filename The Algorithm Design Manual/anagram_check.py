#check anagrams

def anagram_check(str1,str2):

	l1=list(str1)
	l2=list(str2)

	for i in l1:
		for j in l2:
			if i==j:
				l1.remove(i)
				l2.remove(j)
				print l1
				print l2


	return l1 == l2			



anagram_check('aaa','aaa')				