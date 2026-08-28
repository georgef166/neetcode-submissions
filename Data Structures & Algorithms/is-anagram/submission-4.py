class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        else:
            return False



        #Built in Hash Function
        #return Counter(s) == Counter(t)



        #Manual Hash Map Solution
        # if len(s) != len(t):
        #     return False

        # count_S, count_T = {}, {}

        # for i in range(len(s)):
        #     count_S[s[i]] = 1 + count_S.get(s[i], 0)
        #     count_T[t[i]] = 1 + count_T.get(t[i], 0)     
        # for c in count_S:
        #     if countS[c] != countT.get(c, 0):
        #         return False

        # return True       