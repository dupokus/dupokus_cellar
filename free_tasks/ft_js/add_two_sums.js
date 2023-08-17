class Solution {
    static addTwoNumbers(l1, l2) {
        const result = [];
        for (let i = 0; i < 3; i++) {
            result.push(l1[i] + l2[i]);
        }
        if (result[0] >= 10) {
            result[0] -= 10;
            result[1] += 1;
        } else if (result[1] >= 10) {
            result[1] -= 10;
            result[2] += 1;
        }
        return result;
    }
}

const list1 = [1, 6, 2];
const list2 = [3, 5, 1];
console.log(Solution.addTwoNumbers(list1, list2));
