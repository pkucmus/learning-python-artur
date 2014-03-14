def find_hapaxes(filename):
    inputFile = open(filename, 'r')
    words = inputFile.read().split()
    inputFile.close()

    counter = {}

    for word in words:
        counter[word] = counter.get(word, 0) + 1

    return [word for word in counter.keys() if counter[word] == 1]

if __name__ == '__main__':
    print find_hapaxes('words.in')