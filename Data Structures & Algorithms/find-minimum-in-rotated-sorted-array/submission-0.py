class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2 #mid = 5 + 0 //2 = 2, nums[mid] == 5, left = mid + 1 = 3
            #mid = 4, nums[mid] = 1, nums[right] = 2, right = 4 nums[right] = 1
            
            if nums[mid] > nums[right]:
                #min is in the right half
                left = mid+1
            else:
                #min is in the left half including min
                right = mid

        return nums[left]
        