[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/5Ulb2wWI)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=15994986)
# Data Structures Challenge

There are four tasks to complete, one for each of the core data structures in Python

## Task 1 - Lists

You have a starter list called _origional_list_

You must ask the user to input a new name to add to the list and then:
1. Use the appropriate list method to add the name to the __start__ of the list
2. Use an appropriate list method to remove the name "Jeff" from the list
3. Use the appropriate list method to store a copy of the list in a new list called _new_list_

## Task 2 - Dictionaries

You have two tuples called _keys_ and _values_

Using the appropriate dictionary method, combine these two into a single dictionary called _person_ with the keys tuple as the dictionaries keys and the values tuple as the dictionaries values

_**HINT - you will want to look up the "zip" method**_

_Then_, you will create a second dictionary called _car_ with the following keys and values:

```
car = {
    "make": "Ford",
    "model": "Focus",
    "engine": 1.6,
    "colour": "blue"
}
```

Finally, append this _car_ dictionary onto the end of the person dictionary with the key "car"

## Task 3 - Tuples

You have two tuples, _student_1_ and _student_2_

The student 1 tuple is filled out

The student 2 tuple is currently empty

Write a program which asks the user to enter the name (string), subject (string) and score (integer) out of 100 for the second student

_Then_, using the approprate techniques and methods, update the student 2 tuple to include this data in the same way that the student one tuple does

Following this, combine both tuples into a single tuple called _students_ - student 1 data should appear before student 2 data in this tuple

## Task 4 - Sets

You have two sets which contain fruits (and other items)

You must use an appropriate method to remove the non-fruit item from each set - you can simply "hard code" the value of the item to remove

Following this, you must create two more sets called _duplicate_fruits_ and _individual_fruits_

The duplicate fruits set must contain only the fruits that appear in both sets, the individual fruits set must contain only the fruits that appear in one set or the other, and not both

You must use appropriate set methods to do this - not simply type the fruit names into the new sets