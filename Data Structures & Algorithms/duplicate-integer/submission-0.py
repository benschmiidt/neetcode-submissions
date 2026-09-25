class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenMap = set()
        for i in nums:
            if i in seenMap:
                return True
            seenMap.add(i)
        return False