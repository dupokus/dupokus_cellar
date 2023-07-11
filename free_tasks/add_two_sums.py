class Solution:
    list1 = [1, 6, 2]
    list2 = [3, 5, 1]
    def addTwoNumbers(l1, l2):
        result = []
        for i in range(3):
            result.append(l1[i]+l2[i])
        if result[0] > 10:
            result[0]-= 10
            result[1]+=1
        elif result[1] > 10:
            result[1]-= 10
            result[2]+=1
        return result
    print(addTwoNumbers(list1, list2))