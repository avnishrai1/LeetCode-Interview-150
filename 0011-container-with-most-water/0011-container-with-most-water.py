class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, result = 0, len(height) - 1, 0

        while l < r :
            area = (r - l) * min(height[l], height[r])
            result = max(result, area)

            if height[l] < height[r] :
                l = l + 1

            else :
                r = r - 1

        return result