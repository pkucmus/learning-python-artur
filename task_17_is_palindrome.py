from task_8_is_palindrome import is_palindrome

punctuations =  [
    '!', '#', '"', '%', '$', "'", '&', ')', '(', '+',
    '*', '-', ',', '/', '.', ';', ':', '=', '<', '?',
    '>', '@', '[', ']', '\\', '_', '^', '`', '{', '}',
    '|', '~', ' '
    ]

def is_palindrome_ext(string):
    for punc in punctuations:
        string = string.replace(punc, '')

    return is_palindrome(string.lower())

if __name__ == '__main__':
	print is_palindrome_ext('Was it a rat I saw?') == True