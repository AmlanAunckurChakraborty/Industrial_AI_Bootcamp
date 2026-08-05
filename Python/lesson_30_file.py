#File creation and handling

#Write/create a new file if file exits replace previous one
file = open("data.txt", "w")
file.write("Hello Amlan \nThis portion will be deleted after send write cmd\n")
file.close()
file = open("data.txt", "w")
file.write("Writing changed Amlan\n")
file.close()

#Read only the file dont write or change anything
file = open("data.txt","r")
file.close()

#Append a file dont replace previous datas, add at the end
file = open("data.txt", "a")
file.write("New writting added Amlan\n") #new line works here so
file.close()


#Read the data and execute function

file = open("data.txt","r")
data = file.read()
print(data)
file.close()
#final one

#more realestic exicution
print("\n=== Final One ===\n")

import random as r
operator_identifier = ["7","3","9","4","8","6","5"]
user_ratio  = [40,15,20,8,10,5,2]

file = open("mobile directory.txt","a")
file.write("\n==== New Data Set Has Arrived ====\n")
for n in range(30):
    thierd_digit = r.choices(operator_identifier, weights= user_ratio, k=1)[0] 
    phone = "+880-1" + thierd_digit + str(r.randint(10000000,99999999))
    file.write(phone + "\n")
""""
  file.write(phone)      # write() writes one string at a time, so multiple writes are needed for multiple pieces of data.
    file.write("\n")
"""
file.close()



