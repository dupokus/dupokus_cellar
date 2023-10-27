hex_numbers = {
    "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15
}

def hex_to_dec(hex_num:str)->str:
    for sym in hex_num:    
        if sym not in hex_numbers.keys():
            return "None"
    for sym in hex_num:
        if len(hex_num) == 3:
            print(f'{256*hex_numbers[sym]+16*(hex_numbers[hex_num[len(hex_num)-2]])+(hex_numbers[hex_num[len(hex_num)-1]])}')
            break
        elif len(hex_num) == 2:
            print(16*hex_numbers[sym] + (hex_numbers[hex_num[len(hex_num)-1]]))
            break
        else:
            print(hex_numbers[sym])



hex_to_dec("A")     # 10
hex_to_dec("0")     # 0 
hex_to_dec("1B")    # 27 
hex_to_dec("ABC")   # 2748
hex_to_dec("3C0")   # 960
hex_to_dec("ZZTOP") # none
hex_to_dec("A6G")   # none