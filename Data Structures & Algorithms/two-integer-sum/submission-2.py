class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}  # value -> index

        for i, elem in enumerate(nums):
            complement = target - elem
            if complement in seen_map:
                j = seen_map[complement]
                return [min(i, j), max(i, j)]
            seen_map[elem] = i

	