class Solution {
    static SearchInsPos(values, target) {
        let output = 0;
        values.push(target)
        values.sort()
        console.log(values);
        for (let i = 0; i < values.length; i++) {
            if (values[i] === target) {
            output = i
            }
        }
        return output;
    }
}
const values = [1,2,4,5,6]
const target = 3
console.log(Solution.SearchInsPos(values, target)); // 2