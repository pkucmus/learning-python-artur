def are_semordnilap(word1, word2):
    if len(word1) != len(word2):
        return False

    for i in range(len(word1)):
        if word1[i] != word2[-i-1]:
            return False

    return True

def print_semordnilaps(filename):
    file = open(filename, 'r')
    words = file.read().split('\n')

    for i in range(len(words)):
        for j in range(i+1, len(words)): 
            if are_semordnilap(words[i], words[j]):
                print words[i], words[j]

    file.close()

if __name__ == '__main__':
    filename = raw_input('Which file you would like to check?\n')
    print_semordnilaps(filename)