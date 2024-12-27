class Solution(object):
    def maxScoreSightseeingPair(self, values):
        n = len(values)
        previous = values[0] + 0
        maxi = 0
        for j in range(1, n):
            maxi = max(maxi, previous + values[j] - j)
            previous = max(previous, values[j] + j)
        return maxi

values = [8,1,5,2,6]
solution = Solution()
print(solution.maxScoreSightseeingPair(values))