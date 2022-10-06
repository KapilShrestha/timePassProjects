x0 = int(input("Enter five digit number not starting from 0 and 9: "))

while x0 not in range(10000, 89999):
    print("Number not in range")
    x0 = int(input("Enter five digit number not starting from 0 and 9: "))

print("*******************************************************")
#prediction done by magician
x=x0-2

n = x
result = []
while n != 0:
    n, d = divmod(n, 10)
    result.append(int(d))
result.reverse()
#print (result)

result.insert(0,2)
#print (result)

def convert(list): # Converting integer list to string list and joining the list using join()
    listToNumber = int("".join(map(str, list)))
      
    return listToNumber
  
# Driver code
result = result
print("My prediction is : ", convert(result))
print("*******************************************************")

x1 = int(input("Enter five digit number not starting from 0 and 9: "))
while x1 not in range(10000, 89999):
    print("Number not in range")
    x1 = int(input("Enter five digit number not starting from 0 and 9: "))

print("*******************************************************")
y1=99999-x1 # magician's turn to pick
print("My turn to pick a number")
print(y1)
print("*******************************************************")

x2 = int(input("Enter five digit number not starting from 0 and 9: "))
while x2 not in range(10000, 89999):
    print("Number not in range")
    x2 = int(input("Enter five digit number not starting from 0 and 9: "))

print("x2:", x2)
print("*******************************************************")
y2=99999-x2 # magician's turn to pick
print("my turn to pick a number")
print(y2)
print("*******************************************************")
print("Adding your choose", x0, x1, x2, "and my choose", y1,y2)
sum = x0+x1+x2+y1+y2
print(sum)
print("*******************************************************")