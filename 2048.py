import random
from sys import exit

score = 0
flag = [0,0,0,0]

def upAdd(li):
    global score
    for j in range(4):
        for i in range(1,4):
            if li[0][j] != 0:
                if li[i-1][j] == li[i][j] and li[i][j]!=0:
                    flag[0] = 1
                    li[i-1][j] *= 2
                    score += li[i-1][j]
                    if li[i-1][j] == 2048:
                        print("You Won!!!\nScore:",score)
                        exit()
                    li[i][j] = 0
    up(li)
    return

def testUpAdd(li):
    for j in range(4):
        for i in range(1,4):
            if li[0][j] != 0:
                if li[i-1][j] == li[i][j] and li[i][j]!=0:
                    return 0
    return 1

def downAdd(li):
    global score
    for j in range(4):
        for i in range(2,-1,-1):
            if li[3][j] != 0:
                if li[i+1][j] == li[i][j] and li[i][j]!=0:
                    flag[2] = 1
                    li[i+1][j] *= 2
                    score += li[i+1][j]
                    if li[i+1][j] == 2048:
                        print("You Won!!!\nScore:",score)
                        exit()
                    li[i][j] = 0
    down(li)
    return

def testDownAdd(li):
    for j in range(4):
        for i in range(2,-1,-1):
            if li[3][j] != 0:
                if li[i+1][j] == li[i][j] and li[i][j]!=0:
                    return 0
    return 1

def leftAdd(li):
    global score
    for i in range(4):
        for j in range(1,4):
            if li[i][0] != 0:
                if li[i][j-1] == li[i][j] and li[i][j]!=0:
                    flag[1] = 1
                    li[i][j-1] *= 2
                    score += li[i][j-1]
                    if li[i][j-1] == 2048:
                        print("You Won!!!\nScore:",score)
                        exit()
                    li[i][j] = 0
    left(li)
    return

def testLeftAdd(li):
    for i in range(4):
        for j in range(1,4):
            if li[i][0] != 0:
                if li[i][j-1] == li[i][j] and li[i][j]!=0:
                    return 0
    return 1

def rightAdd(li):
    global score
    for i in range(4):
        for j in range(2,-1,-1):
            if li[i][3] != 0:
                if li[i][j+1] == li[i][j] and li[i][j]!=0:
                    flag[3] = 1
                    li[i][j+1] *= 2
                    score += li[i][j+1]
                    if li[i][j+1] == 2048:
                        print("You Won!!!\nScore:",score)
                        exit()
                    li[i][j] = 0
    right(li)
    return

def testRightAdd(li):
    for i in range(4):
        for j in range(2,-1,-1):
            if li[i][3] != 0:
                if li[i][j+1] == li[i][j] and li[i][j]!=0:
                    return 0
    return 1

def printBoard(li):
    print("\nScore:",score,end='')
    for x in li:
        print("\n-----------------------------\n|",end='')
        for i in x:
            if i == 0:
                print('    ',' |',end='')
            else:
                print("%5d" % (i),'|',end='')
    print("\n-----------------------------\n",end='')
    return

def giveInput(li):
    t = input()
    if t == '3':
        up(li)
        upAdd(li)
        if flag[0] == 0:
            print("up not possible")
            giveInput(li)
    elif t == '1':
        left(li)
        leftAdd(li)
        if flag[1] == 0:
            print("left not possible")
            giveInput(li)
    elif t == '4':
        down(li)
        downAdd(li)
        if flag[2] == 0:
            print("down not possible")
            giveInput(li)
    elif t == '2':
        right(li)
        rightAdd(li)
        if flag[3] == 0:
            print("right not possible")
            giveInput(li)
    else:
        print("\nEnter Correct Number \n1 --> left\n2 --> right\n3 --> up\n4 --> down\n")
        giveInput(li)
    return

def up(li):
    for j in range(4):
        index1 = 0
        if li[0][j] != 0:
            index1+=1
        for i in range(1,4):
            if li[i][j] != 0:
                if index1<i:
                    flag[0] = 1
                    li[index1][j] = li[i][j]
                    li[i][j] = 0
                index1+=1
    return

def left(li):
    for i in range(4):
        index1 = 0
        if li[i][0] != 0:
            index1+=1
        for j in range(1,4):
            if li[i][j] != 0:
                if index1<j:
                    flag[1] = 1
                    li[i][index1] = li[i][j]
                    li[i][j] = 0
                index1+=1
    return

def right(li):
    for i in range(4):
        index1 = 3
        if li[i][3] != 0:
            index1-=1
        for j in range(2,-1,-1):
            if li[i][j] != 0:
                if index1>j:
                    flag[3] = 1
                    li[i][index1] = li[i][j]
                    li[i][j] = 0
                index1-=1
    return

def down(li):
    for j in range(4):
        index1 = 3
        if li[3][j] != 0:
            index1-=1
        for i in range(2,-1,-1):
            if li[i][j] != 0:
                if index1>i:
                    flag[2] = 1
                    li[index1][j] = li[i][j]
                    li[i][j] = 0
                index1-=1
    return

def randRC():
    r = random.choice([0,1,2,3])
    c = random.choice([0,1,2,3])
    return r,c

def fillPosition(li):
    while 1:
        r,c = randRC()
        if li[r][c] == 0:
            li[r][c] = random.choices([2,4], weights=(70, 30), k=1)[0]
            break
    return

def gameOver(li):
    for x in li:
        for i in x:
            if i == 0:
                return 0
    return (testUpAdd(li) and testDownAdd(li) and testLeftAdd(li) and testRightAdd(li))

# User will input 1, 2, 3, 4 for left, right, up and down movements

li = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
fillPosition(li)
fillPosition(li)
printBoard(li)
while 1:
    print("\nEnter \n1 --> left\n2 --> right\n3 --> up\n4 --> down\n")
    flag = [0,0,0,0]
    giveInput(li)
    fillPosition(li)
    printBoard(li)
    if gameOver(li):
        print("Thanks for playing\nScore:",score)
        break
    1