"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""

from itertools import islice

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = set(nums)
        frequency = {}
        for n in count:
            frequency[n] = nums.count(n)
        
        sorted_d = dict(sorted(frequency.items(), key=lambda x: x[1]))
        result = []

        for key, value in islice(sorted_d.items(), k):
            result.append(value)
        return result

"""
Explanation: Instead of iterating over the entire list, I just get a set count, and iterate in this values, and count the frequency
After this sorted by the value, and iterate over the sorted list, with limit of k
"""