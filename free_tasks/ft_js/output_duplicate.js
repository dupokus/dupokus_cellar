class Solution {
    static DupOutput(val) {
        let hashmap = {}
        for (let i = 0; i < val.length; i++) {
            if (val[i] in hashmap) {
                hashmap[val[i]]++;
            } else {
                hashmap[val[i]] = 1;
        
            }    
        }
        console.log(hashmap);
        for (const key in hashmap) {
            if (hashmap[key] === 2) {
                return key;
            }
        }
    }
}
const val = [2,1,4,3,5,4];
console.log(Solution.DupOutput(val)); // 4