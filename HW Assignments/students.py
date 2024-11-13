import sys

# Class to represent each student
class Student:
    def __init__(self, ID, last_name, first_name, gender, scores):
        self.ID = ID
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.scores = scores
        self.average_score = self.calculate_average()

    # Method to calculate the average score
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

# Function to read the students.txt file and create Student objects
def makeStudents(filename):
    student_list = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                ID = data[0]
                last_name = data[1]
                first_name = data[2]
                gender = data[3]
                scores = list(map(int, data[4:]))  # Convert scores to integers
                student = Student(ID, last_name, first_name, gender, scores)
                student_list.append(student)
    except FileNotFoundError:
        print(f"Error: File {filename} not found!")
        sys.exit(1)
    return student_list

# Function to find the student with the highest average
def findHighest(students):
    highest_student = max(students, key=lambda student: student.average_score)
    return highest_student.first_name, highest_student.last_name, highest_student.average_score

# Function to find the female student with the highest average
def findHighestFemale(students):
    females = [student for student in students if student.gender.lower() == 'f']
    highest_female = max(females, key=lambda student: student.average_score)
    return highest_female.first_name, highest_female.last_name, highest_female.average_score

# Main function to run the program
def main():
    # Check if the correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python students.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]  # Filename from command line argument
    students = makeStudents(filename)

    if not students:
        print("No students found. Exiting program.")
        return

    # Find and display the student with the highest average
    first_name, last_name, highest_avg = findHighest(students)
    print(f"{first_name} {last_name} had the highest average of {highest_avg:.1f}")

    # Find and display the female student with the highest average
    first_name_f, last_name_f, highest_female_avg = findHighestFemale(students)
    print(f"{first_name_f} {last_name_f} had the highest female average of {highest_female_avg:.1f}")

# Ensure the main function runs if the script is executed
if __name__ == '__main__':
    main()
