file1 = open('input2.txt', 'r')
lines = file1.readlines()

total = 0
punctuation = ";,:"
#Question 1
'''
dict = {
    "red": 12,
    "green": 13,
    "blue": 14
}


for line in lines:
    number = []
    colour = []
    for ch in line:
        if ch in punctuation:
            line = line.replace(ch, "")
    lst = line.split()
    for i in range(3, len(lst), 2):
        colour.append(lst[i])
    for i in range(2, len(lst), 2):
        number.append(lst[i])
    for i in range(len(colour)):
        limit = dict.get(colour[i])
        if int(number[i]) > limit:
            break
    else:
        total += int(line.split(" ")[1])
            
print(total) #2716
'''

for line in lines:
    multiply = 1
    dict = {
    "red": 0,
    "green": 0,
    "blue": 0
    }
    number = []
    colour = []
    for ch in line:
        if ch in punctuation:
            line = line.replace(ch, "")
    lst = line.split()
    for i in range(3, len(lst), 2):
        colour.append(lst[i])
    for i in range(2, len(lst), 2):
        number.append(lst[i])        
    for i in range(len(colour)):
        limit = dict.get(colour[i])
        if int(number[i]) > limit:
            dict[colour[i]] = int(number[i]) 
            limit = int(number[i])
    for num in dict.values():
        multiply *= num
    total += multiply
print(total)
          