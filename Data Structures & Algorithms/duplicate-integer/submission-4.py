class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myNums = set(nums)
        return len(myNums) != len(nums)