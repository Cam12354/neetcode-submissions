class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Use a two-pointer approach, essentially we would have one pointer at the beginning and one pointer at the end. 
        #Then we would take the area of the the two bars that form a container -> Area =  height * length (We want high Height values and heigh length values)
        #We also have to ensure our area forms a container -> if left pointer is less than the right pointer, height = left and our length = right - left
        #When left pointer is greater than the right pointer, we want to height = right and length = right - left
        #maxArea = 1 * 7 = 7 if left pointer < right pointer, then we actually want to move our left pointer because we are seeking high values, else move right pointer.
        #Now we check our max area, we say okay, what is that max area between our current area and our current maxArea
        #At the end of our algorithm we return maxarea 
    
        #1 < 6, thus height = 1 and length = right - left = 7, and thus area = 1 * 7 = 7
        #maxAREA =  max(maxAREA, area)
        #7 > 6, thus height = 6 and length = right - left = 6, thus area = 6 * 6 = 36
        #maxArea
        #7 > 3, thus height = 3 and length = right - left = 5, thus area = 3 * 5 = 15
        #maxArea
        #7 > 7, height = 7 and length = right - left = 4, area = 7 * 4 = 28
        #maxArea

        maxAREA = 0
        left = 0
        right = len(heights)-1
        length = 0
        height = 0

        while left < right:
            if heights[left] < heights[right]:
                height = heights[left]
                length = right - left
                area = height * length
                left += 1
            else:
                height = heights[right]
                length = right - left
                area = height * length
                right -= 1

            maxAREA = max(maxAREA, area)
            
        return maxAREA
            


