from collections import Counter
import heapq


class Solution:

    ### Heep solution
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
    ### Bucket Sort equivalent method

    def topKFrequent2(self,nums,k):
        count = {}
        # ideally we have a frequency array that takes items matching a given count at a certain index
        # if the items are distinct they will fall in the bucket with count of 1
        # [1,2,3,4,5,6]
        # freq [[],[],[],[],[],[],[]] ignore the first index with value zero
        # freq [[],[1,2,3,4,5,6],[],[],[],[],[]] 
        # top 2 elements we will get all 6 elements
        # we iterate from the end (that is the top n elements will be those in higher count buckets)
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n,0) 
        for n, c in count.items():
            freq[c].append(n)
        res = []

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res

# solution with some commentary         
# class Solution:  
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums)+1)]
#         res = []
#         #count the elements up
#         for n in nums:
#             count[n] = count.get(n,0) + 1
#         #put the elements in appropriate bucket count (count is 2 put it in the buckct where count is 2)
#         for n,c in count.items():
#             freq[c].append(n)
#         # from the end of the freqeuncy list
#         for i in range(len(freq)-1,0,-1):
#             # get all element in a given bucket(match a certaion count that is at location i in the frequency array)
#             for n in freq[i]:
#                 # append them to the result
#                 res.append(n)
#                 # check we have reached the count of elements we are looking for return if so correct
#                 if len(res)==k:
#                     return res