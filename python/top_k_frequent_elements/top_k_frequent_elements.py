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