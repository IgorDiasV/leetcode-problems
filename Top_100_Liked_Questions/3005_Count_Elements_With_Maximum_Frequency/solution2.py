class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cont = 1
        max_cont = 1
        frequency = 1
        nums.sort()
        last_value = nums[0]

        for value in nums[1:]:
            if value == last_value:
                cont+=1
            else:
                if  max_cont < cont:
                    max_cont = cont
                    frequency = cont
                elif max_cont == cont:
                    frequency += cont
                cont = 1
                last_value = value
        
        if  max_cont < cont:
            max_cont = cont
            frequency = cont
        elif max_cont == cont and frequency < len(nums):
            frequency += cont
        return frequency
