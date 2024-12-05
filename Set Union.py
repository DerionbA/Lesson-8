myset = {1,1,2,2,3,3,4,4}
print(myset)
myset.add(5)
print(myset)
set1 = myset
set2 = {2,2,2,2,2,2,7,7,7,7,7}
print("\nSet 1", set1)
print("Set 2", set2)
print("Difference")
print(set1.difference (set2))
print("Symmeteric Difference")
print(set1.symmetric_difference(set2))


