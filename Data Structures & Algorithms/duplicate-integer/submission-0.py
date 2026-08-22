class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        new_dict = {}

        for num in nums:
            if num in new_dict:
                return True

            new_dict[num] = True

        return False
        