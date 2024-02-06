'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.'''

def trap(height) :
    res, l, r, lmax, rmax = 0, 0 , len(height)-1, 0, 0
    if r<2: return res

    while l<r:
        if height[l]<height[r]:
            lmax = max(lmax, height[l])
            res+= lmax - height[l]
            l+=1
        else:
            rmax = max(rmax, height[r])
            res+= rmax - height[r]
            r-= 1

    return res

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) 