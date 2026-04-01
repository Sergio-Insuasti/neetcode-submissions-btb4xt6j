class Solution:
    def trap(self, height: List[int]) -> int:
        lWall, rWall = 0, 0
        n = len(height)
        maxLeft = [0] * n
        maxRight = [0] * n
        
        for i in range(n):
            j = -i - 1
            maxLeft[i] = lWall
            maxRight[j] = rWall
            lWall = max(lWall, height[i])
            rWall = max(rWall, height[j])

        summ = 0
        for i in range(n):
            potential = min(maxLeft[i], maxRight[i])
            summ += max(0, potential - height[i])
        return summ