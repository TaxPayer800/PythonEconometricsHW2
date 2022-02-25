def present_value(CF,N,r):
    total = 0
    for int(n) in range(1,N+1):
        pv = pv + CF / ((1+r)**n)
        total = total + pv
        return total

rate=float(input('Enter the annual interest rate'))
years =float(input('Enter the number of years'))
FV = float(input('CF amount'))
print('Current value:€', format(present_value(rate,years,FV), '.2f'))

    
