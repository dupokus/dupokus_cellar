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
        public int Factorial(int num)
        {
            int res = 1;
            for (int i = num; i >1; i--)
            {
                res *= i;
            }
            return res;
        }
    }
}
