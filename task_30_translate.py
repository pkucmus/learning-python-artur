def translate(words):
	dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt"}
	return map(lambda word: dictionary.get(word,word), words)

print translate(['merry', 'god', 'test', 'christmas', 'test2'])