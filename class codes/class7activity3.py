print("Enter marks obtained in 5 subjects")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
average = tot / 5

if average >= 91 and average <= 100:
    print(" your grade is A1")
elif average >= 81 and average < 91:
    print("your grade is A2")
elif average >= 71 and average <81:
    print(" your grade is B1")
elif average >= 61 and average > 71:
    print("your grade is B2")
elif average >= 51 and average < 61:
    print("your grade is C1")
elif average >= 41 and average < 51:
    print("your grade is C2")
else:
    print("Invalid input!")
