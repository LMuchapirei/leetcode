def twoSum(nums, target):
    # [2,7,11,15] target = 9
    # hashmap { 2:0,7:1,11:3,15:4}
    # target-currentValue if its in hashmap return the index, and the current index we are at

    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if j !=i:
    #             if (nums[i] + nums[j]) == target:
    #                 return [min(i,j),max(i,j)] 
    mp = {}
    for i in range(len(nums)):
        val = target - nums[i]
        if nums[i] in mp:
            return [min(mp[nums[i]],i),max(mp[nums[i]],i)]
        else:
            mp[val] = i

print(twoSum([3,4,5,6],7))
print(twoSum([2,7,11,15],9))
print(twoSum([3,2,4],6))