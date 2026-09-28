class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left = 0
        nums.sort()
        while (left<len(nums)-1):
            right = left+1
            if (nums[left] == nums[right]):
                return True
            left += 1
        return False