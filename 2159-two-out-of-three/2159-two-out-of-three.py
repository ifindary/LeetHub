class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        ans = []

        for num in nums:
            print(num, nums.count(num))
            if nums.count(num) >= 2 and not num in ans:
                ans.append(num)

        return ans