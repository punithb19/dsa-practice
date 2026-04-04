class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub, curSum = nums[0], 0
        for num in nums:
            
            curSum = max(curSum + num, num)
            maxSub = max(maxSub, curSum)
        return maxSub