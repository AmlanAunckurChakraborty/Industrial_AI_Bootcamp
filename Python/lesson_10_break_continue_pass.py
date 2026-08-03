# With break function
print("\n========== BREAK ==========\n")

n = 1
while n <= 6:
    print("Number of iteration before break:", n)
    if n == 4:
        break      # break will simply exit the loop
    n += 1  
    i = n-1       # need n+1 after break
    print("Number of ieteration after break",i)
    print("iteration completed ")


# With continue function
print("\n========== CONTINUE ==========\n")

m = 1
while m <= 6:
    print("Number of iteration before continue:", m)
    m += 1         # # Increment before continue, otherwise the loop could become infinite.
    j = m-1       
    if m == 4:
        continue   # continue skips the remaining statements of this iteration
    print("Number of iteration after continue:", j) # not in the continue funtion, in the while loop till skip this iteration and go to next iteration
    print("iteration completed ")


# With pass function
print("\n========== PASS ==========\n")

p = 1
while p <= 6:
    print("Number of iteration before pass:", p)
    p += 1 
    k = p-1       # need n+1 before pass
    if p == 4:
        pass      # pass does nothing but simply ignore the next line
    print("Number of iteration after pass:", k) # in the pass funtion , not in the while loop,only ignore the next line not the iteration and if use with while loop then will till print as not with the pass
    print("iteration completed ")
