class Solution {
    static isPalindrome(x) {
        let useX = x;
        if (x <= 0) {
            return false;
        }
        let reversedNum = 0;
        while (useX !== 0) {
            const digit = useX % 10;
            reversedNum = reversedNum * 10 + digit;
            useX = Math.floor(useX / 10);
        }
        return x === reversedNum;
    }
}

const x = 1221;
console.log(Solution.isPalindrome(x));
