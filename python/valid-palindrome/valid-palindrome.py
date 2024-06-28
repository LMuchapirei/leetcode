class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(c for c in s.lower() if c.isalnum())
        if clean == "":
            return True
        l,r = 0,len(clean)-1

        while clean[l] == clean[r]:
            if l >= r:
                return True
            l,r = l+1,r-1
        return False