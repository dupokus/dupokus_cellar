class Solution {
    static InterCount(arr1, arr2) {
        let res = 0;
        for (let i = 0; i < arr1.length; i++) {
            if (arr2.includes(arr1[i])) {
                res++;
            } 
        }
        return res;
    }
}
const arr1 = [1, 2, 3, 4, 5, 6];
const arr2 = [4, 5, 6, 7];
console.log(Solution.InterCount(arr1, arr2)); // 3