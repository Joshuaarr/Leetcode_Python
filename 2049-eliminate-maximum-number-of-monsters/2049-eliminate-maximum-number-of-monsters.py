class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        timeCost = [dist[i] / speed[i] for i in range(len(dist))]

        timeCost.sort()
        for t in range(len(dist)):
            if timeCost[t] <= t:
                return t
        
        return len(dist)