# import numpy as np
import random 

#move Horizon
def findJ(mov, j):
    if(mov == 'right'):
        j +=1
        return j
    if(mov == 'left'):
        j -= 1
        return j
    return j

#move Vertical
def findI(mov, i):
    if(mov == 'down'):
        i +=1
        return i
    if(mov == 'up'):
        i -=1
        return i
    return i

#display result
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
#for random generate
movHorizonArr = ['left', 'right', 'nope']
movVerticalArr = ['up', 'down', 'nope']
#flags
pointFlag = True
asciiFlag = False

# Open and read file
f = open('stackOperations.txt', 'r')

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
    # moving
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
        movHorizon = 'none'
        print('v')
        continue

    if(table[i][j] == '^' and asciiFlag == False):
        movVertical = 'up'
        movHorizon = 'none'
        print('^')
        continue

    if(table[i][j] == '"' and asciiFlag == True):
        asciiFlag = False
        print(' Ascii False is enabled')
        continue

    if(table[i][j] == '"' and asciiFlag == False):
        asciiFlag = True
        print(' Ascii True is enabled')
        continue

    if(table[i][j] == ',' and asciiFlag == False):
        bufferEcho.append(stack.pop())
        print(' , ')
        continue

    if(table[i][j] == '_' and asciiFlag == False):
        print(' _ ')
        if not stack:
            movHorizon = 'right'
            movVertical = 'none'            
            continue
        movHorizon = 'left'
        movVertical = 'none' 

    if(table[i][j] == '|' and asciiFlag == False):
        print(' | ')
        if not stack:
            movHorizon = 'none'
            movVertical = 'up'            
        continue
        movHorizon = 'none'
        movVertical = 'down'
        continue

    if(table[i][j] == '#' and asciiFlag == False):
        print(' # ')
        j += 1
        continue

    if(table[i][j] == '?' and asciiFlag == False):
        print(' ? ')
        movHorizon = random.choice(movHorizonArr)
        movVertical = random.choice(movVerticalArr)
        continue
 
    if(table[i][j] == '@' and asciiFlag == False):
        pointFlag = False
        print(' @ ',)
        continue
    
    # Constants
    if((table[i][j] == '1' or table[i][j] == '2' or table[i][j] == '3' or table[i][j] == '4' or table[i][j] == '5' or table[i][j] == '6' or table[i][j] == '7' or table[i][j] == '8' or table[i][j] == '9') and  asciiFlag == False):
        stack.append(int(table[i][j]))
        print('num i', table[i][j])
        continue

    if(table[i][j] == '0' and asciiFlag == False):
        stack.append(int(table[i][j]))
        continue

    if asciiFlag:
        stack.append(ord(table[i][j]))
        print('ord symbol', table[i][j])
        continue

    # stack
    if(table[i][j] == ':' and asciiFlag == False):
        headElement = stack[len(stack) - 1] 
        stack.append(headElement)           
        print('copy stack ', headElement)
        continue

    if(table[i][j] == '=' and asciiFlag == False):
        headElement = stack[len(stack) - 1] 
        childrenElement = stack[len(stack) - 2] 
        stack.pop()
        stack.pop()
        stack.append(headElement)
        stack.append(childrenElement)
        print('change stack ', childrenElement, headElement)
        continue

    if(table[i][j] == '$' and asciiFlag == False):
        stack.pop()           
        print('delete head stack ')
        continue

    # math
    if(table[i][j] == '+' and asciiFlag == False):
        headElement = stack[len(stack) - 1] 
        childrenElement = stack[len(stack) - 2]
        res = int(headElement)  + int(childrenElement)
        stack.pop()
        stack.pop()
        stack.append(res)
        print('sum of  ', headElement, childrenElement, res)
        continue

    if(table[i][j] == '-' and asciiFlag == False):
        headElement = stack[len(stack) - 1] 
        childrenElement = stack[len(stack) - 2]
        res = int(childrenElement) - int(headElement)  
        stack.pop()
        stack.pop()
        stack.append(res)
        print('minus of  ', headElement, childrenElement, res)
        continue

    if(table[i][j] == '*' and asciiFlag == False):
        headElement = stack[len(stack) - 1] 
        childrenElement = stack[len(stack) - 2]
        res = int(headElement) * int(childrenElement)
        stack.pop()
        stack.pop()
        stack.append(res)
        print('mul of  ', headElement, childrenElement, res)
        continue

    if(table[i][j] == '/' and asciiFlag == False):
        headElement = stack[len(stack) - 1] 
        childrenElement = stack[len(stack) - 2]
        res = int(childrenElement) / int(headElement)  
        stack.pop()
        stack.pop()
        stack.append(res)
        print('div of  ', headElement, childrenElement, res)
        continue

    if(table[i][j] == '%' and asciiFlag == False):
        headElement = stack[len(stack) - 1] 
        childrenElement = stack[len(stack) - 2]
        res = int(childrenElement) % int(headElement) 
        stack.pop()
        stack.pop()
        stack.append(res)
        print('div of  ', headElement, childrenElement, res)
        continue
    # Logic operations 
    if(table[i][j] == '!' and asciiFlag == False):
        headElement = stack[len(stack) - 1] 
        print(' ! ', headElement)
        if(headElement == 0):   
            print('dsadasdasdas')          
            stack.pop()
            stack.append(1) 
            continue    
        stack.pop()
        stack.append(0)
        continue    
    if(table[i][j] == '`' and asciiFlag == False):
        headElement = stack[len(stack) - 1] 
        childrenElement = stack[len(stack) - 2]
        if(childrenElement > headElement):
            stack.pop()
            stack.pop()
            stack.append(1)
            continue
        else:
            stack.pop()
            stack.pop()
            stack.append(0)    
            continue 

print('buffer to display is ', bufferEcho)
print('stack is ', stack)
print(echo(bufferEcho))

