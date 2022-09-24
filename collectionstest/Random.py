# random library import
from array import array
from random import random, randrange, randint

# print(randrange(10))
# print(randrange(17, 23))

ages = array('i', [])

# Looping
for i in range(0, 24):
    ages.append(randrange(17, 23))

print(ages)
length = len(ages)
print(length)
print(min(ages))
print(max(ages))
print(round(sum(ages) / 24))

tmp = input("Enter age to find : ")
tmp = int(tmp)
count = ages.count(tmp)

# index_of_array = index(tmp, 0, len(ages))

if count > 0:
    print("{} found {} times".format(tmp, count))

else:
    print("{} not found".format(tmp))



##### ----- 21found 2 times in [0,4] indexes ! ----- #####

print(help(randrange))


