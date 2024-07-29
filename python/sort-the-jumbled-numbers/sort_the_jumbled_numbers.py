

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

# Solution failed when handling ties or special edge case
# mapping =
# [8,2,9,5,3,7,1,0,6,4]

# nums =
# [418,4191,916,948,629641556,574,111171937,28250,42775632,6086,85796326,696292542,186,67559,2167,366,854,2441,78176,621,4257,2250097,509847,7506,77,50,4135258,4036,59934,59474,3646243,9049356,85852,90298188,2448206,30401413,33190382,968234660,7973,668786,992777977,77,355766,221,246409664,216290476,45,87,836414,40952]
# my output
# [77,45,87,50,621,186,418,7973,916,948,366,854,574,7506,221,6086,4191,4036,4257,78176,2167,2441,67559,40952,85852,59474,59934,28250,668786,355766,836414,509847,4135258,9049356,3646243,2448206,2250097,42775632,90298188,33190382,30401413,85796326,696292542,629641556,111171937,968234660,992777977,216290476,246409664]
# expected
# [77,77,45,87,50,621,186,418,7973,916,948,366,854,574,7506,221,6086,4191,4036,4257,78176,2167,2441,67559,40952,85852,59474,59934,28250,668786,355766,836414,509847,4135258,9049356,3646243,2448206,2250097,42775632,90298188,33190382,30401413,85796326,696292542,629641556,111171937,968234660,992777977,216290476,246409664]


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

        