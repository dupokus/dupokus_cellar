class Solution:
    val = 12
    def new_pal(val):
        string_val = str(val)
        reversed_string_val = string_val[::-1]

        final_val = val
        reversed_final_val = 0
        while final_val >= val and final_val != reversed_final_val:    
            string_final_val = str(final_val)
            reversed_string_final_val = string_final_val[::-1]
            reversed_final_val = int(reversed_string_final_val)
            if final_val > val and final_val == reversed_final_val:    
                return final_val
            else:
                final_val += 1
    print(new_pal(val))