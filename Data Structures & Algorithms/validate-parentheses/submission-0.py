class Solution:
    def isValid(self, s: str) -> bool:
        openedBracket = []
        closedBracket = []
        
        for bracket in s:
            if bracket == "[" or bracket == "{" or bracket == "(":
                openedBracket.append(bracket)
            else:
                closedBracket.append(bracket)
            
        if len(openedBracket) != len(closedBracket):
            return False

        i = 0
        while i < len(openedBracket):
            if openedBracket[i] == "[":
                if closedBracket[len(openedBracket) - 1 - i] != "]":
                    return False
            elif openedBracket[i] == "{":
                if closedBracket[len(openedBracket) - 1 - i] != "}":
                    return False
            elif openedBracket[i] == "(":
                if closedBracket[len(openedBracket) - 1 - i] != ")":
                    return False
            i+=1

        return True
        