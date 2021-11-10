# Functions
def instructions():
    print("***         Welcome to this Gaming Quiz          ***")
    print("*** Where the success rate is extremely pitiful! ***")
    print("***     To play you must answer 5 questions      ***")
    print("***           All are multiple choice            ***")
    print("***    Incorrect answers lead to punishment      ***")
    print("***         Correct answers are rewarded         ***")
    print("***     Score higher to earn a better grade      ***")
    print("***     Make sure to have no spaces or caps!     ***")


# Main code
heard_of = input("Have you heard of this quiz before?")
if heard_of == "no":
    instructions()
elif heard_of == "yes":
    print("Well we better get started then!")
else:
    print("Please enter yes or no!")
