import time
from heap import sorted

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

sorted1 = sorted(names_1)
sorted2 = sorted(names_2)
duplicates = []

i=0
j=0

while i < len(sorted1) and j<len(sorted2):
    if sorted1[i] == sorted2[j]:
        duplicates.append(sorted1[i])
        i+=1
        j+=1
    elif sorted1[i] < sorted2[j]:
        j+=1
    else:
        i+=1


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

