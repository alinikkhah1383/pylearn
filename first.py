#hi im starting python3 codding this is a description of my progress
print("Hi this is an script for find some num is can be division by 2, 3, 4, 5 or 6 or not ?")

#get number and change from str to float number
x = input("enter your number :")
y = float(x)

#check the number can division
if y % 6 == 0:
  print("it can be number 6")
elif y % 5 == 0:
  print("it can be number 5")
elif y % 4 == 0:
  print("it can be number 4")
elif y % 3 == 0:
  print("it can be number 3")
elif y % 2 == 0:
  print("it can be number 2")

#if number can't division then this code start working
else:
  print("it can't division numbers 2, 3, 4, 5 & 6")

