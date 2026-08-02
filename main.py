class Student:# Student

    def __init__(self, name, roll, course):
        self.name = name
        self._roll = roll
        self.course = course

    def get_roll(self):
        return self._roll

    def __eq__(self, other):
        return (
            isinstance(other, Student)
            and other._roll == self._roll
            and other.course == self.course
        )

    def __hash__(self):
        return hash((self._roll, self.course))

class Teacher: # Teacher

    def __init__(self, name, id, subject='General'):
        self.name = name
        self._id = id
        self.subject = subject

    def get_id(self):
        return self._id

    def set_subject(self, assigned_subject):
        self.subject = assigned_subject

class Library:

    def __init__(self, name, writer):
        self.name = name
        self.writer = writer

class School:

    def __init__(self):
        self.marks = {
            Student('student1', 1, 1): 50,
            Student('student1', 2, 1): 80
        }
        self.student = [Student('student1', 1, 1), Student('student2', 2, 1), Student('student3', 1, 2)]
        self.teacher = [Teacher('teacher1', 1, 'Bengali'), Teacher('teacher2', 2, 'English')]
        self.fund = 5000
        self.library = [Library('Animal Farm', 'George Orwel'), Library('Capital', 'Karl Marx')]
        self.hostel = []

    def check_student(self, student_roll, student_course): # Student
        for i in self.student:
            if i._roll == student_roll and i.course == student_course:
                return i

        return False

    def add_student(self,student_name, student_roll, student_course): # Student
        student = Student(student_name, student_roll, student_course)
        self.student.append(student)
        return True

    def remove_student(self, student_roll, student_course): # Student
        i = self.check_student(student_roll, student_course)
        if i:
            self.student.remove(i)
            return True

    def payment(self, student_roll, student_course, amount):# Student
        i = self.check_student(student_roll, student_course)
        if i:
            self.fund += amount
            return True

    def add_marks(self, student_roll, student_course, average_marks):# Student
        i = self.check_student(student_roll, student_course)
        if i:
            self.marks[i] = average_marks
            return True

    def result(self, average_marks):# Student
        if 33 > average_marks >= 0:
            return f'Accquired: C Grade '
        elif 70 > average_marks >= 33:
            return f'Accquired: B Grade '
        elif 80 > average_marks >= 70:
            return f'Accquired: A Grade '
        elif 100 > average_marks >= 80:
            return f'Accquired: A+ '
        else:
            return 'Failed'

    def show_result(self, student_roll, student_course):# Student
        i = self.check_student(student_roll, student_course)
        if i:
            with open('result.txt', 'w') as f:
                f.write(f'***Result of {i.name}, Roll: {i._roll}, Class: {i.course}***\n\n')
                f.write(f'    Average Mark is: {self.marks[i]}\n')
                f.write(f'    {i.name} is {self.result(self.marks[i])}')
            return True

    def check_teacher(self, teacher_id): # Teacher
        for i in self.teacher:
            if i._id == teacher_id:
                return i

        return False

    def add_teacher(self, teacher_name, teacher_id, assigned_subject): # Teacher
        teacher = Teacher(teacher_name, teacher_id, assigned_subject)
        self.teacher.append(teacher)
        return True

    def remove_teacher(self, teacher_id): # Teacher
        i = self.check_teacher(teacher_id)
        if i:
            self.teacher.remove(i)
            return True
        
        return False

    def subject_assign(self, teacher_id, assigned_subject): # Teacher
        i = self.check_teacher(teacher_id)
        if i:
            i.set_subject(assigned_subject)
            return True
        
        return False

    def provide_salary(self, teacher_id): # Teacher
        i = self.check_teacher(teacher_id)
        if i:
            self.fund -= 500
            return True

        return False

    def check_book(self, book_name, book_writer): # Library
        for i in self.library:
            if i.name == book_name and i.writer == book_writer:
                return i

        return False

    def add_book(self, book_name, book_writer): # Library
        i = self.check_book(book_name, book_writer)
        if not i:
            book = Library(book_name, book_writer)
            self.library.append(book)
            return True

        print('Invalid Input')
        return False

    def remove_book(self, book_name, book_writer): # Library
        i = self.check_book(book_name, book_writer)
        if i:
            self.library.remove(i)
            return True

        print('Book not found')
        return False

    def fine(self, amount): # Library
        self.fund += amount
        return True



