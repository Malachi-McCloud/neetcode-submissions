class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create dictionary
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # List/Array to hold our result:
        res = []
        # Now we need to find the keys with the most occurances
        for _ in range(k):
            # find the key with largest value
            max_key = max(count, key=count.get)
            # append the max_key
            res.append(max_key)

            # remove it so next iteration doesnt grab it:
            del count[max_key]
        return res
