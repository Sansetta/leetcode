from itertools import count


class Solution(object):
    def areAlmostEqual(self, s1, s2):
        count_matches = 0
        for i in range(len(s1)):
            if s1.count(s1[i]) == s2.count(s1[i]):
                if s1[i] != s2[i]:
                    count_matches += 1
            else:
                return False
        if count_matches <= 2:
            return True
        return False

s1 = "abca"
s2 = "abcc"
solve = Solution()
print(solve.areAlmostEqual(s1, s2))
