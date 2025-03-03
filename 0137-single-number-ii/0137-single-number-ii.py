class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = defaultdict(int)

        for num in nums:
            cnt[num] += 1

        for key, value in cnt.items():
            if value == 1:
                return key

        return -1
        