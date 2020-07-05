# Your function for calculating payment goes here

def mpay(x, y, z):
    y = y / 1200
    z = z * 12
    if y == 0:
        p = x / z
    else:
        p = (x * (y * ((1 + y) ** z))) / (((1 + y) ** z) - 1)
    return p

# Your function for calculating remaining balance goes here

def rpay(x, y, z, w):
    y = y / 1200
    z = z * 12
    if y == 0:
        p = x * (1 - w / z)
    else:
        p = (x * (((1 + y) ** z) - ((1 + y) ** w ))) / (((1 + y) ** z) - 1)
        return p

# Your main program goes here

x = float(input("Enter loan amount: "))
y = float(input("Enter annual interest rate (percent): "))
z = int(input("Enter loan duration in years: "))
w = 0
k = mpay(x, y, z)

print('LOAN AMOUNT:', int(x), 'INTEREST RATE (PERCENT):', int(y))
print('DURATION (YEARS):', z, 'MONTHLY PAYMENT:', int(mpay(x, y, z)))

while w == 0:
    w += 1
    g = 12 * w
    print('YEAR:', w, 'BALANCE:', int(rpay(x, y, z, g)), 'TOTAL PAYMENT', int(12 * w * k))
for i in range(1, z):
    w += 1
    g = 12 * w
    print('YEAR:', w, 'BALANCE:', int(rpay(x, y, z, g)), 'TOTAL PAYMENT', int(12 * w * k))
