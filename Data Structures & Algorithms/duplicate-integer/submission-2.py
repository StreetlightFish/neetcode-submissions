class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashm = set()
        for item in nums:
            if item in hashm:
                return True
            hashm.add(item)

        return False