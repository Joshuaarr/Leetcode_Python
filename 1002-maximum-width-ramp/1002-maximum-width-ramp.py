class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:

        # keep index in stack with num in descending order
        stack = []
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= nums[stack[-1]]:
                res = max(res, i - stack.pop())
        
        return res



            
            
