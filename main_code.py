#Functions
def instructions():
    print("***          Welcome to this Gaming Quiz         ***")
    print("*** Where the success rate is extremely pitiful! ***")
    print("***     To play you must answer 5 questions      ***")
    print("***           All are multiple choice            ***")
    print("***    Incorrect answers lead to punishment      ***")
    print("***         Correct answers are rewarded         ***")
    print("***     Score higher to earn a better grade      ***")
    print("***     Make sure to have no spaces or caps!     ***")


#Main code
score = 0

# Ask if the user has played
heard_of = input("Have you heard of this quiz before?")
if heard_of == "no":
    instructions()
elif heard_of == "yes":
    print("Well we better get started then!")
else:
    print("Please enter yes or no!")

# Print questions
quest_ask1 = input("What year was the full version of Minecraft released?")

if quest_ask1 == "2011":
    print("Correct!")
    score += 1
else:
    print("Sorry that isn't correct!")

quest_ask2 = input("How many games does Sonic the hedgehog appear in?")

if quest_ask2 == "90":
    print("Correct!")
    score += 1
else:
    print("Nope that's incorrect")

quest_ask3 = input("What year did Roblox release?")

if quest_ask3 == "2006":
    print("That is correct!")
    score += 1
else:
   print("Nope Incorrect!")

quest_ask4 = input("What was the most popular Roblox game in 2021?")

if quest_ask4 == "piggy":
    print("Absolutely correct!")
    score += 1
else:
    print("Oops, That's not right!")

quest_ask5 = input("How many copies of minecraft were sold in 2021?")

if quest_ask5.strip() == "200million":
    print("100% Correct!")
    score += 1
else:
    print("Sadly, That's incorrect")
