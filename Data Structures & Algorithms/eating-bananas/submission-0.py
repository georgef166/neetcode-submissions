class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            # in pile i, there is n bananas
            # h is number of hours you have to eat n bananas
            # k is bananas-per-hour eating rate
            # each hour, you may chose 1 pile of bananas and eat k bananas from that pile
            # if pile has less than k bananas, you can finish current pile only

            #return min k to eat all bananas within h hours

        # biggestPile = max(piles)
        # totalBananas = sum(piles)
        # minimumEatingRate = 1

        # for i, n in enumerate(piles):
        #     currentTimeLimit = h // len(piles)

        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1

        return res