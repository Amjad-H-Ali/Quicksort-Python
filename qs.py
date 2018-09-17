print("Quicksort!")

# Function that takes in array as argument and returns sorted array
def quick_sort(array):
	# If one element in array, return
	if (len(array) < 2):
		return array

