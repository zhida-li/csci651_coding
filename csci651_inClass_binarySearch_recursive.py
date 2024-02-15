"""
704. Binary Search
https://leetcode.com/problems/binary-search/

"""

# recursive approach
def BinarySearchRecursive(nums, target, start, end):
    """
    :type nums: List[int]
    :type target: int
    :type start: int
    :type end: int
    :rtype: bool
    """
    if start > end:
        return False  # Base case: the target is not found

    mid = (start + end) // 2  # Calculate the middle index

    if nums[mid] == target:
        return True  # The target is found
    elif nums[mid] > target:
        return BinarySearchRecursive(nums, target, start, mid - 1)  # Search in the left half
    else:
        return BinarySearchRecursive(nums, target, mid + 1, end)  # Search in the right half

# Test cases
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(BinarySearchRecursive(nums, target, 0, len(nums) - 1))  # Output: True

target = 2
print(BinarySearchRecursive(nums, target, 0, len(nums) - 1))  # Output: False
