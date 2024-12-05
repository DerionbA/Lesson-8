mytuples=()
print(mytuples)
mytuples=(1,2,3)
print(mytuples)
mytuples=(1, 'Derion', 1.45)
print(mytuples)
mytuples=("Derion", [3,10,5,8], (1,3,2,5))
print(mytuples)
mytuples=("a", "b", "c", "d", "e", "f")
print(mytuples[0])
print(mytuples[5])
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))


#nested index
print(n_tuple[0][3])


print(n_tuple[1][1])
# Slicing
print("Sliced", mytuples[1:4])
# Iterating through tuple
for letter in (mytuples):
    print("Hello", letter)
