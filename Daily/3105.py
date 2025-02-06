class Solution(object):
    def longestMonotonicSubarray(self, nums):
        max_increase = 1
        max_decrease = 1
        decrease = 1
        increase = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                increase += 1
                max_increase = max(increase, max_increase)
                decrease = 1

            elif nums[i] < nums[i + 1]:
                decrease += 1
                max_decrease = max(decrease,max_decrease)
                increase = 1

            else:
                increase = 1
                decrease = 1

        return max(max_increase,max_decrease)
