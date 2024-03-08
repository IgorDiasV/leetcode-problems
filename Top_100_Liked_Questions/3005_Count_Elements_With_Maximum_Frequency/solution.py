class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        map_values = {}
        max_value = 0
        for value in nums:
            qtd = nums.count(value)
            if map_values.get(qtd):
                map_values[qtd]+=1
            else:
                map_values[qtd]=1

            if qtd > max_value:
                max_value = qtd
        
        return map_values[max_value]