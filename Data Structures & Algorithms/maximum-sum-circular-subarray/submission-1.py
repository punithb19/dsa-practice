class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax, curMin = 0, 0
        globalMax, globalMin = nums[0], nums[0]
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        return max(globalMax, total-globalMin) if globalMax > 0 else globalMax