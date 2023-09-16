class Solution:
    def isPalindrome(self, s: str) -> bool:
        #firstly convert all uppercase into lowercase
        isLower = s.lower()

        #secondly filter the alphanumeric values
        alphaNum = ""

        for ch in isLower :
            if ch.isalnum() :
                alphaNum += ch

        #finally check the string forwardly and backwardly
        startPTR = 0
        endPTR = len(alphaNum) - 1

        while startPTR < endPTR :
            if alphaNum[startPTR] !=  alphaNum[endPTR] :
                return False
            
            startPTR += 1
            endPTR -= 1

        return True

