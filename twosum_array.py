class Solution:
    def twoSum(self, nums:list[int], target):
        seen = {}  # value -> index
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i

# explanation
# nums = [2, 7, 11, 15]
# target = 9

# Step 1: i=0, num=2 → diff=7 → not in dict → store {2:0}
# Step 2: i=1, num=7 → diff=2 → 2 is in dict → return [0,1]
