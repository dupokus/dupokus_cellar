class Solution:
    list1 = [1,1,1,2,3,4,4,5]
    def removeDuplicates(list1):
        unique_list = []
  
    # traverse for all elements
        for x in list1:
        # check if exists in unique_list or not
            if x not in unique_list:
                unique_list.append(x)
    # print list
        return unique_list
    print(removeDuplicates(list1))