class Solution:
    def rob(self, nums: List[int]) -> int:
        # [left, right, n[i], n[i + 1]]
        # Do House Robber I Twice
        def robhelper(nums):
            left, right = 0, 0
            temp = 0
            for n in nums:
                temp = max(left + n, right)
                left = right
                right = temp
            return right
        return max(nums[0] + robhelper(nums[2:-1]), robhelper(nums[1::]))