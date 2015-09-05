def generateNums(a, b):
	nums = []
	if a > b:
		return nums
	cur = a
	while not cur == b:
		cur = getNext(cur, b)
		nums.append(cur)

	return nums

def getNext(a, b):
	lastA = a[-1]
	lastB = b[-1]
	if lastA < lastB:
		next = a[:-1] + str(int(a[-1])+1)
	elif lastA == lastB:
		next = getNext(a[:-1], b[:-1]) + "0"	
	return next

if __name__ == "__main__":
	a = "100"
	b = "111"

	print(generateNums(b, a))

