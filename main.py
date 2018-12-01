import numpy as np

def findJ(mov, j):
    if(mov == 'right'):
        j +=1
        return j
    if(mov == 'left'):
        j -= 1
        return j
    return j

def findI(mov, i):
    if(mov == 'down'):
        i +=1
        return i
    if(mov == 'up'):
        i -=1
        return i
    return i

def echo(buffer):
    str = ''
    for i in range(0, len(buffer)):
        str = str + chr(buffer[i])
    return str    

#start program
lines = []
table = []
stack = []
bufferEcho = []
movHorizon = 'none'
movVertical = 'none'
pointFlag = True
asciiFlag = False

# Open and read file
f = open('hello.txt', 'r')

# delete \n and to array
lines = f.read().splitlines()

#make table with operations and operands
for i in range(0, len(lines)):
    lin = list(lines[i])
    print(lin)
    table.append(lin)
print(table)

# print(table[first(IP)][second(IP)])

#start proccesing
i = 0
j = 0
while(pointFlag == True):
    i = findI(movVertical, i)
    j = findJ(movHorizon, j)
    # print('i is', i)
    # print('j is', j)
    if(table[i][j] == '>' and asciiFlag == False): 
        movHorizon = 'right'
        movVertical = 'none'
        print('>')
        continue
    if(table[i][j] == '<' and asciiFlag == False):
        movHorizon = 'left'
        movVertical = 'none'
        print('<')
        continue
    if(table[i][j] == 'v' and asciiFlag == False):  
        movVertical = 'down'
        print('v')
        continue
    if(table[i][j] == '^' and asciiFlag == False):
        movVertical = 'up'
        print('^')
        continue
    if(table[i][j] == '"' and asciiFlag == True):
        asciiFlag = False
        print(' ASCII False')
        continue
    if(table[i][j] == '"' and asciiFlag == False):
        asciiFlag = True
        print(' Ascii True')
        continue
    if(table[i][j] == ',' and asciiFlag == False):
        bufferEcho.append(stack.pop())
        print(' , ')
        continue
    if(table[i][j] == '@' and asciiFlag == False):
        pointFlag = False
        print(' @ ',)
        continue
    if(type(table[i][j]) is int and  asciiFlag == False):
        stack.append(table[i][j])
        print('num i')
        continue
    if(asciiFlag):
        stack.append(ord(table[i][j]))
        print('ord symbol', table[i][j])
        continue
   

print('buffer to display is ', bufferEcho)
print('stack is ', stack)
print(echo(bufferEcho))

