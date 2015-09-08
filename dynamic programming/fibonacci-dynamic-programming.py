fib = [1, 1]

def getNthFib(n):
	for i in range(2, n):
		fib.append(fib[i-1] + fib[i-2])
	return fib[-1]

if __name__ == "__main__":
	n = 3
	print(getNthFib(n))