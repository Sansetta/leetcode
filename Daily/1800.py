class Solution(object):
    def maxAscendingSum(self, nums):
        local_sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                local_sum += nums[i]
                max_sum = max(max_sum, local_sum)
            else:
                local_sum = nums[i]

        return max_sum
