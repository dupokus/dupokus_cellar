class Solution {
    static twoSum(nums, target) {
        const prevDict = {}; // значення: індекс
        for (let i = 0; i < nums.length; i++) {
            const n = nums[i];
            const diff = target - n;
            if (prevDict[diff] !== undefined) {
                return [prevDict[diff], i];
            }
            prevDict[n] = i; // заповнення словника
        }
        return;
    }
}

const nums = [2, 7, 11, 15];
const target = 9;
console.log(Solution.twoSum(nums, target));
