# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 15:28:34 2020

@author: a0767
"""

   

def printboard(vector):
    vector1=[]
    for i in range(len(vector)):
        if vector[i]==0:
            vector1.append("o")
        elif vector[i]==1:
            vector1.append("x")
        else:
            vector1.append(" ")
    
    print(vector1[0],"----------------",vector1[1],"------------------",vector1[2])
    print("    ",vector1[8],"----------",vector1[9],"-----------",vector1[10],"    ")
    print("        ",vector1[16],"------",vector1[17],"------",vector1[18],"         ")
    print(vector1[7],"--",vector1[15],"-",vector1[23],"               ",vector1[19],"--",vector1[11],"---",vector1[3])
    print("        ",vector1[22],"------",vector1[21],"------",vector1[20],"         ")
    print("    ",vector1[14],"----------",vector1[13],"-----------",vector1[12],"    ")
    print(vector1[6],"----------------",vector1[5],"------------------",vector1[4])
    

vec=[0,0,0,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
vector=[]
for i in range(24):
    vector.append(-1)


#printboard(vec)
def heuristic(vector,player):
    value=0
    for i in range(0,3,24):
        if(vector[i]==vector[i+1] and vector[i]==vector[i+2] and vector[i]==1  ):
            value+=10
    for i in range(8):
        if(vector[i]==vector[i+8] and vector[i]==vector[i+2*8]and vector[i]==1):
            value+=10
    for i in range(0,3,24):
        if(vector[i]==vector[i+1] and vector[i]==vector[i+2] and vector[i]==0):
            value-=10
    for i in range(8):
        if(vector[i]==vector[i+8] and vector[i]==vector[i+2*8]and vector[i]==0):
            value-=10

    return value
    
    
#vector is the current laout on the borard
#dept is how many moves in the futures we should look for
#turn is an integer for checking in what game stae we are
#player represent minimizing of maximizing player
#alpha and beta are things    

def minmaxstart(vector,depth,turn,player,alpha,beta):
    if depth==0 :
        return heuristic(vector,player)  #returns evaluation for bootom node
    if player==1:#this is maximizing player
        value=-10000000000
        for i in range(len(vector)):
            if(vector[i]<0):
                vector[i]=1
                value=max(value,minmaxstart(vector,depth-1,turn+1,0,alpha,beta))
                vector[i]=-1
                alpha=max(alpha,value)
                if alpha>=beta:
                    break
        return value
    else:
        value=10000000000
        for i in range(len(vector)):
            if(vector[i]<0):
                newVec=vector
                newVec[i]=0
                value=min(value,minmaxstart(newVec,depth-1,turn+1,1,alpha,beta))
                newVec[i]=-1
                beta=min(beta,value)
                if alpha>=beta:
                    break
        return value
    
    #player är 1 eller 0
    #returns best move that is an integer representing a place in the vector wher the next
    #pice shuld be placed.
def findNextMove(vector,player,turn):

    bestMove = 0
    bestMoveVal=0
    currentMove=0
    newVec=[]
    for i in range(len(vector)):
        if(vector[i]<0):
            newVec=vector
            newVec[i]=player
            currentMove=minmaxstart(newVec,4,turn,player,-10000000,1000000000)
            newVec[i]=-1
            if(bestMoveVal<currentMove):
                bestMove=i
    return bestMove

            
            

#test=findNextMove(vector,1,0)
#printboard(vector)

for k in range(1,15):
    player=k%2
    move=findNextMove(vector,1,k)
    print(vector)
    print(move)
    vector[move]=player
    print(vector)
    printboard(vector)
    print("\n \n \n")
        
            
    
    

    
#function alphabeta(node, depth, α, β, maximizingPlayer) is
#    if depth = 0 or node is a terminal node then
#        return the heuristic value of node
#    if maximizingPlayer then
#        value := −∞
#        for each child of node do
#            value := max(value, alphabeta(child, depth − 1, α, β, FALSE))
#            α := max(α, value)
#            if α ≥ β then
#                break (* β cut-off *)
#        return value
#    else
#        value := +∞
#        for each child of node do
#            value := min(value, alphabeta(child, depth − 1, α, β, TRUE))
#            β := min(β, value)
#            if α ≥ β then
#                break (* α cut-off *)
#        return value