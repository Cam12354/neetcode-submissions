class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #How do we identify proper anagrams, how can we say that act is an anagram of cat?
        #Initially, Im thinking that the we can determine proper anagrams based off of the frequencies of the letters in the word
        #First note that our input is all lower case
        #We will need an empty list call it our result
        #If our character is in the hashmap, then we know that we've seen a word with this character before MEANING
        #We have a possible match, so then while the character frequency is the same then keep traversing and checking, if we
        #finish traversing the word and ALL the characters in the word have the same frequency map as another character, then we know we have an anagram match
        #If our character is not in the hashmap, then this is the first we're seeing this word.
        
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char)-ord('a')] += 1
            res[tuple(count)].append(string)
        return list(res.values())
            

        