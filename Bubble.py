def bubble_sort(array):
  """Sorts an array in ascending order using the bubble sort algorithm.

  Args:
    array: A list of elements to be sorted.

  Returns:
    A sorted list of elements.
  """

  for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]

  return array


# Example usage:

array = [5, 3, 2, 1, 4]
sorted_array = bubble_sort(array)

print(sorted_array)
