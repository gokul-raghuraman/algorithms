"""
Return all permutations of a string

Trick: Notice that permuting a string (E.g. ABC) can be broken down as:
	(1) Picking one character and fixing at the beginning (A)
	(2) Permuting all other characters (BC)
	(3) Prepending the fixed character to each permuted combination returned by step 2
		i.e. A + BC, A + CB
	(4) Repeating (1)-(3) for each character as fixed character
"""

class Solution:
	permutations = []

	def permute(self, input):

		if len(input) == 0:
			return [input]
		
		permutations = []
		for i in range(len(input)):
			fixed = input[i]
			permutedList = self.permute(input[:i] + input[i+1:])

			for permutedCombo in permutedList:
				permutations.append(fixed + permutedCombo)

		return permutations 

if __name__ == "__main__":
	string = "ABC"
	sol = Solution()

	print(sol.permute(string))