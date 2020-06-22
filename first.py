#hi im starting python3 codding this is a description of my progress
print("Hi this is an script for find some num is can be division by 2 ,3 ,5 or 6 or not ?")
x = input("enter your number :")
y = int(x)
if y%6==0 :
  print("its can be number 6")
elif y%3==0 :
  print("its can be number 3")
elif y%2==0 :
  print("it can be number 2")
elif y%5==0 :
  print("it can by number 5")
else:
  print("it cant division numbers 2,3 & 6")