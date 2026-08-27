class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        items = list(hash_map.keys())

        items.sort(key=lambda x: hash_map[x], reverse=True)

        return items[:k]
        