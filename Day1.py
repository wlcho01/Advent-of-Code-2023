import re

file1 = open('input.txt', 'r')
lines = file1.readlines()

total = 0

words_to_numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
#Question 1
'''
for line in lines:
    lst = []
    for i, c in enumerate(line):
        if c.isdigit():
            lst.append(c)
            break
    for i, c in enumerate(line[::-1]):
        if c.isdigit():
            lst.append(c)
            break
    calibration = lst[0] + lst[1]
    total += int(calibration)
    
print(total) #54708
'''

    
#Question 2
for line in lines:
    lst = []
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    first = (re.findall(r'(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d)',line))[0] 
    last = (re.findall(r'(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|(\d)',line))[-1]
    first_test = [thing for thing in first]
    new_first = [thing for thing in first_test if thing != '']
    if new_first[0].isalpha():
        num_first = ''.join(words_to_numbers[ele] for ele in new_first)
        lst.append(num_first)
    else:
        lst.append(new_first[0])
    last_test = [thing for thing in last]
    new_last = [thing for thing in last_test if thing != '']
    if new_last[0].isalpha():
        num_last = ''.join(words_to_numbers[ele] for ele in new_last)
        lst.append(num_last)
    else:
        lst.append(new_last[0])
    calibration = lst[0] + lst[1]
    print(calibration)
    total += int(calibration)
     
print(total)
    
        
    