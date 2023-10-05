"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [_ for _ in s]
        t = [_ for _ in t]
        s.sort()
        t.sort()
        "".join(s)
        "".join(t)
        if s == t:
            return True
        else:
            return False

"""
Explanation:
I thought, if anagram is a word with same chacarects, but in different order, I can sort the strings and compare them.
"""