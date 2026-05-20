class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Initial thought process is two use two pointers
        #One at the front of the string and one pointing to towards the back
        #While left pointer is less than right pointer, we want to traverse the string and check if the values that the pointers point to match
        #We can call .lower() to make steady comparisons between strings (make sure we're comparing lower case vs lower case)
        #We can also call .isalnum() to check if we are on a alphanumeric character or not.
        #If we're not on an alphanumeric character then we skip that character and move on.

        l = 0
        r = len(s)-1

        while l < r:
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            elif s[l].isalnum() == False:
                l += 1
            elif s[r].isalnum() == False:
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
        return True

        #s = "tab a cat?"   l = t, r = ? l < r true, t != ? r -= 1
        #Now l = t, r = t. l < r still and l = a, r = a, thus they match again