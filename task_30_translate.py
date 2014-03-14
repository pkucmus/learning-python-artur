def translate(words):
	dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt"}
	return map(lambda word: dict[word], words)

print translate(['merry'])