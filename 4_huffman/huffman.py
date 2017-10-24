input_str = input('Please enter sentence >> ')


# Count Prob
alphabet = 'abcdefghijklmnopqrstuvwxyz '
count_alpha = [0]*len(alphabet)
count = 0

for char in input_str:
    if char not in alphabet:
        print('error: Some character not in languages.')
        exit()

for char in input_str:
    count += 1
    count_alpha[alphabet.find(char)] += 1

first_step = list()
consider_alpha = dict()

for i in range (len(count_alpha)):
    if count_alpha[i] > 0:
        consider_alpha[alphabet[i]] = ''
        first_step.append((alphabet[i],count_alpha[i]/count))

if len(consider_alpha) < 2:
    print('error: Required more than 2 unique characters.')
    exit()

first_step = sorted(first_step, key=lambda x: -x[1]) 

consider = list(first_step)
steps = list()

print('Steps')
while len(consider) > 1:
    steps.append(consider)
    step_str = ''
    for each in consider:
        step_str += '\''+each[0]+'\':' + str(each[1])[:4] +' '
    print(step_str)
    last = consider[-1]
    pre_last = consider[-2]
    com1 = ''
    com2 = ''
    for c in last[0]:
        if c != '|':
            com1 += c
    for c in pre_last[0]:
        if c != '|':
            com2 += c
    new = (com2+'|'+com1,last[1]+pre_last[1])
    new_consider = consider[:-2]
    new_consider.append(new)
    consider = sorted(new_consider, key=lambda x: -x[1]) 

print('\nFinal Encoding')

for char in steps[-1][0][0]:
    if char != '|':
        consider_alpha[char] += '0'
for char in steps[-1][1][0]:
    if char != '|':
        consider_alpha[char] += '1'

for i in range(len(steps)-1,0,-1):
    unique = list()
    for each in steps[i-1]:
        if each not in steps[i]:
            unique.append(each)
    for char in unique[0][0]:
        if char != '|':
            consider_alpha[char] += '0'
    for char in unique[1][0]:
        if char != '|':
            consider_alpha[char] += '1'
    
print(consider_alpha)