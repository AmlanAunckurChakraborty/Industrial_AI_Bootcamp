
#Random module
import random as r
print(r.random()) # random function under random module works for printing any float between 00.0<=x>=1.0
print(r.randint(1,100)) # need uper and lower range value otherwise wont work
print(r.randrange(15,100,5)) # handle step also for even we can put 2 as step and # Upper value is excluded, just like range()
#***** both works only for integer value********
print(r.uniform(1,100)) # design floating values but cant handle step

#choice
numbers = tuple(map(float,input("enter anynuber").split()))
print(r.choice(numbers)) #choice choos any element from substance but cant handle set
num = set(map(int,input("enter any number").split()))
print(r.choice(list(numbers)))

#choices
alarms = ["NORMAL","HIGH P","LOW P","TRIP"]
print(r.choices(alarms, k=15)) # can execute random as may times we need by key ,k
print(r.choices(alarms,weights=[90,5,3,2],k=20)) # can also put weight to create a specific pattern in data set

#sample
value = list(map(float,input("enter any value").split()))
data = r.sample(value,k=len(value))
print(data)
print("output data type",type(data))
#moredata = r.sample(value,k=(int(len(value))*2)) #cant perform this but choices can
#print(moredata)
moredata = r.choices(value,k=(len(value))*2) #can make even more data then actual data set picking values multiple time
print(moredata)

#shuffle
r.shuffle(value)
print ("shuffled values",value) #shuffle dont need to assgin on anything it simple shuffle the original list,
#as changing so dont work on tuple also also cant print one line as dont return anything
#so if we train directly for big data shuffle reduce significant time

#seed
r.seed(100) # seed will fix the random output once and ever no matter how many times we run the file
#Make random numbers repeat exactly
for i in range(5):
    print(r.randint(1,10)) 

#my old phone number data set
import random as r
 #single random phone number having 02 at the bigening
phone = "02" + str(r.randint(1000000, 9999999))
print(phone)
#using loops for more numbers
for n in range(5):
 phone = "02" + str(r.randint(1000000, 9999999))
 print(phone)

#mobile phone number data generation 
third = r.choice([3, 4, 5, 6, 7, 8, 9]) # need to put it in the for loop otherwise every number will have same third number which it randomly picks first
for n in range (5):
 phone = "+880-1" + str(third) + str(r.randint(10000000, 99999999))
 print(phone)


#final one
print("\n=== Final One ===\n")
operator_identifier = ["7","3","9","4","8","6","5"]
user_ratio  = [40,15,20,8,10,5,2]

for n in range(30):
    thierd_digit = r.choices(operator_identifier, weights= user_ratio, k=1)[0] 
# [0] is used to get the value of first element of the list and k= 1 as we need only one number during one iteration 
    phone = "+880-1" + thierd_digit + str(r.randint(10000000,99999999))
    print(phone)

print("phone datatype",type(phone))
print("thrid_digit datatype",type(thierd_digit))
