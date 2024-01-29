class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target) 
        for index, value in enumerate(nums):
            if target < value:
                return index
        return len(nums)
        