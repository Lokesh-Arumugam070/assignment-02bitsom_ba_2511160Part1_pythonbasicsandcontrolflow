# #Task1
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]
for data in raw_students:       
    name = data["name"].strip() #removing spaces and converting to title case 
    name = data["name"].title()
    roll = int(data["roll"])
    marks = [int(m) for m in data["marks_str"].split(", ")]   
# Validating name 
    is_valid = all(word.isalpha() for word in name.split())
    if is_valid:
        print(f"{name} (Roll: {roll}) = Valid name")
    else:
        print(f"{name} (Roll: {roll}) = Invalid name")
# output    
    print("=" * 32)
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print("=" * 32)
    
 # displaying student with roll no 103
    for student in raw_students:
     if student["roll"] == 103:
        name = student["name"]
        print("UPPERCASE :", name.upper())
        print("lowercase :", name.lower())

#Task2
student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]
# Grade validation
def get_grade(mark):
    if 90 <= mark <= 100:
        return "A+"
    elif 80 <= mark <= 89:
        return "A"
    elif 70 <= mark <= 79:
        return "B"
    elif 60 <= mark <= 69:
        return "C"
    else:
        return "F"

print("=" * 40)
print("Student :", student_name)
print("=" * 40)
#subject with grade
for i in range(len(subjects)):
    print(f"{subjects[i]} : {marks[i]} -> Grade {get_grade(marks[i])}")
# calculation of average,min and max
total = sum(marks)
avg = round(total / len(marks), 2)
highest_mark = max(marks)
lowest_mark = min(marks)
highest_subject = subjects[marks.index(highest_mark)]
lowest_subject = subjects[marks.index(lowest_mark)]
print("Total   :", total)
print("Average :", avg)
print(f"Highest : {highest_subject} ({highest_mark})")
print(f"Lowest  : {lowest_subject} ({lowest_mark})")
# While loop
new_subjects = []
new_marks = []
while True:
    subject = input("\nEnter subject name (or 'done' to stop): ").strip()
    
    if subject.lower() == "done":
        break

    mark_input = input(f"Enter marks for {subject} 0 to 100): ").strip()
# checking type of  input for marks
    if not mark_input.isdigit():
        print("Invalid input! Marks must be numeric.")
        continue

    mark = int(mark_input)

    # checking range of input for marks
    if mark < 0 or mark > 100:
        print("Invalid input! Marks must be between 0 and 100.")
        continue
    new_subjects.append(subject)
    new_marks.append(mark)
# result/final_output
total_of_new_subjects = len(new_marks)
all_marks = marks + new_marks
updated_avg = round(sum(all_marks) / len(all_marks), 2)

print("New Subjects Added :", total_of_new_subjects)
print("Updated Average    :", updated_avg)
print("=" * 40)


# #Task3
class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]
print("Name              | Average | Status")
print("-" * 40)
passed_count = 0
failed_count = 0
total_avg_sum = 0
topper_name = ""
topper_avg = 0
for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    status = "Pass" if avg >= 60 else "Fail"

    # Counting pass/fail
    if status == "Pass":
        passed_count += 1
    else:
        failed_count += 1

    # top performer identification
    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

    # Sum of averages
    total_avg_sum += avg

    print(f"{name} | {avg:>7.2f} | {status}")

# Class average
class_avg = round(total_avg_sum / len(class_data), 2)

# Final outputs
print("\nSummary:")
print("Students_Passed :", passed_count)
print("Students_Failed :", failed_count)
print(f"Class_Topper    : {topper_name} ({topper_avg})")
print("Class_Average   :", class_avg)


#Task4
essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Strip spaces
essay_new = essay.strip()
print("Essay New:")
print(essay_new)
#Title Case
print("\nTitle Case:")
print(essay_new.title())
# Count word python
count_python = essay_new.count("python")
print("\nCount of 'python':", count_python)
# Replace word  python with Python symbol
essay_replaced = essay_new.replace("python", "Python 🐍")
print("\nReplaced Essay:")
print(essay_replaced)
# Splitting sentence into list
sentences = essay_new.split(". ")
print("\nSentences List:")
print(sentences)
# Numbering sentences   
print("Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    sentence = sentence.strip()
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")
