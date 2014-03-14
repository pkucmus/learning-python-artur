from task_8_is_palindrome import is_palindrome

def is_palindrome_ext(string):
    punctuations =  [
        '!', '#', '"', '%', '$', "'", '&', ')', '(', '+',
        '*', '-', ',', '/', '.', ';', ':', '=', '<', '?',
        '>', '@', '[', ']', '\\', '_', '^', '`', '{', '}',
        '|', '~', ' '
        ]

    for punc in punctuations:
        string = string.replace(punc, '')

    return is_palindrome(string.lower())

print is_palindrome_ext('Was it a rat I saw?') == True