#an script for find square root of a number

#print some txt about script
print('this script find square root of any number')

#get input of number
number = float(input('enter your number : ' ))

#square root of number 1 and 0
if (number == 0 or number == 1):
    guess = number

#square root of unknown number
else:
    guess = number / 2
    step = 0

    while ( abs(number - guess**2) > 0.001 ):
        step = step + 1
        print('you are in step -> ', step, ' and your guss is : ', guess)
        division = number / guess
        guess = (division + guess) / 2

#print export
print('square root is : ', guess)

