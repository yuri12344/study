"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_group = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word in anagrams_group:
                anagrams_group[sorted_word].append(word)
            else:
                anagrams_group[sorted_word].append(word)
        return [_ for _ in anagrams_group.values()]
            
"""
Explanation: first I thought, group the anagrams with dictionary, and append the words, using the default dict 
for skip key error.

The append the value, into the key of the dictionary, with list. And for each value, return a list of this values
"""