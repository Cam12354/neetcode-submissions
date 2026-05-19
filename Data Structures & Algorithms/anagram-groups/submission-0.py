from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       res = defaultdict(list) #mappingCharCount to list of Anagrams

       for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch)-ord("a")] += 1
        
        res[tuple(count)].append(word) #in python, list cannot be keys

       return list(res.values())