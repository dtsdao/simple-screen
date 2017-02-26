"""
Simple Screen
By DTSDAO
2017.2.25
"""

print('=====================')
print('|   Simple Screen   |')
print('|    Version 1.0    |')
print('=====================')

# Define varibles
print('[INFO]Defining screen settings...')

screenList = list()
SCREEN_HEIGHT, SCREEN_WIDTH = 0, 0

#Get data
try:
    SCREEN_HEIGHT = int(input('[INPUT]Screen Height: '))
    SCREEN_WIDTH = int(input('[INPUT]Screen Width: '))
    #if SCREEN_HEIGHT > 50 or SCREEN_WIDTH > 70 or SCREEN_HEIGHT <= 0 or SCREEN_WIDTH <= 0:
    if SCREEN_HEIGHT <= 0 or SCREEN_WIDTH <= 0:
        raise ValueError()
except ValueError as e:
    print('[WARN]Unacceptable Values! Using default settings...')
    SCREEN_HEIGHT = 20
    SCREEN_WIDTH = 30
finally:
    print('[INFO]Final height: %d' % SCREEN_HEIGHT)
    print('[INFO]Final width: %d' % SCREEN_WIDTH)

# Make screen
input('Press enter to continue...')

for i in range(SCREEN_HEIGHT):
    screenList.append(list())
    for j in range(SCREEN_WIDTH):
        screenList[i].append('*')

import os
linePrint = ''
straightLine = ''

for i in range(SCREEN_WIDTH):
    straightLine += '='

#Show & Draw screen
while True:
    cls = os.system('cls')
    
    #Show screen
    for i in range(SCREEN_HEIGHT):
        for j in range(SCREEN_WIDTH):
            linePrint += screenList[i][j]
        print(linePrint)
        linePrint = ''
    print(straightLine)
    
    #Draw square
    print('[INPUT]Square starts in: ')
    try:
        squareStartPoint = (int(input('x: ')), int(input('y: ')))
        squareHeight = int(input('[INPUT]Square height: ')) - 1
        squareWidth = int(input('[INPUT]Square width: ')) - 1
        if squareHeight <= 0 or squareWidth <= 0 or squareStartPoint[0] < 0 or squareStartPoint[1] < 0:
            raise ValueError()
        
        squareMaterial = input('[INPUT]Fill with(char): ')
        if squareMaterial == '' or len(squareMaterial) > 1:
            raise ValueError()
    except ValueError as e:
        print('[WARN]Wrong data!')
        input('Press enter to continue...')
        continue
    
    for y in range(SCREEN_HEIGHT):
        for x in range(SCREEN_WIDTH):
            if squareStartPoint[1] <= y <= squareStartPoint[1] + squareHeight and \
                                    squareStartPoint[0] <= x <= squareStartPoint[0] + squareWidth:
                screenList[y][x] = squareMaterial

    print('[INFO]Make square successfully!')
    input('Press enter to continue...')
