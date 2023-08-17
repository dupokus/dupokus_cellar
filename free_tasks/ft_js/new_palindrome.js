class Solution {
    static newPal(val) {
        const stringVal = val.toString();
        const reversedStringVal = stringVal.split('').reverse().join('');

        let finalVal = val;
        let reversedFinalVal = 0;

        while (finalVal >= val && finalVal !== reversedFinalVal) {
            const stringFinalVal = finalVal.toString();
            const reversedStringFinalVal = stringFinalVal.split('').reverse().join('');
            reversedFinalVal = parseInt(reversedStringFinalVal);

            if (finalVal > val && finalVal === reversedFinalVal) {
                return finalVal;
            } else {
                finalVal++;
            }
        }
    }
}

const val = 12;
console.log(Solution.newPal(val));
