score = 5
#Figure out the users grading
if score == 0:
    grade = "F"
    print("Damn that's not good, Oh well there's always next time!")
elif score == 1 or score == 2:
    grade = "B"
    print("Oh no! So close!")
elif score == 3 or score == 4:
    grade = "A"
    print("Great job You win! Now try to get a better score!")
else:
    grade = "S"
    print("Wow amazing! A perfect score!")
# Tell the user their final grade
print("Your grade is {}".format(grade))
