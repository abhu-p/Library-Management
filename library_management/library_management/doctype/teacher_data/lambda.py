num = [1, 2, 3, 4, 5]
new = list(filter(lambda n: n % 2 == 0, num)) 
print("the new list is", new)

students = [
    {"name": "Ram", "marks": 95},
    {"name": "Sita", "marks": 92},
    {"name": "Hari", "marks": 78}
]

# Marks ले sort
sorted_by_marks = sorted(students, key=lambda s: s["marks"])
print("Marks:", sorted_by_marks)

# Name ले sort
sorted_by_name = sorted(students, key=lambda s: s["name"])
print("Name:", sorted_by_name)

# String length ले sort 
words = ["apple", "hi", "banana", "ok"]
sorted_by_length = sorted(words, key=lambda w: len(w))
print("Length:", sorted_by_length)