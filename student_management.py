import json
import os

# ---------- Student Class ----------
class Student:
    def __init__(self, student_id, name, grade):
        self.id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "grade": self.grade
        }


# ---------- Student Manager Class ----------
class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = {}
        self.load_data()

    # Load students from file
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                self.students = json.load(file)
        else:
            self.students = {}

    # Save students to file
    def save_data(self):
        with open(self.filename, "w") as file:
            json.dump(self.students, file, indent=4)

    # Add student
    def add_student(self, student):
        if student.id in self.students:
            print("❌ Student ID already exists!")
            return
        self.students[student.id] = student.to_dict()
        self.save_data()
        print("✅ Student added successfully.")

    # Update student
    def update_student(self, student_id, name, grade):
        if student_id not in self.students:
            print("❌ Student not found!")
            return
        self.students[student_id]["name"] = name
        self.students[student_id]["grade"] = grade
        self.save_data()
        print("✅ Student updated successfully.")

    # Delete student
    def delete_student(self, student_id):
        if student_id not in self.students:
            print("❌ Student not found!")
            return
        del self.students[student_id]
        self.save_data()
        print("✅ Student deleted successfully.")

    # List students
    def list_students(self):
        if not self.students:
            print("📭 No student records found.")
            return

        print("\n📋 Student Records")
        print("-" * 40)
        print(f"{'ID':<10}{'Name':<20}{'Grade'}")
        print("-" * 40)

        for s in self.students.values():
            print(f"{s['id']:<10}{s['name']:<20}{s['grade']}")
        print("-" * 40)


# ---------- Main Menu ----------
def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")
            student = Student(sid, name, grade)
            manager.add_student(student)

        elif choice == "2":
            sid = input("Enter Student ID to update: ")
            name = input("Enter New Name: ")
            grade = input("Enter New Grade: ")
            manager.update_student(sid, name, grade)

        elif choice == "3":
            sid = input("Enter Student ID to delete: ")
            manager.delete_student(sid)

        elif choice == "4":
            manager.list_students()

        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()