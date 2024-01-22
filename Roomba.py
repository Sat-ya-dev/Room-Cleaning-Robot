# Room Cleaning Robot
import numpy as np
import random
m = int(input("enter the number of rows "))
n = int(input("enter the number of columns "))
d=np.zeros((m,n))
count=0
while count<10:
    x = random.choice(range(m)) # randomly selecting x coordinate
    y = random.choice(range(n))  # randomly selecting y coordinate
    if(d[x][y]==0): # if the cell is empty only then increase count value and cell value updates to 1 - Initial setup
        d[x][y]+=1
        count+=1
print(d)

def agent(x,y,d,act): # x,y initial coordinates, d is the matrix, act is action performed
    fx=x  #fx corresponds to final x coordinate
    fy=y   #fy corresponds to final y coordinate
    if act=='up':
        if x==0: # first row
            score= -10 # hits wall
        else:
            fx = x - 1
            score=0
    elif act=='down':
        if x==m-1:  # last row
            score= -10  # hits wall
        else:
            fx = x+1
            score=0
    elif act=='right':
        if y==n-1:  # last column
            score= -10   # hits wall
        else:
            fy = y+1
            score=0
    elif act=='left':
        if y==0:  # first column
            score= -10  # hits wall
        else:
            fy=y-1
            score=0
    elif act=='pick':
        if d[x][y]==0:
            score= -1
        else:
            dirt = d[x][y]
            d[x][y]=0
            score = dirt
    l = [x,y,act,fx,fy,score]
    return l 
x = random.choice(range(m))
y = random.choice(range(n))
a = ['up','down','right','left','pick']
act = random.choice(a)
l=agent(x,y,d,act)
print("Initial value of x and y are : " + str(l[0])+" "+ str(l[1]))
print("action chosen is "+ l[2])
print("Final coordinates after performing action : "+str(l[3])+" "+str(l[4]))
print("Score is "+str(l[5]))
print(l)

x = random.choice(range(m))
y = random.choice(range(n))
print(x,y)
for i in range(1000):
    act = random.choice(a)
    print(act)
    l=agent(x,y,d,act)
    x=l[3] # final coordinate becomes initial coordinate for the next action
    y=l[4]
    print(d)
    print(l[5]) # score
    x1 = random.choice(range(m)) # at each instant of time a unit dirt is added to random cell
    y1 = random.choice(range(n))
    d[x1][y1]+=1
    print(" ")
    print("Current coordinates: ",x,y)