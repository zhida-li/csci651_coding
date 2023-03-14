# Reversing an array

"""
In this example, the reverse_array function takes an array arr, 
a starting index start, and an ending index end. 
The function swaps the values at start and end, and then 
recursively calls itself with start + 1 and end - 1 until start is greater than or equal to end.
"""
def reverse_array(arr, start, end):
    if start >= end:
        return 
    arr[start], arr[end] = arr[end], arr[start]
    # tmp = arr[start]  # other way
    # arr[start] = arr[end]
    # arr[end] = tmp

    print(f'index ({start}, {end}):', arr[start], arr[end])
    print(f'current arr: {arr}')

    reverse_array(arr, start + 1, end - 1)  # recursion

# Here's an example of how to reverse an array iteratively in Python:
def reverse_array_iter(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1  # 2 pointers 
        end -= 1  # 2 pointers 


# Here's how you could use the reverse_array function to reverse an array:
arr = [1, 2, 3, 4, 5]
reverse_array(arr, 0, len(arr) - 1)
print(arr)  # Output: [5, 4, 3, 2, 1]

"""
In this example, we start with the array [1, 2, 3, 4, 5], 
and call reverse_array with start=0 and end=4 
(the indices of the first and last elements in the array). 
The function swaps the values at start=0 and end=4, 
resulting in the array [5, 2, 3, 4, 1]. 
Then, it recursively calls itself with start=1 and end=3, 
swapping the values at start=1 and end=3 to get the array [5, 4, 3, 2, 1]. 
Finally, the function returns, and the reversed array is printed to the console.
"""


