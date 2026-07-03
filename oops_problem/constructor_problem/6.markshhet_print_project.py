class Marksheet:
    def __init__(self):
        self.name = []
        self.age = []
        self.marks = []
        self.grade = []

    def input_data(self):
        for i in range(5):
            print(f"\nEnter details of student {i + 1}")

            n = input("Enter student name: ")
            self.name.append(n)

            a = int(input("Enter age of student: "))
            self.age.append(a)

            m = int(input("Enter marks of student: "))
            self.marks.append(m)

            g = input("Enter grade of student: ")
            self.grade.append(g)

    def display(self):
        for i in range(5):
            print()
            print("=================================")
            print("Name  :", self.name[i])
            print("Age   :", self.age[i])
            print("Marks :", self.marks[i])
            print("Grade :", self.grade[i])
            print("=================================")
            print()


m = Marksheet()
m.input_data()
m.display()