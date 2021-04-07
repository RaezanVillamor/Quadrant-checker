#Question 4

#Tasks:
#prompt inputs (x and y)
#determine which quadrant they're in
#-------------------------------------

#Take in inputs
x = int(input("Please type in an x-coordinate"))
y = int(input("Please type in a y coordinate"))


#find all instances of being in quad1,quad2, quad3, quad4
#then find all instances of it being on the line or 0,0

if(x > 0 and y > 0):
    print("The point","(",x,",",y,")", "lies in the first quadrant")

elif(x < 0 and y > 0):
    print("The point","(",x,",",y,")", "lies in the second quadrant")

elif(x < 0 and y < 0):
    print("The point","(",x,",",y,")", "lies in the third quadrant")
    
elif(x > 0 and y < 0):
    print("The point","(",x,",",y,")", "lies in the fourth quadrant")

elif(x == 0 and y > 0 or x == 0 and y < 0 or y == 0 and x < 0 or y == 0 and x > 0):
    print("The point","(",x,",",y,")", "The point lies between two quadrants")

else:
    print("The point","(",x,",",y,")", "at the orgin")

    









