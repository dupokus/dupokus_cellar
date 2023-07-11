using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    /// <summary>
    /// factorial problem using cs
    /// </summary>

    internal class Program
    {
        static void Main(string[] args)
        {
            var newProgram = new Program();
        }
        public int RemoveDuplicates(int[] nums)
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
            int invalidCount = 0;
            // Replace duplicates with 999 in-place
            for (int i = 0; i < nums.Length; i++)
            {
                int num = nums[i];
                if (countDict[num] > 1)
                {
                    nums[i] = 999;
                    countDict[num]--;
                    invalidCount++;
                }
            }

            // Sort the array, keeping the duplicates (999) at the end
            Array.Sort(nums, (x, y) => (x == 999 && y != 999) ? 1 : (x != 999 && y == 999) ? -1 : 0);

            // Print the array
            foreach (int num in nums)
            {
                Console.WriteLine(num);
            }
            return nums.Length - invalidCount;
        }
    }
}