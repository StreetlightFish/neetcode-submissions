class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_index = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if compliment in nums_to_index:
                j = nums_to_index[compliment]
                return [j, i]
            nums_to_index[num] = i

        return []
        