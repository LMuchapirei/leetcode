class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        # Pick the first word,and then for each character in this word,check if the current character in the first string matches all the string 
        # if it does add it to the current result we are building
        for i in range(len(strs[0])):
            for s in strs:
                # guard for when the current string is now out of bounds,so we return the current prefix we have mad so far
                # otherwise append it given that it has matched the rest of the strings
                if i==len(s) or s[i]!=strs[0][i]:
                    return res
            res += strs[0][i]
        return res