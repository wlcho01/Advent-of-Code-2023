file1 = open('input4.txt', 'r')
lines = file1.readlines()

total = 0

#Question 1
'''
for line in lines:
    points = 0
    str = line.split()
    card = str[1]
    win = str[2:12]
    nums = str[13:38]
    for num in win:
        if num in nums and points == 0:
            points += 1
        elif num in nums and points > 0:
            points *= 2
            
    total += points
print(total) #25231
'''

#Question 2
index = 0
copies = [0] * 212 #minus original
for line in lines:
    num_of_cards = 1
    num_of_cards += copies[index]
    #print(num_of_cards)
    increase = 0
    str = line.split()
    card = str[1]
    win = str[2:12]
    nums = str[13:38]
    for num in win:
        if num in nums:
            increase += 1
    for i in range(index + 1, index + 1 + increase):
        copies[i] += num_of_cards
    total += num_of_cards
    index += 1
#print(copies)
print(total)
        