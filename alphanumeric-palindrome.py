def isAlphaNumericPalindrome(string):
	front = 0
	back = len(string) - 1

	while front < back:
		while front < len(string)-1 and not string[front].isalnum():
			front += 1
		while back > 0 and not string[back].isalnum():
			back -= 1

		if not string[front].lower() == string[back].lower():
			return False
		front += 1
		back -= 1
	return True

if __name__ == "__main__":
	string = "A man, a plan, a canal, Panama!"
	string2 = "!aA"
	print(isAlphaNumericPalindrome(string))