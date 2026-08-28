class Solution:

    def encode(self, strs: List[str]) -> str:
        fullStr = ""
        for singleStr in strs:
            fullStr += singleStr
            fullStr += " "
        
        return fullStr


    def decode(self, s: str) -> List[str]:
        words = s.split()
        return words
