static bool CheckDuplicate(int[] nums)
        {

            Dictionary<int, int> countDict = new Dictionary<int, int>();
            foreach (int num in nums)
            {
                if (countDict.ContainsKey(num))
                {
                    countDict[num]++;
                }
                else
                {
                    countDict[num] = 1;
                }
            }
            foreach (int value in countDict.Values)
            {
                if (value > 1) 
                {
                    return true;
                }
            }
            return false;

        }