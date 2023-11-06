# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        record = {} #{sum: freq}
        maxFreq = 0

        def helper(node):
            nonlocal maxFreq
            if not node:
                return 0
            leftSum, rightSum = helper(node.left), helper(node.right)

            # update record
            currSum = leftSum + rightSum + node.val
            record[currSum] = 1 + record.get(currSum, 0)
            maxFreq = max(maxFreq, record[currSum])
            return currSum
        
        helper(root)

        res = []
        for key in record:
            if record[key] == maxFreq:
                res.append(key)
        
        return res

        