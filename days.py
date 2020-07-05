time = int(input('enter the number : '))

day = time // 86400
z = time % 86400
hrs = z // 3600
y = z % 3600
mn = y // 60
sec = y % 60

print(day, 'days and', hrs, 'hours and', mn, 'min and', sec, 'seconde')
