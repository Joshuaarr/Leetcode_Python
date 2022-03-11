class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # 只有一个数字的情况
        if n == 1:
            return nums[0]
        # 不仅有一个数字的情况
        max_sol = cumsum = nums[0] # 初始值，最大解和连续和都为列表第一个数字
        for num in nums[1:]: #从第二个数字开始循环
            if cumsum < 0 and num > cumsum: #如果之前的和小于0且num大于此和，则由num开始
                cumsum = num
            else:
                cumsum += num
            max_sol = max(max_sol, cumsum) #每一步后更新最大值！！
        return max_sol