# I've actually not understood what was the problem !!!
# This is the solution to another problem !


class Solution:
	# @return a string
	def convert(self, s, nRows):
		result=''

		if nRows == 1:
			return s

		if len(s) <=nRows :
			return s	

		mydict = self.build(s,nRows)

		for k in mydict:
			for char in mydict[k]:
				result+=char



	def build(self, s, nRows):
		mydict={}
		for i in range(0,nRows):
			mydict[i]=[]

		#print dict	

		count_row = 0
		count_columns=0	

		for i in range(0,len(s)):
		
			if ((count_columns % 2) ==0):
				mydict[count_row].append(s[i])
				count_row+=1

				if count_row >= nRows:
					count_columns+=1
					count_row = 0

			elif ((count_columns % 2) == 1):
				count_row+=1
				mydict[count_row].append(s[i])
				count_row+=1

				if count_row >=nRows-1:
					count_columns+=1
					count_row=0	
		
		return mydict		

		
s=Solution()

print s.convert('ABC',1)						