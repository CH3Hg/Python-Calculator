print('==========Python Calculator v0.1==========')
print('by CH3Hg')
while True:
    try:
        num1=float(input('Please enter the first number:'))
        calculation_symbol=input('Please enter the calculation symbol(+ - * /):')
        num2=float(input('Please enter the second number:'))
        if calculation_symbol=='+':
            answer=num1+num2
            print('Answer:',answer)
        if calculation_symbol=='-':
            answer=num1-num2
            print('Answer:',answer)
        if calculation_symbol=='*':
            answer=num1*num2
            print('Answer:',answer)
        if calculation_symbol=='/':
            answer=num1/num2
            print('Answer:',answer)
        else:
            print('ERROR!(stop:0002)')
    except:
            print('ERROR!(stop:0001)')
