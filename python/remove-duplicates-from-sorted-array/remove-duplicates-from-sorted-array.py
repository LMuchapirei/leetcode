class Solution:
    def removeDuplicates(self, nums) -> int:
        i,j=0,1
        # do this as long as our left pointer has not crossed the right pointer and we are still within the bounds of our array
        while i<=j and j<len(nums):
            # check if we have duplicates that is two elements are the same
            if nums[i]==nums[j]:
                # advance our right pointer till we get to an element thats not a duplicate
                j+=1
            else:
                # if the element is not a duplicate , we swap it with the value thats at our right pointer
                nums[i+1]=nums[j]
                # we update our left pointer one step 
                i+=1
        return i+1
"""  
    [1,1,2,2,3,4,4,5]       i=0,j=1
    while i <= j (0<=1-->true) j<len(nums) (1<5----> true):
        first check succeeds run the block under first check
        j=2 
    [1,1,2,2,3,4,4,5]       i=0,j=2
    while i <= j (0<=2-->true) j<len(nums) (2<5----> true):
        first check failes nums[0](1) != nums[2](2)
        we get to else clause
        we update the last duplicates 1 with 2 ie nums[0+1](nums[1]-->nums[j]=nums[2]-->2) 
        we update i to 1 note j is still at two
    [1,2,2,2,3,4,4,5]       i=1,j=2
    while i <= j (1<=2 ---> true) j<len(nums) (2<5 ---> true)
        first check succeeds and we update j to 3
    [1,2,2,2,3,4,4,5]       i=1,j=3
    while passes
        first check pass  nums[1](2)==nums[3](2)
        update j to 4
    [1,2,2,2,3,4,4,5]       i=1,j=4
    while passes
        first check fails nums[1](1)!=nums[4](3)
        execute else
        set nums[i(1)+1] to nums[4]
        update i to i+1 
    [1,2,3,2,3,4,4,5]       i=2,j=4
    while passes
        first check succeeds nums[2](3)==nums[4](3)
        update j = 5
    [1,2,3,2,3,4,4,5]       i=2,j=5
    while passes
        first check failes nums[2](3)!=nums[5](4)
        swap nums[i+1] with nums[5]
        i incremented to i+1 ->3
    [1,2,3,4,3,4,4,5]       i=3,j=5
        while passes
        first check passes nums[3](4)==nums[5](4)
        increment j to 6
    [1,2,3,4,3,4,4,5]       i=3,j=6
        while passes
        first check passes nums[3](4)==nums[6](4)
        increment j to 7
    [1,2,3,4,3,4,4,5]       i=3,j=7
        while passes
        first check failes nums[3](4)!=nums[7](5)
        swap nums[i+1] with nums[7]
        increment i by 1 to 4
    [1,2,3,4,5,4,4,5]       i=4,j=7
        while passes
        first check passes nums[4](5)==nums[7](5)
        increment j to 8
    [1,2,3,4,5,4,4,5]
        while failes and then we return i+1(5)
    [1,2,3,4,5] is the unduplicated section that will be evaluated by the judge
"""