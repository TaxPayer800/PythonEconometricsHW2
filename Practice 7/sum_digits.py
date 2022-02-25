def sum_digits():
    num = input ('Enter an integer number')
    total=0
    for digit in range(len(num)):
        total=total+int(num[digit])
    return total    
    
