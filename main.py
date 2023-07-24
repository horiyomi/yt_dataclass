from dataclasses import dataclass, field

# class Student:

#     def __init__(self, name: str, age: int, course: str, grade: int):
#         self.name = name
#         self.age = age
#         self.course = course
#         self.grade = grade

#     def __repr__(self) -> str:
#         return f"Name: {self.name} \nAge: {self.age} \nCourse: {self.course} \nGrade: {self.grade}"
    
# davis = Student(name="Davis", age=20, course="Physics", grade=60)
# raven = Student(name="Raven", age=22, course="Physics", grade=60)

# # print(davis)
# # print("------------")
# # print(raven)

# print( davis == raven)


@dataclass(frozen=True, slots=True)
class Student:
    name: str
    age: int = field(init=False, default=0)
    course: str
    grade: int
    bonus_point: int = 10

    def __eq__(self, other) -> bool:
        return self.course == other.course
    
    def __gt__(self, other) -> bool:
        return self.grade > other.grade

davis = Student(name="Davis", course="Physics", grade=60)
# raven = Student(name="Raven", age=22, course="Physics", grade=80)

# davis.name = "Rayden"

print(davis)