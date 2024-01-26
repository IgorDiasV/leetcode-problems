class Solution:
    def romanToInt(self, s: str) -> int:
        romam_numbers = {"I":1,
                         "V":5,
                         "X":10,
                         "L":50,
                         "C":100,
                         "D":500,
                         "M":1000}
        value = 0
        index = 0
        size_input = len(s)
        for number in s:
            if index == size_input:
                break
            value_index_current = romam_numbers[s[index]]
            if index == size_input - 1:
                return value + value_index_current
            else:    
                value_next_index = romam_numbers[s[index+1]]
                if value_next_index > value_index_current:
                    value += value_next_index - value_index_current
                    index+=2
                else:
                    value += value_index_current
                    index +=1
        return value