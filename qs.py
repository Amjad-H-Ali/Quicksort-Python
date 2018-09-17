print("Quicksort!")

# Function that takes in array as argument and returns sorted array
def quick_sort(array):
	# Define and initialize length of array
	arrLen = len(array)
	# If one element in array, return
	if (arrLen < 2):
		return array

	# Define and initialize pivot to last number in array to compare to other digits in array
	pivot = array[arrlen - 1]

	# Define and initialize left to empty array
	left = [];

	# Define and initialize right to empty array
	right = [];
	

