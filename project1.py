
students = {
    "Aisha": 95,
    "Hauwa": 82,
    "Bilkisu": 90,
    "Amina": 76,
    "Fatima": 88
}

total = 0
topper = ""
highest = 0

for name, score in students.items():
    total += score

    if score > highest:
        highest = score
        topper = name

average = total / len(students)

print("STUDENT GRADE BOOK")
print("------------------")

print("Class Average:", average)
print("Class Topper:", topper)
print("Top Score:", highest)

search = input("Enter student name to search: ")

if search in students:
    print(search, "scored", students[search])
else:
    print("Student not found!")
