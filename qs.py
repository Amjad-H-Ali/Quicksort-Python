print("Quicksort!")

# Function that takes in array as argument and returns sorted array
def quick_sort(array):
	# Define and initialize length of array
	arrLen = len(array)
	# If one element in array, return
	if (arrLen < 2):
		return array

	# Define and initialize pivot to last number in array to compare to other digits in array
	pivot = array[arrLen - 1]

	# Define and initialize left sub-array
	left = [];

	# Define and initialize right sub-array
	right = [];

	# For loop to iterate over indices in array but the pivot
	for i in range(0, arrLen - 1):

		# If current element is less than the pivot
		# place it in the left sub-array
		if (array[i] < pivot):
			left.insert(array[i])

		# Otherwise, place it in right
		else:
			right.insert(array[i])

	# Recursively, do the above code to the left and right sub arrays
	# while placing the pivot in between
	return quick_sort([*quick_sort(left), pivot, *quick_sort(right)])		



print(quick_sort([31, 17, 13, 0, 0, 42, 0, 9, 5, 7, 9, 19, 2]))