'''
Name: Quinton
Date: 10/22/24
Description: Unit 4 Lesson 1 - while loops

'''
'''
while some_condition is true:
    code to execute
    update variable (if forgotten -> infinite loop)
'''




start_number = 10
while start_number > 0:
    print(start_number)
    start_number = start_number - 1
    if start_number == 0:
        print(start_number)
        print("Blastoff!")

# change the code so it prints 10 9 8....0 Blastoff!!





while True:
    user_age = int(input("enter age or -1 to quit: "))
    if user_age == -1:
        break # exits the loop
    else:
        continue # return to the top of the loop