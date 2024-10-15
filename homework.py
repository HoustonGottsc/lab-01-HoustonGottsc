# Houston Gottsch
# UWYO COSC 1010
# 10/15/24
# HW 01
# Lab Section: 15
# Sources, people worked with, help given to:
# your
# comments
# here
# Homework Question:
#
# You are given a list of dictionaries where each dictionary represents a student
# and their scores
# in different subjects.
#
# Student Data:
#students = {
 #{"name": "Alice", "scores": {"Math": 85, "Science": 90, "English": 78}},
 #{"name": "Bob", "scores": {"Math": 70, "Science": 88, "English": 82}},
 #{"name": "Charlie", "scores": {"Math": 92, "Science": 81, "English": 89}},
 #{"name": "David", "scores": {"Math": 60, "Science": 75, "English": 80}}
#}
#Write a Python program that:
# 1. Calculates the average score for each student.
# 2. Stores these averages in a new dictionary where the student’s name is the key
# and their average score is the value.
# 3. Prints the names of students whose average score is greater than 80.
# Your task is to calculate the average scores for each student and print the names
# of students
# whose average score is greater than 80.
#Solution
students = {
    "Name":"Alice",
    "Scores":{
        "Math": 85,
        "Science": 90,
        "English": 78
    },
     "Name":"Bob",
    "Results":{
        "Math": 70,
        "Science": 88,
        "English": 82
    },
    "Name":"Charlie",
    "Grades":{
        "Math": 92,
        "Science": 81,
        "English": 89
    },
    "Name":"David",
    "Graded":{
        "Math": 60,
        "Science": 75,
        "English": 80
    },
}
a = (0)
b = (0)
c = (0)
d = (0)
e = (0)
g = (0)
h = (0)
i = (0)
j = (0)
for key, value in students.items():
    if key == "Scores":
        for value, digit in value.items():
            a += digit
            b += 1
            c = (a/b)
    elif key == "Results":
        for value, digit in value.items():
             d += digit
             e = (d/b)
    elif key == "Grades":
        for value, digit in value.items():
             g += digit
             h = (g/b)
    elif key == "Graded":
        for value, digit in value.items():
             i += digit
             j = (i/b)
        Averages = {}
        Averages["Alice"] = c
        Averages["Bob"] = e
        Averages["Charlie"] = h
        Averages["David"] = j
        for key, value in Averages.items():
            if value > 80:
                print(key)