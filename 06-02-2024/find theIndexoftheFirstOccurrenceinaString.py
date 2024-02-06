'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.'''

def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1

print(strStr("sadbutsad", "sad"))