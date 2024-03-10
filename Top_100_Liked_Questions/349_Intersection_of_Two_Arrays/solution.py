class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        intersections = []

        for value in nums1:
            if value in nums2:
                intersections.append(value)

        return intersections
        