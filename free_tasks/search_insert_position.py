class Solution:
    nums = [1,3,6]
    target = 7
    def searchInsert(nums, target: int) -> int:
        for i in range(len(nums)): 
            if target == nums[i]: 
                return i
            else: 
                nums.append(target)
                nums.sort()
                for i in range(len(nums)):
                    if target == nums[i]: 
                        return i
    print(searchInsert(nums, target))