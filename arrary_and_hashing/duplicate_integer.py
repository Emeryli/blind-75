class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashSet = set()

        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False