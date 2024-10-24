'''
Name: Quinton Fedora
Date: 10/24/24
Description: For loops
'''


#For loop style 1 - for in range(stop)
#this prints 0, 1, 2, 3, 4 each on their own line
#the number in range(stop) is how many nums are printed
#Starting at 0 and ending at stop-1

#common use: doing a known number of things.

for i in range(5):
    print(i)
print()
#or
#nums on the same line
for i in range(5):
    print(i,end=" ")
#or
print()

for i in range(5):
    print(i,end=", ")

print()

#for loop style 2 - for i in range(start, stop)
#this prints start, start+1, ......, stop-1
#loop runs stop-start number of times

for num in range(2,6):
    print("*"*num)

print(f"x|x^2")
print(f"------")
for num_to_square in range(1,6):
    print(f"{num_to_square} | {num_to_square**2}")
print(f"------")



#for loop style 3 - for i in range(start, stop, step)
#this prints start, start+1, ......, stop-1 but counts by step
#loop runs ceiling((stop-start)/step)times

for number in range(10,40,4): #want: 10 to 40 counting by 4s
    print(number, end = ", ")

# want: start at 12, count by 7s up to but not past 93
print()
for number in range(12,93,7):
    print(number, end = ", ")
print()
##############################

#print the sum of the numbers 1 through n

user_num = int(input("Give me a number: "))
sum = 0 #intialize our sum to 0
for num in range(1,user_num+1):
    sum = sum + num

print(f"The sum is {sum}")

#####################################

# 1) ask the user to enter 5 numbers
# 2) find the average of those numbers ( hunt: use a loop)
# 3) print "The average of your numbers is  ----"

