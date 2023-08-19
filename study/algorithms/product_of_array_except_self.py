from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the numbers to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the numbers to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1
        for i in reversed(range(length)):
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer


"""
Explanation: this is not my implementation, my fist implementantio I got O(log N), which is not good, I mean, its not O(1)
but I need study this implementantion in order to understeand and recreate it in my way
"""

class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # This determine the size of the array to return
        prefix = [1]
        
        for i in len(nums):
            res[i] = prefix
            prefix *= nums[1]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    
"""
Why this code is better? We store the sufix (nothing more then result of every multiplication in the list)
After that, we iterate over the result of the sufix and multiply by the prefix, which is the result of the multiplication
"""