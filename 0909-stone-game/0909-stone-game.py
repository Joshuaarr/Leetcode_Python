class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # find maximum point for alice
        visited = {}
        def helper(l, r):
            if (l, r) in visited:
                return visited[(l, r)]

            # base case
            if (
                l >= r or
                l < 0 or
                r >= len(piles)
                ):
                return 0

            # take left/right
            visited[(l, r)] = max(piles[l] + helper(l + 1, r), piles[r] + helper(l, r - 1))
            return visited[(l, r)]
        
        return helper(0, len(piles) - 1) > sum(piles) / 2
