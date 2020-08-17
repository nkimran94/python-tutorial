marks = int(input("What is your grade: "))

def show_grade(grade):
    print("You got: {}".format(grade))

if marks >= 80:
    show_grade("A+")
elif marks < 80 and marks >= 70:
    show_grade("A")
elif marks < 70 and marks >= 60:
    show_grade("A-")
elif marks >= 33:
    show_grade("Passed")
else:
    show_grade("F")
print("Finished")