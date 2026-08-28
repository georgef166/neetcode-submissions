class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        for current_t in t:
            isAnagramFlag = 0
            for current_s in s:
                if current_s == current_t:
                    isAnagramFlag = 1
            if isAnagramFlag == 0:
                return False
        return True
            
                