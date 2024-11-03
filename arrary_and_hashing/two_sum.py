from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevDict = {} # val : index
        for index, value in enumerate (nums):
            diff = target - value
            if diff in prevDict:
                return [prevDict[diff], index]
            prevDict[value] = index
        return 