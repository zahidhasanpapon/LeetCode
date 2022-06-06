class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = len(nums)
        nums.sort()
        result = ""
        for i in range(0, length):
            if nums[i] != i:
                result = i
                break
        if result == "":
            return length
        return result
        