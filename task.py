def task_1(): # Lists

    origional_list = ["Geoff", "Jeff", "Jeffrey"]
    name = input("What name should be added to the list?")
    origional_list.insert(0, name)
    origional_list.remove("Jeff")
    new_list = origional_list.copy()
    return new_list


def task_2(): # Dictionaries

    keys = ("name", "age", "profession")
    values = ("Geoff", 35, "technician")
    person = dict(zip(keys, values))
    car = {
    "make": "Ford",
    "model": "Focus",
    "engine": 1.6,
    "colour": "blue"
    }
    person.update({"car": car})
    return person


def task_3(): # Tuples
    student_1 = ("Geoff", "Maths", 80)
    name = input("What's student 2's name?")
    subject = input("Their subject?")
    score = int(input("Their score?"))
    student_2 = (name, subject, score)
    student_2 = tuple(student_2)
    students = student_1 + student_2
    return students


def task_4(): # Sets
    fruits_1 = {"apple", "banana", "cherry", "grape", "mango", "pineapple", "papaya","sprite", "orange", "lemon", "strawberry"}
    fruits_2 = {"raspberry", "banana", "cherry", "grape", "mango", "blueberry", "papaya", "melon", "lemon", "steak"}
    fruits_1.discard("sprite")
    fruits_2.discard("steak")

    duplicate_fruits = fruits_1.intersection(fruits_2)
    individual_fruits = fruits_1.symmetric_difference(fruits_2)

    return [duplicate_fruits, individual_fruits] # Note - functions can only return one data item - so both tuples
                                                 # are contained inside a single list
