class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #How can we identify a start of a sequence. if we can identify a start of a sequence IF n-1 is NOT in nums,
        #nums = [2, 20, 4, 10, 3, 4, 5]
        #Then our "starting values", are 2, 10, and 20 because when you subtract 1 from them they arent in nums
        #Checking if a val is in nums in O(n) time, so this suggests that we may want to use a set, Since we also don't need repetitive values
        #create a set of our nums, {2, 20, 4, 10, 3, 5}
        #then we can iterate through our nums, if n-1 is not in our set
        #Then we know its a starting sequence, then we can check if n+length is in our set, if it is we can increment hte counnt
        #if its not then we take the longest of our length and longestcount

        #we then want to set our currentvalue to n+1, then check if n+1 is in our set, if it is we increment
    
      

        setofnums = set(nums)
        longestcount = 0

        for n in nums:
            #check if its start of seq
            if (n-1) not in setofnums:
                length = 0
                while (n+length) in setofnums:
                    length += 1
                longestcount = max(length, longestcount)
        return longestcount

        


        

