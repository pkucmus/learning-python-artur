def is_palindrome(string):
    for i in range(len(string)/2):
        if string[i] != string[-i-1]:
            return False

    return True

if __name__ == '__main__':
	print is_palindrome("kajak") == True
	print is_palindrome("kajaks") == False