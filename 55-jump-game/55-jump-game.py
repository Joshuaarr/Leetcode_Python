class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        dp[len(nums) - 1] = 1
        for i in range(len(nums) - 1, -1, -1):
            r = min(i + nums[i], len(nums))
            if 1 in dp[i:r + 1]:
                dp[i] = 1    
        return dp[0]