def intersection(setA, setB):
	mapA = {}
	mapB = {}
	intersectedSet = []

	for i in range(len(setA)):
		if mapA.get(setA[i]):
			mapA[setA[i]] += 1
		else:
			mapA[setA[i]] = 1

	for i in range(len(setB)):
		if mapB.get(setB[i]):
			mapB[setB[i]] += 1
		else:
			mapB[setB[i]] = 1

	for item in mapA:
		if item in mapB:
			intersectedSet.extend([item] * min(mapA[item], mapB[item]))

	return intersectedSet



if __name__ == "__main__":
	setA = [0, 1, 1, 2, 2, 5]
	setB = [0, 1, 2, 2, 2, 6]

	print(intersection(setA, setB))