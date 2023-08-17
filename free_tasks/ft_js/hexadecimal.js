const hexNumbers = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
};

function hexToDec(hexNum) {
    for (let i = 0; i < hexNum.length; i++) {
        if (!(hexNum[i] in hexNumbers)) {
            return "None";
        }
    }
    let result = 0;
    for (let i = 0; i < hexNum.length; i++) {
        const sym = hexNum[i];
        if (hexNum.length === 3) {
            result = 256 * hexNumbers[sym] + 16 * hexNumbers[hexNum[1]] + hexNumbers[hexNum[2]];
            break;
        } else if (hexNum.length === 2) {
            result = 16 * hexNumbers[sym] + hexNumbers[hexNum[1]];
            break;
        } else {
            result += hexNumbers[sym];
        }
    }
    console.log(result);
}

hexToDec("A");     // 10
hexToDec("0");     // 0
hexToDec("1B");    // 27
hexToDec("ABC");   // 2748
hexToDec("3C0");   // 960
hexToDec("ZZTOP"); // None
hexToDec("A6G");   // None
