"""
#Exam grade calculator
# Input exam mark from the keyboard
exam_mark = int(input("Enter the exam mark: "))

# Check if the mark is in the correct range
if 0 <= exam_mark <= 100:
    # Determine the grade based on the mark
    if 80 <= exam_mark <= 100:
        grade = 'A'
    elif 70 <= exam_mark <= 79:
        grade = 'B'
    elif 60 <= exam_mark <= 69:
        grade = 'C'
    elif 50 <= exam_mark <= 59:
        grade = 'D'
    else:
        grade = 'F'

    # Output the grade
    print(f"Your Grade is: {grade}")
else:
    # Output an error message for an invalid mark
    print("Error: Invalid exam mark. Please enter a mark between 0 and 100.")
"""

#Write a program that will input a exam mark from the keyboard.
exam_mark = int(input("Enter your exam mark: "))
#The program needs to find out the grade for that mark and then output that grade to the screen.
#The program should have the following grades:
#A  80 - 100
#B  70 - 79
#C  60 - 69
#D  50 - 59
#F  0 - 49
if exam_mark >= 80 and exam_mark <=100:
  print("Your grade is A")
elif exam_mark >=70 and exam_mark <=79:
  print("Your grade is B")
elif exam_mark >= 60 and exam_mark <=69:
  print("Your grade is C")
elif exam_mark >=50 and exam_mark <=59:
  print("Your grade is D")
elif exam_mark >=0 and exam_mark<=49:
  print("Your grade is F")
#The program should output an error message if the mark entered is not in the correct.
else:
  print("Error: Invalid Exam mark. Please enter a mark between 0 and 100.")
  
