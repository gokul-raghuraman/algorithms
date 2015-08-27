def binSearch(input, searchItem, lo, hi):
	if lo > hi:
		return -1
	mid = lo + (hi - lo) / 2
	if input[mid] == searchItem:
		return mid
	elif input[mid] < searchItem:
		return binSearch(input, searchItem, mid+1, hi)
	else:
		return binSearch(input, searchItem, lo, mid-1)


if __name__ == "__main__":
	input = [1, 4, 6, 6, 6, 6, 6, 6, 6, 6, 9, 12, 14, 15, 19, 31]

	print(binSearch(input, 6, 0, len(input)))