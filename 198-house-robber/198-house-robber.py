class Solution:
    def rob(self, nums: List[int]) -> int:
        lis = [0] * (len(nums) + 2)
        
        for i in range(len(nums) - 1, -1, -1):
            lis[i] += max(lis[i + 2::]) + nums[i]
        
        return(max(lis))