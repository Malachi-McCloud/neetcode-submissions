class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        if len(nums) == 0:
            return False
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        max_key = max(count, key=count.get)
        print(max_key)
        if max(count.values()) > 1:
            return True
        return False