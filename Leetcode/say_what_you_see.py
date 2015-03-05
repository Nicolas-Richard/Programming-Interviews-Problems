'''
Just like a Leetcode problem, but was the sample problem sent by Dropbox.
Not the actual problem they wanted me to solve, this was just to get used to HackerRank.
'''

# Complete the function below.

def say_what_you_see(input_strings):

	full_result =[]

	for input_string in input_strings:
		#go through the string looking for alternate chars
		i = 0
		result = ''
		counter = 1

		while i < len(input_string)-1:
			if input_string[i] == input_string[i+1]:
				i += 1
				counter += 1
			else:
				result += str(counter) + input_string[i]
				i += 1
				counter = 1	
		
		# take care of the last char

		if input_string[i] == input_string[i-1]:
			result += str(counter) + input_string[i]
		else:
			result += '1' + input_string[i]	

		full_result.append(result)

	return full_result


print say_what_you_see(['1','12', '215','123456'])


'''
input0 = ['2','12','21']
input1 = ['3', '215', '5', '0']
input2 = ['1', '05']
input3 = ['2', '2222', '888888888']
input4 = ['1', '1111111111']
input5 = ['1', '112223']

print say_what_you_see(input0)
print say_what_you_see(input1)
print say_what_you_see(input2)
print say_what_you_see(input3)
print say_what_you_see(input4)
print say_what_you_see(input5)
'''


