class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Since sets allow us to are ordered and have unique values, we can check if the set of the array is equal to the original array
        #If it is, return true

        seen = set()
    
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
    
        return False
        