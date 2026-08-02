#While Loops
#basic while loop
i = 1
while i <= 5:
    print("Number of itaration:",i)
    i=i+1

#With break function

n = 1

while n <= 5:

    print("Number of itaration before break:",n)

    if n == 3:
        break

    n += 1  # need n+1 after break and before continue
    print(n)

#With continue function

m = 0

while m <= 5:

    m += 1

    if m == 3:
        continue  # continue will simply skip the itaration and jump to the next

    print("Number of iteration for continue in 3:",m)

#user input while loop with else funtion
#continous while loop

""" 
while password != "1234": 

*** in this example its printing access denied even after we put 1234 for 
    the first time so we need a if loop in the shile loop , so its better we make the while loop a contineous one and use if in it.  ***

    password = input("Enter password: ")
    print("Access Granted !!!")
    
else:
    print("Welcome to the system")
"""
while True:
    password = input("Enter password: ")
    if(password != "1234"):
     print("Access Denied !!!")

    else:
     print("Welcome to the system")  
     pressure =float(input("Enter the Current pressure"))
     if(pressure <= 100):
        valve = True
     else:
        valve = False
     print("valve status :",valve)  

#use first one for if access denied and in the valve one did ture in if and false in else just tried two mathods , as cant use two contineoues loop in same project that why use single loop for two logic


"""
while(1):
    print("Running,,, To stop press : Ctrl+c")
 
"""