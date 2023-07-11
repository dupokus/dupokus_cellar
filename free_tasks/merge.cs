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
            int[] firstArray = new int[3] { 1, 2, 3 };
            int lengthOfFirstArray = firstArray.Length;
            int[] secondArray = new int[3] { 2, 5, 6 };
            int lengthOfSecondArray = secondArray.Length;
            Console.WriteLine(newProgram.Merge(firstArray, lengthOfFirstArray, secondArray, lengthOfSecondArray));
        }
        public int[] Merge(int[] nums1, int m, int[] nums2, int n)
        {
            Array.Resize(ref nums1, m + n);
            nums2.CopyTo(nums1, m);
            Array.Sort(nums1);
            return nums1;
        }
    }
}
