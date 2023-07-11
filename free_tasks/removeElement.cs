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
        public int RemoveElement(int[] nums, int val)
        {
            int countOfinvalid = 0;
            for (int i = 0; i < nums.Length; i++)
            {
                if (nums[i] == val)
                {
                    nums[i] = 999;
                    countOfinvalid++;
                }
            }
            Array.Sort(nums);
            int returnVal = nums.Length - countOfinvalid;
            return returnVal;
        }
    }
}