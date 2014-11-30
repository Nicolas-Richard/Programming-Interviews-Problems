
# The second solution doens't do what is expected to do by Leetcode, so in this sense it's totally wrong. I kept it as it can help understand the acutal solution which uses the same idea.
# These solutions were not accepted on LeetCode. However the atoi() method probably should, the error I receive on Leetcode doesn't appear on my computer.
# See my post on Leetcode here : https://oj.leetcode.com/discuss/17313/python-valueerror-invalid-literal-for-int-with-base-10

#https://oj.leetcode.com/problems/string-to-integer-atoi/ 

class Solution:
    # @return an integer
    def atoi(self, str):

    	str = str.replace(' ','z')
    	
    	first_int_index=-1
    	for c in str:
    		if c.isdigit():
    			first_int_index=str.index(c)
    			break
    	if first_int_index==-1:
    		return 0
    	print first_int_index

    	plus_flag=0
    	minus_flag=0
    	for c in str[:first_int_index]:
    		if c =='+':
    			plus_flag=1
    		if c =='-':
    			minus_flag=1	
    			
    	first_non_int_index=-1
    	for c in str[first_int_index:]:
    		if c.isdigit() == False:
    			first_non_int_index=str.index(c)
    			break
    	print str[first_int_index:]
    	print first_non_int_index		

    	result=0
    	if first_non_int_index ==-1:		
    		result = int("".join(str[first_int_index:]))
    	else:
    		result = int("".join(str[first_int_index:first_non_int_index]))
    		
    	
    	if plus_flag and minus_flag:
    		return 0
    	elif minus_flag:
    		return -result
    	else:
    		return result
    		
    				

    def atoi_all_int_in_string(self,str):
    	all_ints = [c for c in str if c.isdigit()]
    	return int("".join(all_ints))
		
s=Solution()