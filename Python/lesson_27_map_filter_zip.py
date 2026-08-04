#map (function, iterable) it perfor same function on each iterables
#normal funtion
print("====Normal functon using map ====")
def square(x):
    return x * x

numbers = [1,2,3,4]
result = list(map(square, numbers))
print(result)