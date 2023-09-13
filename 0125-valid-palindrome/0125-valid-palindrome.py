class Solution:
    def isPalindrome(self, s: str) -> bool:
        isLower = s.lower()

        alphaNum = ""
        for ch in isLower :
            if ch.isalnum() :
                alphaNum += ch

        startPTR = 0 
        endPTR = len(alphaNum) - 1

        while startPTR < endPTR :
            if alphaNum[startPTR] != alphaNum[endPTR] :
                return False

            startPTR += 1
            endPTR -= 1

        
        return True