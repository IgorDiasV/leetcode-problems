def singleNumber(self, nums: List[int]) -> int:
    unique_numbers = list(set(nums))
    sum_unique_numbers = sum(unique_numbers)
    sum_nums = sum(nums)

    return sum_unique_numbers*2 - sum_nums