def threeSum(nums):
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        l,r = i + 1,len(nums)-1
        # check if the two numbers are equal if yes jump to next iteration
        if i > 0 and a != nums[i-1]:
            continue
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a,nums[l],nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    
    return res
