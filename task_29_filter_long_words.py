def filter_long_words(words, n):
	return filter(lambda word: len(word) > n,words)

print filter_long_words(['ala','ma','kota','asdffdf'], 3) == ['kota', 'asdffdf']