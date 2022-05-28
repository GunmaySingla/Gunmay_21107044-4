y = int(input('Enter year:'))
if y%4==0:
    print('Entered year is a leap year')
elif y/100==0 & y/400 == 0:
    print('Entered year is a leap year')
else:
    print('Entered year is not a leap year')   
        