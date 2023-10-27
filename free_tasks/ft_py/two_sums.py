class Solution:
    nums = [2, 7, 11, 15]
    target = 9
    def two_Sum(nums, target):     
        prev_dict = {} # значення: індекс
        for i, n in enumerate(nums): # індекс та число в проіндексованому списку
            diff = target - n 
            if diff in prev_dict: 
                return [prev_dict[diff], i]
            prev_dict[n] = i # заповнення словника
        return
    print(two_Sum(nums, target))