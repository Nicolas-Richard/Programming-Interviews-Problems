'''sentence='my name is Nicolas Richard turlututu'

words = sentence.split()

result=[]

for i in range(0, len(words)-2):
	result.append([words[i],words[i+1],words[i+2]])

print result	'''


sentence = 'i went to the store'.split(' ')
words = {}
for i in range(len(sentence)):
		words[sentence[i]] = [sentence[i+j] for j in range(3)]


