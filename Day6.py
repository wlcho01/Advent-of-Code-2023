import time

file1 = open('input6.txt', 'r')
lines = file1.readlines()
#Part1
'''
timelist = lines[0].split()[1:5]
print(timelist)
distlist = lines[1].split()[1:5]
print(distlist)

total = 1

for count, ele in enumerate(timelist):
    num = 0
    time_int = int(timelist[count])
    for hold_time in range(1, time_int):
        dist = hold_time * (time_int - hold_time)
        if dist > int(distlist[count]):
            num += 1
    total *= num   
print(total)#4403592
'''
#Part 2
total = 0            
t = int(''.join(lines[0].split()[1:5]))
distance = int(''.join(lines[1].split()[1:5]))
start_time = time.time()
for hold_time in range(1, t):
    dist = hold_time * (t - hold_time)
    if dist > distance:
        total += 1


print(total)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))
            
