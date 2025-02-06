from _collections import defaultdict

class Solution(object):
    def tupleSameProduct(self, nums):
        count_variants = 0
        product_count = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                count_variants += 8 * product_count[product]
                product_count[product] += 1

        return count_variants
