class Solution {
    static isValid(s) {
        const stack = [];
        const closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{"
        };
        for (const c of s) {
            if (c in closeToOpen) {
                if (stack.length && stack[stack.length - 1] === closeToOpen[c]) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.length === 0;
    }
}

const s = "(){}}{";
console.log(Solution.isValid(s));
