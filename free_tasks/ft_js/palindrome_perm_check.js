class Solution {
    static PalCheck(val) {
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
                delete hashmap[key];
            }
        }
        console.log(Object.keys(hashmap).length);
        if (Object.keys(hashmap).length>1){
            return false
        } else {
            return true;
        }
    }
}
const val = "civic"; // outputs true
console.log(Solution.PalCheck(val));