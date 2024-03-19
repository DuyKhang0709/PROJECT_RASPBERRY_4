number = int(input("Enter number between 1 and 100: "))


if number <= 0 or number > 100:
    print("Wrong number: " + str(number))
else:
    print("Correct number: " + str(number))