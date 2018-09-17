print("Quicksort!")

# Function that takes in array as argument and returns sorted array
def quick_sort(array):
	# If one element in array, return
	if (len(array) < 2):
		return array

	# Define and initialize pivot to last number in array to compare to other digits in array
	pivot = len(array - 1)

