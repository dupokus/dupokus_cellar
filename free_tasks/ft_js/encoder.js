class Solution {
    static Encode(input) {
        let res = ""
        let count = 1
        for (let i = 0; i < input.length; i++) {
            if (i < input.length - 1 && input[i] === input[i + 1]) {
                count++;
            } else {
                res+= input[i] + count;
                count = 1
            }    
        }
        console.log(res);
        return res;
    }
}
const input = "ATTTGC"
console.log(Solution.Encode(input)); // A1T3G1C1