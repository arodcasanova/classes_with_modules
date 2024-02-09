from teacher import Teacher
from course import Course

if __name__ == "__main__":
    hcde_teacher = Teacher("Adrian Rodriguez")
    hcde_class = Course("HCDE 310", hcde_teacher)
    print(hcde_class.teacher.name)

    for course in hcde_teacher.courses_taught:
        print(course.name)

    print(f"Teacher: {hcde_teacher.name} is teaching {hcde_teacher.courses_taught[0].name}")
