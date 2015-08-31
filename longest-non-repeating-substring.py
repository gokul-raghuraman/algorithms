def getLongestNonRepeatingSubstring(input):
	map = {}
	maxLength = 0
	start = 0
	for i in range(len(input)):
		if not map.get(input[i]):
			map[input[i]] = i
		else:
			start = max(map[input[i]], start)
			map[input[i]] = i
		if i - start > maxLength:
			maxLength = i - start
	return maxLength

if __name__ == "__main__":
	input = "abcdeabca"
	print(getLongestNonRepeatingSubstring(input))