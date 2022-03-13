class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxV = 0
        n = len(height)
        i = 0
        j = n - 1
        while i < n and j > 0:
            width = j - i
            if height[i] < height[j]:
                Volumn = height[i] * width
                i += 1
            else:
                Volumn = height[j] * width
                j -= 1
            maxV = max(maxV, Volumn)
        return maxV