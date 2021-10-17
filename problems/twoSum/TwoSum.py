from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # if nums[j] == target - nums[i]
                if nums[i] + nums[j] == target:
                    return [i, j]

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen = {}
#         for i, value in enumerate(nums):
#             remaining = target - nums[i]
#             if remaining in seen:
#                 return [i, seen[remaining]]
#             else:
#                 seen[value] = i
