def rotateLeft(string, k):
	n = len(string)
	k = k % n
	string = string[k:] + string[:k]
	return string

if __name__ == "__main__":
	k = 4
	string = "ABCDEFGHIJ"
	print(rotateLeft(string, k))