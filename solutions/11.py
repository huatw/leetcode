class Solution:
    def maxArea(self, height):
        res = 0
        left, right = 0, len(height)-1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            if area > res:
                res = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res



