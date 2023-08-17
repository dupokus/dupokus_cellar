class Solution {
    static removeDuplicates(list1) {
        const uniqueList = [];
        
        for (const x of list1) {
            if (!uniqueList.includes(x)) {
                uniqueList.push(x);
            }
        }
        
        return uniqueList;
    }
}

const list1 = [1, 1, 1, 2, 3, 4, 4, 5];
console.log(Solution.removeDuplicates(list1));
