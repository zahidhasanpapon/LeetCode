## Approach 1. Brute Force

### Algorithm

We can think of a brute force approach. (1) Loop through each element x and find if there is another value that eqaults to target - x. (2) Or, Loop through each element x and find if there is another value y, that sums x + y = target.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # if nums[j] == target - nums[i]
                if nums[i] + nums[j] == target:
                    return [i, j]
```

### Complexity Analysis

- Time Complexity: O(n^2). For each element, we try to find its compliment by looping through the rest of the array which takes O(n) time. Therefore, the time complexity is O(n^2).
- Space Complexity: O(1). The space required does not depend on the size of the input array, so only constant space is used.
