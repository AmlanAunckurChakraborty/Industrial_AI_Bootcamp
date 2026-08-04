# LESSON 19.3 - SET OPERATIONS

print("\n========== SET OPERATIONS ==========\n")
A = set(map(int, input("Enter Set A: ").split()))
B = set(map(int, input("Enter Set B: ").split()))
print("\nSet A :", A)
print("Set B :", B)

# UNION  ***** add all the values *****
print("\n========== UNION ==========")
print("Using | :", A | B)
print("Using union() :", A.union(B))

# INTERSECTION ***** only extract common value *****
print("\n========== INTERSECTION ==========")
print("Using & :", A & B)
print("Using intersection() :", A.intersection(B))

# DIFFERENCE ***** only delete 2nd set common elements from first set*****
print("\n========== DIFFERENCE ==========")
print("A - B :", A - B)
print("A.difference(B) :", A.difference(B))
print("B - A :", B - A)
print("B.difference(A) :", B.difference(A))

# SYMMETRIC DIFFERENCE ***** delete common values and pull others ,its some how oposite of intersection *****
print("\n========== SYMMETRIC DIFFERENCE ==========")
print("Using ^ :", A ^ B)
print("Using symmetric_difference() :", A.symmetric_difference(B))

# SUBSET ***** St b will have all the a set values and other then that if a has 3values b shold have atleast 4 and out of them which 3 elements a have b should have them all *****
print("\n========== SUBSET ==========")
print("A is subset of B :", A.issubset(B))
print("B is subset of A :", B.issubset(A))

# SUPERSET 
print("\n========== SUPERSET ==========")
print("A is superset of B :", A.issuperset(B))
print("B is superset of A :", B.issuperset(A))

# DISJOINT ***** shouldnt have common values ***
print("\n========== DISJOINT ==========")
print("A and B are disjoint :", A.isdisjoint(B))