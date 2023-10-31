class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subList = []

        def helper(index, currSum):
            if (
                index >= len(candidates) or 
                currSum > target 
            ):
                return
            if currSum == target:
                res.append(subList.copy())
                return
            
            # yes this index
            subList.append(candidates[index])
            helper(index, currSum + candidates[index])
            

            # no this index
            subList.pop()
            helper(index + 1, currSum)
            
        
        helper(0, 0)
        return res
