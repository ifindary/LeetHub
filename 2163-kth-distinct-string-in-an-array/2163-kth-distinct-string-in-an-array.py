class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for words in arr:
            if words in count:
                count[words] += 1
            else:
                count[words] = 1

        singleCount = []
        order = 0

        for word in arr:
            if count[word] == 1:
                order += 1

                if order == k:
                    return word


        return ""

