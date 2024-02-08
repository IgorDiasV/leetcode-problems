class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        qtd_number = {}
        n = len(nums)//2
        if n == 0:
            return nums[0]
        for value in nums:
            if qtd_number.get(value):
                qtd_number[value] += 1
                if qtd_number[value] > n:
                    return value
            else:
                qtd_number[value] = 1