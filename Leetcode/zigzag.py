
'''

You might struggle with what Zig Zag mean, see this : https://oj.leetcode.com/discuss/14105/what-does-zigzag-means

https://oj.leetcode.com/problems/zigzag-conversion/

'''

class Solution:
	# @return a string
	def convert(self, s, nRows):

		if nRows == 1:
			return s

		down = True
		position = 0

		strings = [''] * nRows

		for letter in s:

			strings[position] += letter

			if position == nRows -1:
				position -= 1
				down = False
			elif position == 0:
				position += 1
				down = True
			elif down:
				position += 1		
			else:
				position -= 1

		return "".join(strings)		
