class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums) - 1
        while r >= 0 :
            if nums[r] == target:
                return r
            r -= 1
        return -1