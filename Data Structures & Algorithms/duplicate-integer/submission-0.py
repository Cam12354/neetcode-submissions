class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #Edge cases: CASE where input size is 1 automatically true, and case where input size is 0, we return true


        # empty set, iterate through nums and for each nummber in our array we check if its in set, if not we add it to our set and we 
        
        # if that num is in our set, then we know that we have seen that number before and thus we return True.
        # if we finish the loop without returning false, then we know that every value appears only once
        # -> return False
        # Note: set/hashmap > array in this problem because of the O(1) lookup time due to their hashing properties.

        duplicate = set()

        for num in nums:
            if num not in duplicate:
                duplicate.add(num)
            else:
                return True
        return False