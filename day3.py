
for _ in range(5):
    print("i am looping")

turns = 0
while turns < 5:
    print("WHILE LOOPING")
    turns += 1

choice = ""
while choice != "n":
    print(choice)
    choice = input("Do you want to loop again? [Y/n] ")
