class Solution:
    x = 1221
    def isPalindrome(x: int) -> bool:
        use_x = x 
        if x <= 0:
            return False
        reversed_num = 0
        while use_x != 0:
            digit = use_x % 10
            reversed_num = reversed_num * 10 + digit
            use_x //= 10
        if x == reversed_num:
            return True
    print(isPalindrome(x))    