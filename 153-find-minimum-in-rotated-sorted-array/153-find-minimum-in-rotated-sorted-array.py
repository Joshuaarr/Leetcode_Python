class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[r] >= nums[l]:
            return nums[l]
        while r > l:
            mid = (r + l)//2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        return nums[mid+1]
                