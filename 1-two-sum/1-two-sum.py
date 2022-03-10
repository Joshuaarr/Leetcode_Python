class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Using a map
        m = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in m :
                return[m[diff],i]
            else:
                m[n] = i
        