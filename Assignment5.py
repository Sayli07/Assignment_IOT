#The marks obtained by a student in 3 different subjects are input by the user. 
#Your program should calculate the average of subjects and display the grade. 
#The student gets a grade as per the following rules:
#Average Grade
#90-100 A
#80-89 B
#70-79 C
#60-69 D
#0-59 F


m1=int(input("Enter marks in subject1: "))
m2=int(input("Enter marks in subject2: "))
m3=int(input("Enter marks in subject3: "))

avg=(m1+m2+m3)/3
print(f"Avg={avg}")

if(90.0<=avg<=100.0):
    print("Grade A")
elif(80.0<=avg<=89.0):
    print("Grade B")
elif(70.0<=avg<=79.0):
    print("Grade C")
elif(60.0<=avg<=69.0):
    print("Grade D")
else:
    print("Grade F")  
      



