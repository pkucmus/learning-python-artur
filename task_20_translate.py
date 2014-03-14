def translate(words):
    dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt"}
    result = []
    for word in words:
    	result.append(dictionary.get(word, word))

    return result

print translate(['merry', 'christmas', 'and', 'happy', 'new']) == ['god', 'jul', 'och', 'gott', 'nytt']