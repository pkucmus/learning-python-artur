from task_21_char_freq import char_freq

def char_freq_table(filename):
    file = open(filename, 'r')
    result = char_freq(file.read())

    for char, count in result.items():
        print char, count

    file.close()

if __name__ == '__main__':
    filename = raw_input('Which file you would like to check?\n')
    char_freq_table(filename)