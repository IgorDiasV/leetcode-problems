class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {}
        for i, value in  enumerate(order):
            order_map[value] = i
        
        list_letters = []
        for value in s:
            pos = order_map.get(value, None)
            if pos is not None:
                list_letters.append((pos, value))
            else:
                list_letters.append((len(s), value))
        
        list_letters.sort()
        return "".join([value[1] for value in list_letters])