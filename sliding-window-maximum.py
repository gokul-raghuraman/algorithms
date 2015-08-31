"""
Get a list of maximum values in a window of size k
sliding over a given input.

Intuition: A sliding window can be viewed as a queue,
where at each iteration, one element comes in and
another goes out.

We want to use a deque (double-ended queue, because we
want to be able to pop both from left and right sides)

"""

from collections import deque

def slidingWindowMaximum(inputs, k):

	n = len(inputs)

	"""
	Declare empty results array
	"""
	results = []

	"""
	Populate the indices of the initial k elements into the queue, 
	and keep the maximum seen so far on the left (so it's easy to pop 
	and assign later). Why indices? Because as the queue slides, we 
	want to drop the indices that are outside the window out of the queue.
	"""
	queue = deque()

	for i in range(k):
		while queue and inputs[i] > inputs[queue[-1]]:
			queue.pop()
		queue.append(i)

	"""
	Step 1|: Now iterate i=0 to n-k+1 times, and append the queue's first element 
	to results at each iteration.

	Step 2|: Next, we pop (left) elements out of the queue that are outside the sliding 
	window range. In this iteration, since we've already picked the maximum 
	(at index i), we will popleft all indices that are less than or equal to i.

	Step 3|: Next, we shift the window to the right, this means we again keep popping
	from the queue until the newly added number is lesser than the queue's
	last element (remember, we've already extracted the max value out into 
	results, so we're prepping for the next number). Then add this next number
	into the queue.
	
	"""
	for i in range(n-k+1):
		# Step 1
		results.append(inputs[queue[0]])

		# Step 2
		while queue and queue[0] <= i:
			queue.popleft()

		# Step 3
		while queue and inputs[i+k-1] > inputs[queue[-1]]:
			queue.pop()
		queue.append(inputs[i])

if __name__ == "__main__":
	inputs = [2, 3, 4, 2, 6, 2, 5, 1]
	k = 3

	print(slidingWindowMaximum(inputs, k))