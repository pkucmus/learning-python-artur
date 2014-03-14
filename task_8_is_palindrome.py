from task_7_reverse import reverse

def is_palindrome(string):
    return string == reverse(string)

if __name__ == '__main__':
	print is_palindrome("kajak") == True
	print is_palindrome("kajaks") == False