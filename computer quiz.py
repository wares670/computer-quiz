print("welcome to my computer quiz")

playing = input("do you want to play? ")

if playing != "yes":
     quit()

print("okay! let's play :)")

answer = input("what does cpu stand for? ")
if answer == "central processing unit":
    print('correct!')
else:
    print("incorrect!")

answer = input("what is python? ")
if answer == "programming language":
    print('correct!')
else:
    print("incorrect!")

answer = input("what does ram stand for? ")
if answer == "random access memory":
    print('correct!')
else:
    print("incorrect!")

answer = input("what does gpu stand for? ")
if answer == "graphics processing unit":
    print('correct!')
else:
    print("incorrect!")
    print("your the best!")