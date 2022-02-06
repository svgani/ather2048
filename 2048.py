import random

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
                    li[i][j] = 0
    up(li)
    return

def downAdd(li):
    global score
    for j in range(4):
        for i in range(2,-1,-1):
            if li[3][j] != 0:
                if li[i+1][j] == li[i][j] and li[i][j]!=0:
                    flag[2] = 1
                    li[i+1][j] *= 2
                    score += li[i+1][j]
                    li[i][j] = 0
    down(li)
    return

def leftAdd(li):
    global score
    for i in range(4):
        for j in range(1,4):
            if li[i][0] != 0:
                if li[i][j-1] == li[i][j] and li[i][j]!=0:
                    flag[1] = 1
                    li[i][j-1] *= 2
                    score += li[i][j-1]
                    li[i][j] = 0
    left(li)
    return

def rightAdd(li):
    global score
    for i in range(4):
        for j in range(2,-1,-1):
            if li[i][3] != 0:
                if li[i][j+1] == li[i][j] and li[i][j]!=0:
                    flag[3] = 0
                    li[i][j+1] *= 2
                    score += li[i][j+1]
                    li[i][j] = 0
    right(li)
    return

def printBoard(li):
    print("\nScore:",score,end='')
    for x in li:
        print("\n-------------------------\n|",end='')
        for i in x:
            if i == 0:
                print('  ',' |',end='')
            else:
                print(' ',i,' |',end='')
    print("\n-------------------------\n",end='')
    return

def giveInput(li):
    t = input()
    if t == 'w' or t == 'W':
        up(li)
        upAdd(li)
        print(flag)
        if flag[0] == 0:
            print("up not possible")
            giveInput(li)
    elif t == 'a' or t == 'A':
        left(li)
        leftAdd(li)
        if flag[1] == 0:
            print("left not possible")
            giveInput(li)
    elif t == 's' or t == 'S':
        down(li)
        downAdd(li)
        if flag[2] == 0:
            print("down not possible")
            giveInput(li)
    elif t == 'd' or t == 'D':
        right(li)
        rightAdd(li)
        if flag[3] == 0:
            print("right not possible")
            giveInput(li)
    else:
        print("\nEnter correct character \nW --> up\nA --> left\nS --> down\nD --> right\n")
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
                # print("done","row: ",i,index1,j)
                index1+=1
        # print(li[j])
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
                # print("done","row: ",i,index1,j)
                index1+=1
        # print(li[i])
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
                # print("done","row: ",i,index1,j)
                index1-=1
        # print(li[i])
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
                # print("done","row: ",i,index1,j)
                index1-=1
        # print(li[j])
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
    return 1

li = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
fillPosition(li)
fillPosition(li)
while 1:
    printBoard(li)
    print("\nEnter \nW --> up\nA --> left\nS --> down\nD --> right\n")
    flag = [0,0,0,0]
    print(flag)
    giveInput(li)
    fillPosition(li)
    # printBoard(li)
    if gameOver(li):
        print("Thanks for playing")
        break