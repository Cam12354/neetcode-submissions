class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0
        max_freq = 0
        max_len = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0) + 1
            max_freq = max(max_freq, freq[s[r]])

            while (r-l+1) - max_freq > k:  #invariant
                freq[s[l]] -= 1 #decrement the count of whatever char s[l] points to
                l += 1 #shrink window until we are valid

            max_len = max(max_len, r-l+1)

        return max_len