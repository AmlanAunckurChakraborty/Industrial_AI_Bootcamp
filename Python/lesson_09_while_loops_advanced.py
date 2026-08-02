#final output by using break in contineous while loops
while True:

    password = input("Enter password: ")

    if password != "1234":
        print("Access Denied !!!")

    else:
        print("Welcome to the system")
        break        # exit password loop


while True:

    pressure = float(input("Enter the Current pressure: "))

    if pressure <= 100:
        valve = True
    else:
        valve = False

    print("Valve status:", valve)