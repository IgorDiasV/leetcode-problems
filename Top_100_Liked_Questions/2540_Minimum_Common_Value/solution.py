class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        cont1 = 0
        cont2 = 0
        size_nums1 = len(nums1)
        size_nums2 = len(nums2)
        while cont1<size_nums1 and cont2 < size_nums2:
        
            if nums1[cont1] == nums2[cont2]:
                return nums1[cont1]
            if nums1[cont1] > nums2[cont2]:
                if cont2 < size_nums2:
                    cont2+=1
            else:
                if cont1 < size_nums1:
                    cont1+=1
        
        return -1