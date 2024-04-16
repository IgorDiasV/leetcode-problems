class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, value in enumerate(nums):
            if hashMap.get(value) is not None:
                return [hashMap.get(value), i]
            hashMap[target - value] = i 