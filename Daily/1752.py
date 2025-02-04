class Solution(object):
    def check(self, nums):
        copy_nums = sorted(nums)
        for i in range(1, len(nums)+1):
            new_nums = copy_nums[-i:] + copy_nums[:-i]
            if new_nums == nums:
                return True
        return False
