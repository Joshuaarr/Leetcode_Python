'''
Dynamic Programming using Depth First Search
Start at the last index to the first one
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Using another list to save the maxlen of the number
        # lis and nums shares the same index
        lis = [1] * len(nums)
        
        # Start from the last one, one left till reach posi 0
        for i in range(len(nums) + 1, -1, -1):
        # Search through any number behide nums[i], and larger then it
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    lis[i] = max(lis[i], 1 + lis[j])
                    
        return max(lis)