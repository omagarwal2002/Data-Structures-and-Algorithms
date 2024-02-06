'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]'''

def productExceptSelf(nums):
    n = len(nums)
    left = [1]*n
    for i in range(0, n-1):
        left[i+1] = left[i] * nums[i]
    for i in range(0, n-1):
        left[-1-i] *= left[0]
        left[0] *= nums[-1-i]
    return left

print(productExceptSelf([1,2,3,4])) 
        