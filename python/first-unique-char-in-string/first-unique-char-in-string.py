from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # solution from neetcode
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        for i,c in enumerate(s):
            if count[c] == 1:
                return i
        return -1

        # # word - > list of indexes as a dictionary
        # my first solution
        # dic = {}
        # # "leetcode"
        # for i,c in enumerate(s):
        #     if c in dic:
        #         dic[c].append(i)
        #     else:
        #         dic[c] = [i]
        # # {"l":[0],"e":[1,2,7],"t":[3],"c":[4],"o":[5],"d":[6]}
        # minIdx = []
        # for key in dic.keys():
        #     val = dic[key]
        #     if len(val) == 1:
        #         indx = val[0]
        #         minIdx.append(val[0])
        # return min(minIdx) if len(minIdx) else -1