class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        substring = ""
        for i in s:
            if i in substring:
                if len(substring) > max_size:
                    max_size = len(substring)
                index = substring.index(i) + 1
                substring = substring[index:] + i
            else:
                substring += i
        
        if len(substring) > max_size:
            max_size = len(substring)
        
        return max_size