# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.
# Example:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
# In this case, 6 units of rain water (blue section) are being trapped.




class Solution:
    def trap(self, height):
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]  # Update left_max
                else:
                    water += left_max - height[left]  # Add trapped water
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]  # Update right_max
                else:
                    water += right_max - height[right]  # Add trapped water
                right -= 1

        return water