if __name__ == '__main__':

    school = School()

    while True:

        print("""
1. Student
2. Teacher
3. Library
""")

        choice =  input('Choose : ')

        if choice == '1': # Student


            print("""
1. Add Student
2. Remove Student
3. Payment
4. Add Marks
5. Show Result
            """)

            choice2 = input('Choose : ')

            if choice2 == '1':
                student_name = input('Name: ')
                student_roll = int(input('Roll: '))
                student_course = int(input('Assigned Class (1 - 5) : '))
                if school.add_student(student_name, student_roll, student_course):
                    print('Student Added Successfully..!')
                else:
                    print('Invalid input..')

            elif choice2 == '2':
                student_roll = int(input('Roll: '))
                student_course = int(input('Assigned Class (1 - 5) : '))
                if school.remove_student(student_roll, student_course):
                    print('Student removed Successfully..!')
                else:
                    print('Student not found.')

            elif choice2 == '3':
                student_roll = int(input('Roll: '))
                student_course = int(input('Assigned Class (1 - 5) : '))
                amount = int(input('Payment Amount.. = '))
                if school.payment(student_roll, student_course, amount):
                    print('Payment successfull')
                else:
                    print('Payment failed, Please try again....')

            elif choice2 == '4':
                student_roll = int(input('Roll: '))
                student_course = int(input('Assigned Class (1 - 5) : '))
                average_marks = int(input('Average Marks.. = '))
                if school.add_marks(student_roll, student_course, average_marks):
                    print('Marks added successfully')
                else:
                    print('Student not Found')

            elif choice2 == '5':
                student_roll = int(input('Roll: '))
                student_course = int(input('Assigned Class (1 - 5) : '))
                if school.show_result(student_roll, student_course):
                    print('Result Generated Successfully, Please check the file result.txt')
                else:
                    print('Student not Found')

        elif choice == '2': # Teacher

            print('''
1. Add Teacher
2. Remove Teacher
3. Subject Assign
4. Provide Salary
''')
            choice2 = input('Choose: ')

            if choice2 == '1':

                teacher_name = input('Name: ')
                teacher_id = int(input('ID: '))
                assigned_subject = input('Subject: ')
                if school.add_teacher(teacher_name, teacher_id, assigned_subject):
                    print('Added Successfully')
                else:
                    print('Invalid input')

            elif choice2 == '2':

                teacher_id = int(input('ID: '))
                if school.remove_teacher(teacher_id):
                    print('Removed')
                else:
                    print('Teacher not Found')

            elif choice2 == '3':
                teacher_id = int(input('ID: '))
                assigned_subject = input('Subject: ')
                if school.subject_assign(teacher_id, assigned_subject):
                    print('Assigned')
                else:
                    print('Teacher not Found')

            elif choice2 == '4':
                teacher_id = int(input('ID: '))
                if school.provide_salary(teacher_id):
                    print('Provided')
                else:
                    print('Teacher Not found')

        elif choice == '3': # Library

            print('''
1. Add Book
2. Remove Book
3. Borrow
4. Return
5. Fine
''')
            choice2 = input('Choose: ')

            if choice2 == '1':
                book_name = input('Name: ')
                book_writer = input('Writer: ')
                if school.add_book(book_name, book_writer):
                    print('Added')

            elif choice2 == '2':
                book_name = input('Name: ')
                book_writer = input('Writer: ')
                if school.remove_book(book_name, book_writer):
                    print('Removed')

            elif choice2 == '3':
                book_name = input('Name: ')
                book_writer = input('Writer: ')
                if school.remove_book(book_name, book_writer):
                    print('Borrwed')

            elif choice2 == '4':
                book_name = input('Name: ')
                book_writer = input('Writer: ')
                if school.add_book(book_name, book_writer):
                    print('Returned')

            elif choice2 == '5':
                amount = int(input('Enter amount: '))
                if school.fine(amount):
                    print('Fine Added to School Fund')
                else:
                    print('Invalid input')




        else:
            print('Invalid input')