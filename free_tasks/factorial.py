def factorial(num):
    if type(num) == int and num > 0:
        result = 1
        while num > 1:
            result *= num
            num -= 1
        print(result)
    elif num == 0:
        print(1)
    else: print("None")
factorial(5)
factorial(6)
factorial(0)
factorial(-2)
factorial(1.2)
factorial('Spam spam spam spam spam')
