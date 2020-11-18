def word_count(x):
	count = {}
	for char in x:
		count[char] = x.count(char)
	return count
print(word_count('hello world'));
