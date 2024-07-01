class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # makes sure we don't iterate through a substring that is shorter than needle
        for i in range(len(haystack)-len(needle)+1):
            # check if any substring of haystack with the same length as needle is equal to needle
            if haystack[i:i+len(needle)] == needle:
                return i
            
        # the underlying code of what is happening on the above slicing solution
        # for i in range(len(haystack)+1-len(needle)):
        #     for j in range(len(needle)):
        #         if haystack[i+j] != needle[j]:
        #             break
        #         if j == len(needle)-1:
        #             return i
        return -1