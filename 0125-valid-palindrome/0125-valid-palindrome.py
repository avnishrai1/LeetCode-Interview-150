class Solution:
    def isPalindrome(self, s: str) -> bool:
        #firstly convert all the uppercase into lowercase
        sLower = s.lower()
        
        #now remove all alphanumeric char
        alphaNum = ""
        for ch in sLower :
            if ch.isalnum() :
                alphaNum += ch

        #now compare forward and backward
        startSTR = 0
        endSTR = len(alphaNum) - 1

        while startSTR < endSTR :
            if alphaNum[startSTR] != alphaNum[endSTR] :
                return False

            startSTR += 1
            endSTR -= 1

        return True
