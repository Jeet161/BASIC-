class person:
    def __init__(self,student_id,name,age,maths,english,science,social):
        self.student_id=student_id
        self.name=name
        self.age=age
        self.maths=maths
        self.english=english
        self.science=science
        self.social=social
        
    def display(self):
        print("\nstudent details:")
        print(f"student_id:{self.student_id}")
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"maths:{self.maths}")
        print(f"english:{self.english}")
        print(f"science:{self.science}")
        print(f"social:{self.social}")
        print("----------------------------")
        
class System:
    def __init__(self):
        self.person = []

    # -------------------------------
    # REGISTER NEW CUSTOMER
    # -------------------------------
    def register_person(self):
        print("\n---Registration ---")

        while True:
            student_id = input("Enter 6-digit Account Number: ")
            if student_id.isdigit() and len(student_id) == 6:
                break
            print("❌ Invalid ID! Must be exactly 6 digits.\n")
        
        name = input("Enter Customer Name         : ")
        age = int(input("Enter Age                : "))
        print("\n---enter marks---")
        maths=int(input("enter marks for maths              :"))
        english=int(input("enter marks for english          :"))
        science=int(input("enter marks for science          :"))
        social=int(input("enter marks for social            :"))
        
        student = person(student_id,name,age,maths,english,science,social )
        self.person.append(student)

        print("\n✅ person Registered Successfully!")

#   SEARCH

    def find_person(self, student_id):
        for student in self.person:
            if student.student_id == student_id:
                return student
        return None               

#UPDATE MARKS
    def update_marks(self):
        student_id=input("\nenter student ID :")
        student =self.find_person(student_id)
        if not student:
            print("❌ student Not Found!")
            return

        print("\n--- Update Menu ---")
        print("1. update maths")
        print("2. Update english")
        print("3. Update science")
        print("4. Update social")

        choice = input("Enter choice: ")
        if choice == "1":
            student.maths = int(input("Enter marks: "))
        elif choice == "2":
            student.english = int(input("Enter marks: "))
        elif choice == "3":
            student.science = int(input("Enter marks: "))
        elif choice == "4":
            student.social = int(input("Enter marks:"))
        else:
            print("❌ Invalid Choice!")
            return

        print("✅ Marks Updated Successfully!")

#check
   
    def check_marks(self):
        student_id = input("\nEnter ID Number: ")
        student = self.find_person(student_id)

        if student:
            print(f"\n Marks in maths    : {student.maths}")
            print(f"\n Marks in english  : {student.english}")
            print(f"\n Marks in science  : {student.science}")
            print(f"\n Marks in social   : {student.social}")
        else:
            print("❌ person Not Found!")
        
school = System()

while True:
    print("\n============= SYSTEM MENU =============")
    print("1. Register person")
    print("2. check marks")
    print("3.update marks")    
    print("4.exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        school.register_person()
    elif choice == "2":
        school.check_marks()
    elif choice == "3":
        school.update_marks()
    elif choice == "10":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
        