# original numbers in list
l = [1, 2, 2, 2, 3, 3, 3, 4]

# empty dictionary to hold pair of number and its count
d = {}

# loop through all elements and store count
[d.update({i: d.get(i, 0)+1}) for i in l]

print(d)
# {1: 1, 2: 2, 3: 3, 4: 1}
