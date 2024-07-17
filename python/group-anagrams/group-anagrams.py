

from collections import defaultdict


def groupAnagrams(strs):
    res = defaultdict(list) # mapping charCount  to List of Anagrams

    for s in strs:
        count = [0] * 26 # from a ... z
        for c in s:
            count[ord(c)-ord("a")] += 1
        res[tuple(count)].append(s)
    
    return res.values()

vals = groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(vals)