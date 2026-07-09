class Solution:
    def maxArea(self, heights: List[int]) -> int:

        i, j, max_area = 0, len(heights)-1, 0

        while i < j:

            area = min(heights[i], heights[j]) * (j-i)

            max_area = max(area, max_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_area