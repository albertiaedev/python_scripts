#Create a class with n number of students
print("Add the total students signed in to your class:\n")

i = 0
students = []

while 1:
        #Structure_Of_The_Counter                        
        i+=1
        student = input('\nEnter student name: ')
        if student == '':
                print("Done.")
                break
        students.append(student)
        print("Student added.\n")
        print(f"Number of students: {i}")
print(f"\nTotal students signed in: {i-1}")
print(f"\nStudents in your class:\n{students}\n")
