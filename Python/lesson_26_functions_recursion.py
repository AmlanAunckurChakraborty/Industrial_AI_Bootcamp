#recursion
print("========recursion, when function calls it self=========")

#normal example without recursion
print("\n=== normal  ====\n")
def countdown(number):
    while number > 0:
        print("\n iteration")
        print(number)
        number -= 1

countdown(5)

#using recursive funtion
print("\n==== recursive ====\n")
def countdown(number):
    if number == 0: #stopping condition by this function stops
        return       # function stops here
    print("\n iteration")
    print(number)
    countdown(number - 1)

countdown(5)

print("\n==== recursive plant example ====\n")
pressure = [520,525,530,540]
def check_sensor(data, index):
    if index == len(data):
        return
    print(data[index])
    check_sensor(data, index + 1)

check_sensor(pressure, 0)

print("\n==== recursive factorial example ====\n")
def factorial(number):
    if number == 1:
        return 1
    return number * factorial(number-1)

print(factorial(6))
