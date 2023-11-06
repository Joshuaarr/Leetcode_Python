# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        nodeCount = 0
        def helper(node):
            nonlocal nodeCount
            if not node:
                return (0, 0)
            sumTillNowL, countTillNowL = helper(node.left)
            sumTillNowR, countTillNowR = helper(node.right)

            sumTillNow = sumTillNowL + sumTillNowR + node.val
            countTillNow = countTillNowL + countTillNowR + 1
            
            if node.val == sumTillNow // countTillNow:
                nodeCount += 1
            
            return (sumTillNow, countTillNow)
        
        helper(root)
        return nodeCount