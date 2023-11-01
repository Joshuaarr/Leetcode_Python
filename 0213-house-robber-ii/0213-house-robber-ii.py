class Solution:
    def rob(self, nums: List[int]) -> int:
        # Starting from index-0 till end - 1 
        # and starting from index-1 till end
        def helper(nums):
            record = [0] * (len(nums) + 2)
            for i in range(2, len(nums) + 2):
                record[i] = max(nums[i - 2] + record[i - 2], record[i - 1])
            return record[-1]
        
        return max(nums[0], helper(nums[1:]), helper(nums[0:(len(nums) - 1)]))