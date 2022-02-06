'''
33. Search in Rotated Sorted Array
    time complexity O(log(n))
'''


def search(nums, target):
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        if (left == right) and (nums[right] != target):
            return -1
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= target < nums[mid]:
            right = mid - 1
        elif nums[mid] < target <= nums[right]:
            left = mid + 1
        elif (nums[mid] > nums[right]) and ((nums[mid] < target) or (target <= nums[right])):
            left = mid + 1
        elif (nums[mid] < nums[left]) and ((target >= nums[left]) or (target < nums[mid])):
            right = mid - 1
        else:
            right = mid - 1

    return -1

