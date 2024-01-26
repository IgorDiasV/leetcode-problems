class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_world = strs[0]
        longest_prefix = "" 
        for i in range(len(first_world)):
            substring = first_world[:i+1]
            for word in strs[1:]:
                if not substring in word[:i+1]:
                    return longest_prefix
            longest_prefix = substring
        return longest_prefix
