# Dictionaries

# Dictionaries use key/value pairs

# key = a refernence to a particular object
# value = data storage mechanism you want to use

# create a dictionary

student_1 = {
    "name": "skitz",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types" "set_up"]

}

# Access data within a dictionary

print(student_1["stream"]) # Devops

# how to access particular parts of a list in a dictionary
print(student_1["completed_lesson_names"[2]])

# changing a value in a dictionary

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

# Removing items from a dictionary

student_1["completed_lesson_names"].remove(data_types)
print(student_1["completed_lesson_names"])

# dicitionary methods

# keys

print(student_1.keys())

# gets the value of the key back without []
print(student_1.get("name"))

student_2 = {
    "name": "joohnny",
    "stream": "DevOps",
    "completed_lessons": 1,
    "completed_lesson_names": ["variables", "data_types" "set_up"]




