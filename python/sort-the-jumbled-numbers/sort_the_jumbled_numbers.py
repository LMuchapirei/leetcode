

# def sortJumbled(mapping,nums):
#     pairs = []
#     for i,n in enumerate(nums):
#         n = str(n)
#         mapped_n = 0
#         for c in n:
#             mapped_n *= 10 # shift left by multiplying by 10
#             mapped_n += mapping[int(c)]  
#         pairs.append((mapped_n,i))
    
#     pairs.sort()

#     return [nums[p[1]] for p in pairs]

#with a math trickery
def sortJumbled(mapping,nums):
    pairs = []
    for i,n in enumerate(nums):
        mapped_n = 0
        base = 1
        if n == 0:
            mapped_n = mapped_n[n]
        while n > 0:
            digit = n % 10
            n = n // 10
            mapped_n += mapping[digit]  
            base *= 10
        pairs.append((mapped_n,i))
    
    pairs.sort()

    return [nums[p[1]] for p in pairs]

def sortJumbled2(mapping,nums):
     mpDict =[]
     for i,num in enumerate(nums):
        mpDict.append((relativeValue(mapping,num),i))
     mpDict.sort()
     return [ nums[p[1]] for p in mpDict]


def relativeValue(mappings,number):
    digits = [c for c in str(number)]
    res = ""
    for c in digits:
        res += f"{mappings[int(c)]}"
    return int(res)

# Solution failed when handling ties
# class Solution:
#     def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
#         mpDict = {}
#         for num in nums:
#             mpDict[num] = self.relativeValue(mapping,num)
#         sorted_dict = dict(sorted(mpDict.items(), key=lambda item: item[1]))
#         return sorted_dict.keys()
#     def relativeValue(self,mappings,number):
#         digits = [c for c in str(number)]
#         res = ""
#         for c in digits:
#             res += f"{mappings[int(c)]}"
#         return int(res)

        