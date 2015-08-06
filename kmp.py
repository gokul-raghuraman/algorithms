"""
Knuth-Morris-Pratt algorithm for string search.

Given a string s (length m) and a pattern p (length n), 
return the position at which p begins in s.

Running time: O(m+n)

->We first compute the prefix array for the string p. See
the next method for how to do this.
->The algorithm uses 2 index pointers i and j, both of which 
start from index 0. 
->i tracks the search position in s, and j tracks the search 
posiion in p.
->We start a loop that ends if either i or j reaches the end 
of s or p (respectively).
	->We compare s[i] and p[j]:
		-->If they are equal, then we increment both i and j
		-->If not, then we check if j > 0:
			--->If yes, then we set j to the value in the prefix
				array at index j-1.
			--->Else, increment only i
->We check if j is equal to length of p. This means we have had 
successful consecutive comparisons until the end of p.
	-->If yes, then we return i-j which gives the start position
		of p in s (remember i tracks j as long as the chars 
		are equal)
	-->If not, then we return -1 for a failure.


"""
def getPosKmp(s, p):
	prefixArray = getPrefixArray(p)
	i = 0
	j = 0
	while i < len(s) and j < len(p):
		if s[i] == p[j]:
			i += 1
			j += 1
		else:
			if j > 0:
				j = prefixArray[j-1]
			else:
				i += 1
	if j == len(p):
		return i-j
	else:
		return -1



def getPrefixArray(p):
	"""
	Method that returns a prefix array. The array looks something like this:
	E.x.: [0, 0, 1, 2, 3, 0, 0, 1]

	This array is used to compute the position to start searching from within
	the main string in the KMP algorithm. It is simply the max value in this
	array (in the above example, it is 3).

	To compute this array, we use 2 index pointers - i and j. 
	(1) i starts with 0, and j starts with 1.
	(2) We initialize an array cont with the first value of 0.
	(3) We compare the characters at position i and j: 
			->If they're equal, then we append cont with a value i + 1, and 
			  increment both i and j.
			->If not, then:
				-->If i is greater than 0, we reset i to be equal to the value
				   stored in cont[i-1]
				-->If not, then we append cont with 0, and increment only j.
			We stop when j reaches the end of the string.
	"""
	cont = [0]
	i = 0
	j = 1
	while j < len(p):
		if p[j] == p[i]:
			cont.append(i+1)
			i += 1
			j += 1
		else:
			if i > 0:
				i = cont[i-1]
			else:
				cont.append(0)
				j += 1
	return cont


if __name__ == "__main__":
	s = "abcxabcdabxabcdabcdabcy"
	p = "dabcdabc"
	print(getPosKmp(s, p))