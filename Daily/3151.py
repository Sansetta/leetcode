class Solution(object):
    def isArraySpecial(self, nums):
        truth_set = set()
        for i in range(len(nums) - 1):

            if self.is_parity(nums[i]) != self.is_parity(nums[i + 1]):
                truth_set.add(True)
            else:
                truth_set.add(False)

        if all(i for i in truth_set):
            return True
        return False

    def is_parity(self, num):
        if num % 2 == 0:
            print(num)
            print(True)
            return True
        return False

