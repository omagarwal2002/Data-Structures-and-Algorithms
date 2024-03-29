'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3'''

import math
def majorityElement(nums):
    for i in list(set(nums)):
        if nums.count(i) > math.floor(len(nums)/2):
            return i
    return -1

print(majorityElement([3,2,3])) 