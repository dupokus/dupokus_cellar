class Solution {
    static top3Words(text) {
        const result = {};
        const res = [];
        const punctuations = `!()-[]{};:'"\,<>./?@#$%^&*_~`;
        let refinedText = '';
        
        for (const char of text) {
            if (!punctuations.includes(char)) {
                refinedText += char;
            }
        }
        
        const sortedText = refinedText.toLowerCase().split(' ');
        
        for (const word of sortedText) {
            const cleanWord = word.replace(new RegExp(`[${punctuations}]`, 'g'), '');
            if (!result[cleanWord]) {
                result[cleanWord] = 0;
            } else {
                result[cleanWord]++;
            }
        }
        
        for (let i = 0; i < 3; i++) {
            if (Object.keys(result).length > 0) {
                const e = Object.keys(result).reduce((a, b) => result[a] > result[b] ? a : b);
                res.push(e);
                delete result[e];
            }
        }
        
        return res;
    }
}

const text = `  //wont won't won't`;
console.log(Solution.top3Words(text));
