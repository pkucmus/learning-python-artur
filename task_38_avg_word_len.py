def avg_word_len(filename):
    file = open(filename, 'r')
    words = file.read().split('\n')
    file.close()

    lengthSum = 0

    for word in words:
        lengthSum += len(word)

    return lengthSum/(len(words)-1)

if __name__ == '__main__':
    filename = raw_input('Type a filename\n')
    print avg_word_len(filename)
