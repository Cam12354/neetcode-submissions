class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        target_count = Counter(s1)
        window_count = Counter()

        for i,char in enumerate(s2):
            window_count[char] += 1

            if i >= len_s1:
                left_char = s2[i - len(s1)]
                if window_count[left_char] == 1:
                    del window_count[left_char]
                else:
                    window_count[left_char] -= 1
            
            if window_count == target_count:
                return True
        return False


        #What is the invariant? what must the window satisfy? How can we identify a substring in this context
        #One way we can do that is by essentially asking whether or not a contiguous represention of s1 exists in s2

        #This is a fixed length problem, note we want to have a window size of len(s1)
        #If our window is 