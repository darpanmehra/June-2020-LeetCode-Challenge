"""
Largest Divisible Subset

Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if nums == []: return []
        nums.sort()
        res = []
        count = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    count[i] = max(count[i], count[j]+1)
        max_index = count.index(max(count))
        temp = nums[max_index]
        currentCount = count[max_index]
        for i in range(max_index, -1, -1):
            if temp % nums[i] == 0 and count[i] == currentCount:
                res.append(nums[i])
                temp = nums[i]
                currentCount -=1
        return res

