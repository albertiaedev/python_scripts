# This is an implementation of the merge sort algorithm in Python,
# which is a divide-and-conquer algorithm that splits a given array into two halves,
# sorts them, and then merges them together

# This script is well docummented with comments to explain every step of this proccess

def merge_sort(array):
    # Returns 1 if the array contains none or just a single number
    if len(array) <= 1:
        return
    
    # Calculate the middle index of the array and split it in two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # Recursive call to the merge_sort function
    merge_sort(left_part)
    merge_sort(right_part)

    # These variables will be used to iterate through the halves and merge them together
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Iterates through both halves and compares their elements
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # If the left element is smaller, it is placed in the sorted position in the original array,
        # and the left_array_index is incremented
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        # If the right element is smaller, it is placed in the sorted position in the original array,
        # and the right_array_index is incremented
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1
        # The sorted_index is incremented after placing an element in the sorted position

    # For the left half:
    # Place the remaining elements in the sorted position in the original array
    # and increment the indices
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1
    
    # For the right half:
    # Place the remaining elements in the sorted position in the original array
    # and increment the indices
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1
        

# Checks if the script is being run directly or imported as a module
if __name__ == '__main__':

    # Define an unsorted array and print it
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array:',numbers)

    # Call the merge_sort function on the unsorted array and print the sorted array
    merge_sort(numbers)
    print('Sorted array:',str(numbers))