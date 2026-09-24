print("\n---------------------#1---------------------\n")
numbers = [10, 20, 10, 30, 20, 40, 10, 50]
unique_numbers = set(numbers)
print(numbers)
print(unique_numbers)
print(len(unique_numbers))
print(30 in unique_numbers)
print(100 in unique_numbers)

print("\n---------------------#2---------------------\n")
data = [15, "Python", 15, True, "Python", 3.14, False, True]
unique_data = set(data)
print(unique_data)
unique_data.add("Redis")
unique_data.add(100)
unique_data.remove("Python")
print(unique_data)
print(True in unique_data)
print(False in unique_data)

print("\n---------------------#3---------------------\n")
python_students = {"Anna", "Oleh", "Ivan", "Maria"}
redis_students = {"Oleh", "Maria", "Petro", "Sofia"}
students_union_operator = python_students | redis_students
students_union_method = python_students.union(redis_students)
print(students_union_operator)
print(students_union_method)
print(students_union_operator == students_union_method)

print("\n---------------------#4---------------------\n")
students_intersection_operator = python_students & redis_students
students_intersection_method = python_students.intersection(redis_students)
print(students_intersection_operator)
print(students_intersection_method)

print("\n---------------------#5---------------------\n")
all_students = {"Anna", "Oleh", "Ivan", "Maria", "Petro", "Sofia"}
python_students = {"Anna", "Oleh", "Ivan"}
students_difference_operator = all_students - python_students
students_difference_method = all_students.difference(python_students)
print(students_difference_operator)
print(students_difference_method)

print("\n---------------------#6---------------------\n")
numbers = {10, 20, 30}
numbers.add(40)
numbers.add(40)
numbers.update([50, 60, 70])
numbers.remove(20)
numbers.discard(100)
removed_number = numbers.pop()
print(removed_number)
print(numbers)
