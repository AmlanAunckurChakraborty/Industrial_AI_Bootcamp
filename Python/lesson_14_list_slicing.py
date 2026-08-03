#list slicing
print("\nlist slicing\n")

pressure = list(map(int, input("Enter pressure values: ").split()))
print("list lenght:",len(pressure),"\n","list value :",pressure)
print("start: ",pressure[2:]) #start
print("stop: ",pressure[:2]) #stop
print("step: ",pressure[::2]) #step
print("start,stop: ",pressure[1:8]) #start,stop
print("start,step: ",pressure[1::2]) #start,step
print("stop,step: ",pressure[:8:2]) #stop,step
print("start,stop,step: ",pressure[1:8:2]) #start,stop,step
print("reverse list: ",pressure[::-1]) #reverse the list
print("reverse with interval: ",pressure[::-3]) #reverse with interval
print("user defined-start,stop,step: ",pressure[ int(input("Enter start value:")) : int(input("Enter stop value:")) : int(input("Enter step value:")) ]) #start,stop,step user defined