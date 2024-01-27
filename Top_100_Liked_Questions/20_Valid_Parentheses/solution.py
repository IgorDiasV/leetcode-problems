class Solution:
    def isValid(self, s: str) -> bool:
        dict_pairs = {"{": "}",
                      "(": ")",
                      "[": "]"
                      }

        inverted_dict_pairs = {"}": "{",
                               ")": "(",
                               "]": "["
                               }
        list_parentheses = []
        for i in s:
            if i in dict_pairs:
                list_parentheses.insert(0, i)
            else:
                open_parentheses = inverted_dict_pairs[i]
                if open_parentheses in list_parentheses:
                    if list_parentheses.index(open_parentheses) != 0:
                        return False
                    list_parentheses.remove(open_parentheses)
                else:
                    return False
        if len(list_parentheses) == 0:
            return True
        return False
