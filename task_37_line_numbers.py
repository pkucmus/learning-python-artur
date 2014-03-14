def print_line_numbers(filename):
    inputFile = open(filename, 'r')
    outputFile = open(filename[:-2] + 'out', 'w')
    lines = inputFile.read().split('\n')

    for i, line in enumerate(lines[:-1]):
        outputFile.write("{0} {1}\n".format(i, line))

    inputFile.close()
    outputFile.close()

if __name__ == '__main__':
    filename = raw_input('Type a filename?\n')
    print_line_numbers(filename)