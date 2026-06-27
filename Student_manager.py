# Day 7 - Mini Project: Student Record Manager

students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = input("Enter marks: ")
        students[name] = marks
        print("Student added!")

    elif choice == "2":
        if not students:
            print("No records found")
        else:
            for name, marks in students.items():
                print(name, ":", marks)

    elif choice == "3":
        name = input("Enter name to search: ")
        if name in students:
            print(name, ":", students[name])
        else:
            print("Not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        if name in students:
            del students[name]
            print("Deleted")
        else:
            print("Not found")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
