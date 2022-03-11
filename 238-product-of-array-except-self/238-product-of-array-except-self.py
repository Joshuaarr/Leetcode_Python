class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        i = 0
        product = [1] * len(nums)
        while i < len(nums) :
            product[i] = prefix
            prefix = prefix * nums[i]
            i += 1
        postfix = 1
        i = 1
        while i <= len(nums) :
            product[-i] = product[-i] * postfix
            postfix = postfix * nums[-i]
            i += 1
        return(product)