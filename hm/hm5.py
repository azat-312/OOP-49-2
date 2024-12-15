def find_max(arr):

 max_value = arr[0]

 for item in arr:

    if item > max_value:

        max_value = item

 return max_value

my_list = [64, 34, 25, 12, 22, 11, 90]

max_element = find_max(my_list)

print("Максимальный элемент:", max_element)
# O(log n ) логорифмическая сложность