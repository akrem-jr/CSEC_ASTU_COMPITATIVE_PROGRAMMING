
class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        end = len(height) - 1
        max_area = 0

        while first < end:
            
            area = min(height[first], height[end]) * (end - first)
            max_area = max(area, max_area)

            if height[first] < height[end]:
                first += 1
            else:
                end -= 1

        return max_area
