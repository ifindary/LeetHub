class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            k -= 1

            temp = max(gifts)

            gifts.remove(temp)
            gifts.append(math.floor(math.sqrt(temp)))

        return sum(gifts)