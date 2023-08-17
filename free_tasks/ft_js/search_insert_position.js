class Solution {
    static searchInsert(nums, target) {
        for (let i = 0; i < nums.length; i++) {
            if (target === nums[i]) {
                return i;
            } else {
                nums.push(target);
                nums.sort((a, b) => a - b);
                for (let i = 0; i < nums.length; i++) {
                    if (target === nums[i]) {
                        return i;
                    }
                }
            }
        }
    }
}

const nums = [1, 3, 6];
const target = 7;
console.log(Solution.searchInsert(nums, target));
