#Find a full diviser of a number

list = []

def findDiviser(number):
    for i in range(1, (number + 1)):
        if number % i == 0:
            list.append(i)
    return list

while True:
    print("******************Diviser Finder******************")
    print("Enter the number press y to find diviser")
    print("Enter q to quit")
    option = input(">")
    if option == "q":
        break
    elif option == "y":
        while True:
            number = int(input("Enter the number: "))
            findDiviser(number)
            print(list)
            list.clear()
    else:
        print("Invalid input")
