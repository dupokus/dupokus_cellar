class Solution {
    static longestCommonPrefix(strs) {
        let res = "";
        for (let i = 0; i < strs[0].length; i++) {
            for (let s of strs) {
                if (i === s.length || s[i] !== strs[0][i]) {
                    return res;
                }
            }
            res += strs[0][i];
        }
        return res;
    }
}

const strs = ["wliwer", "flight", "fliw", "flinger", "fliod", "flicker"];
console.log(Solution.longestCommonPrefix(strs));
