from math import floor

f = open('input.txt', 'r')
data = f.readlines()
f.close()



i = 0
integers = []
while i < len(data):
    integers.append(int(data[i]))
    i += 1

j = 0
res = []
while j < len(data):
    res.append(floor(integers[j]/3) - 2)
    j += 1

print("Total: ", sum(res))