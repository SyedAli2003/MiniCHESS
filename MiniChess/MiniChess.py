"""
CSD311 ARTIFICIAL INTELLIGENT
PROJECT

MINI CHESS

GROUP 1

MEMBERS:
SYED ALI KAMIL - 2010110670
KARTIKAY NAUTIYAL - 211011279
SRIMAHAGUHAN - 2010110648
"""

import pygame
import copy
import random
import numpy as np
import time
cScale = 4/3
class ChessBoard:
    boardLayout = [['r','n','q','k','n','r'],['p','p','p','p','p','p'],['0','0','0','0','0','0'],['0','0','0','0','0','0'],['P','P','P','P','P','P'],['R','N','Q','K','N','R']]
    toPutLocation = []
    allPawns = []
    toPutRect = []
    boxes = []
    currentLocation = []

    def __init__(self):
        self.boxes.append([((55*cScale, 135*cScale),(55*cScale, 135*cScale)),((135*cScale, 215*cScale),(55*cScale, 135*cScale)),((215*cScale, 295*cScale),(55*cScale, 135*cScale)),((295*cScale, 375*cScale),(55*cScale, 135*cScale)),((375*cScale, 455*cScale),(55*cScale, 135*cScale)),((455*cScale, 535*cScale),(55*cScale, 135*cScale))])
        self.boxes.append([((55*cScale, 135*cScale),(135*cScale, 215*cScale)),((135*cScale, 215*cScale),(135*cScale, 215*cScale)),((215*cScale, 295*cScale),(135*cScale, 215*cScale)),((295*cScale, 375*cScale),(135*cScale, 215*cScale)),((375*cScale, 455*cScale),(135*cScale, 215*cScale)),((455*cScale, 535*cScale),(135*cScale, 215*cScale))])
        self.boxes.append([((55*cScale, 135*cScale),(215*cScale, 295*cScale)),((135*cScale, 215*cScale),(215*cScale, 295*cScale)),((215*cScale, 295*cScale),(215*cScale, 295*cScale)),((295*cScale, 375*cScale),(215*cScale, 295*cScale)),((375*cScale, 455*cScale),(215*cScale, 295*cScale)),((455*cScale, 535*cScale),(215*cScale, 295*cScale))])
        self.boxes.append([((55*cScale, 135*cScale),(295*cScale, 375*cScale)),((135*cScale, 215*cScale),(295*cScale, 375*cScale)),((215*cScale, 295*cScale),(295*cScale, 375*cScale)),((295*cScale, 375*cScale),(295*cScale, 375*cScale)),((375*cScale, 455*cScale),(295*cScale, 375*cScale)),((455*cScale, 535*cScale),(295*cScale, 375*cScale))])
        self.boxes.append([((55*cScale, 135*cScale),(375*cScale, 455*cScale)),((135*cScale, 215*cScale),(375*cScale, 455*cScale)),((215*cScale, 295*cScale),(375*cScale, 455*cScale)),((295*cScale, 375*cScale),(375*cScale, 455*cScale)),((375*cScale, 455*cScale),(375*cScale, 455*cScale)),((455*cScale, 535*cScale),(375*cScale, 455*cScale))])
        self.boxes.append([((55*cScale, 135*cScale),(455*cScale, 535*cScale)),((135*cScale, 215*cScale),(455*cScale, 535*cScale)),((215*cScale, 295*cScale),(455*cScale, 535*cScale)),((295*cScale, 375*cScale),(455*cScale, 535*cScale)),((375*cScale, 455*cScale),(455*cScale, 535*cScale)),((455*cScale, 535*cScale),(455*cScale, 535*cScale))])

    def initialize(self, screen):
        toPutLocation = [[],[],[],[],[],[]]
        for i in range(6):
            for j in range(6):
                toPutLocation[j].append([57*cScale+(i*108), 47*cScale+(j*108)])
        self.toPutLocation = toPutLocation
        boardLayout = self.boardLayout
        screen.blit(gameB,(0,0))
        screen.blit(board,(50*cScale, 50*cScale))
        
        for i in range(6):
            for j in range(6):
                if boardLayout[i][j]=='P':
                    screen.blit(font.render("\u2659", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='K':
                    screen.blit(font.render("\u2654", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='R':
                    screen.blit(font.render("\u2656", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='N':
                    screen.blit(font.render("\u2658", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='Q':
                    screen.blit(font.render("\u2655", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='p':
                    screen.blit(font.render("\u265F", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='k':
                    screen.blit(font.render("\u265A", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='r':
                    screen.blit(font.render("\u265C", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='n':
                    screen.blit(font.render("\u265E", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='q':
                    screen.blit(font.render("\u265B", True, (0,0,0)),self.toPutLocation[i][j])

        
    def writer(self, outputBoard, screen, wTtime, bTtime):
        print("IN WRITER")
        boardLayout = outputBoard
        screen.blit(gameB,(0,0))
        screen.blit(board,(50*cScale, 50*cScale))
        screen.blit(timerBack,(260*cScale,5*cScale))
        screen.blit(timerBack,(260*cScale,555*cScale))
        screen.blit(tfont.render("%.2f"%bTtime, True, (255, 255, 255)), (265*cScale, 5*cScale))
        screen.blit(tfont.render("%.2f"%wTtime, True, (255, 255, 255)), (265*cScale, 555*cScale))
        for i in range(6):
            for j in range(6):
                if boardLayout[i][j]=='P':
                    screen.blit(font.render("\u2659", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='K':
                    screen.blit(font.render("\u2654", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='R':
                    screen.blit(font.render("\u2656", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='N':
                    screen.blit(font.render("\u2658", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='Q':
                    screen.blit(font.render("\u2655", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='p':
                    screen.blit(font.render("\u265F", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='k':
                    screen.blit(font.render("\u265A", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='r':
                    screen.blit(font.render("\u265C", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='n':
                    screen.blit(font.render("\u265E", True, (0,0,0)),self.toPutLocation[i][j])
                if boardLayout[i][j]=='q':
                    screen.blit(font.render("\u265B", True, (0,0,0)),self.toPutLocation[i][j])

chessBoard = ChessBoard()

mover=[]
class Generator:
    def kingcheck(self,T,c):
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        flg=0
        for i in range(0,6):
            for j in range(0,6):
                if T[i][j]=='k' and c==0:
                    flg=1
                    break
                if T[i][j]=='K'and c==1:
                    flg=1
                    break
            if flg==1:
                break
        if c==0:
            if i<5:
                if j<5:
                    if T[i+1][j+1]=='P':
                        return True
                    for k in range(j+1,6):
                        if T[i][k] in black or T[i][k] in ['K','N','P','B']:
                            break
                        if T[i][k]=='Q' or T[i][k]=='R':
                            return True
                    k=min(5-i,5-j)
                    for l in range(1,k+1):
                        if T[i+l][j+l] in black or T[i+l][j+l] in ['K','N','P','R']:
                            break
                        if T[i+l][j+l] in ['Q','B']:
                            return True
                if j>0:
                    if T[i+1][j-1]=='P':
                        return True
                    for k in reversed(range(0,j)):
                        if T[i][k] in black or T[i][k] in ['K','N','P','B']:
                            break
                        if T[i][k]=='Q' or T[i][k]=='R':
                            return True
                    k=min(5-i,j)
                    for l in range(1,k+1):
                        if T[i+l][j-l] in black or T[i+l][j-l] in ['K','N','P','R']:
                            break
                        if T[i+l][j-l] in ['Q','B']:
                            return True               
                for k in range(i+1,6):
                    if T[k][j] in black or T[k][j] in ['K','N','P','B']:
                        break
                    if T[k][j]=='Q' or T[k][j]=='R':
                        return True
            if i>0:
                if j<5:
                    for k in range(j+1,6):
                        if T[i][k] in black or T[i][k] in ['K','N','P','B']:
                            break
                        if T[i][k]=='Q' or T[i][k]=='R':
                            return True
                    k=min(i,5-j)
                    for l in range(1,k+1):
                        if T[i-l][j+l] in black or T[i-l][j+l] in ['K','N','P','R']:
                            break
                        if T[i-l][j+l] in ['Q','B']:
                            return True
                if j>0:
                    for k in reversed(range(0,j)):
                        if T[i][k] in black or T[i][k] in ['K','N','P','B']:
                            break
                        if T[i][k]=='Q' or T[i][k]=='R':
                            return True
                    k=min(i,j)
                    for l in range(1,k+1):
                        if T[i-l][j-l] in black or T[i-l][j-l] in ['K','N','P','R']:
                            break
                        if T[i-l][j-l] in ['Q','B']:
                            return True
                    
                for k in reversed(range(0,i)):
                    if T[k][j] in black or T[k][j] in ['K','N','P','B']:
                        break
                    if T[k][j]=='Q' or T[k][j]=='R':
                        return True
            J1=[[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1],[i+1,j+2],[i-1,j+2],[i+1,j-2],[i-1,j-2]]
            J2=[[i+1,j+1],[i+1,j-1],[i-1,j+1],[i-1,j-1],[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
            for k in J1:
                if 0<=k[0]<=5 and 0<=k[1]<=5:
                    if T[k[0]][k[1]]=='N':
                        return True
            for k in J2:
                if 0<=k[0]<=5 and 0<=k[1]<=5:
                    if T[k[0]][k[1]]=='K':
                        return True
        if c==1:
            if i<5:
                if j<5:
                    for k in range(j+1,6):
                        if T[i][k] in white or T[i][k] in ['k','n','p','b']:
                            break
                        if T[i][k]=='q' or T[i][k]=='r':
                            return True
                    k=min(5-i,5-j)
                    for l in range(1,k+1):
                        if T[i+l][j+l] in white or T[i+l][j+l] in ['k','n','p','r']:
                            break
                        if T[i+l][j+l] in ['q','b']:
                            return True
                if j>0:
                    for k in reversed(range(0,j)):
                        if T[i][k] in white or T[i][k] in ['k','n','p','b']:
                            break
                        if T[i][k]=='q' or T[i][k]=='r':
                            return True
                    k=min(5-i,j)
                    for l in range(1,k+1):
                        if T[i+l][j-l] in white or T[i+l][j-l] in ['k','n','p','r']:
                            break
                        if T[i+l][j-l] in ['q','b']:
                            return True                
                for k in range(i+1,6):
                    if T[k][j] in white or T[k][j] in ['k','n','p','b']:
                        break
                    if T[k][j]=='q' or T[k][j]=='r':
                        return True
            if i>0:
                if j<5:
                    if T[i-1][j+1]=='p':
                        return True
                    for k in range(j+1,6):
                        if T[i][k] in white or T[i][k] in ['k','n','p','b']:
                            break
                        if T[i][k]=='q' or T[i][k]=='r':
                            return True
                    k=min(i,5-j)
                    for l in range(1,k+1):
                        if T[i-l][j+l] in white or T[i-l][j+l] in ['k','n','p','r']:
                            break
                        if T[i-l][j+l] in ['q','b']:
                            return True
                if j>0:
                    if T[i-1][j-1]=='p':
                        return True
                    for k in reversed(range(0,j)):
                        if T[i][k] in white or T[i][k] in ['k','n','p','b']:
                            break
                        if T[i][k]=='q' or T[i][k]=='r':
                            return True
                    k=min(i,j)
                    for l in range(1,k+1):
                        if T[i-l][j-l] in white or T[i-l][j-l] in ['k','n','p','r']:
                            break
                        if T[i-l][j-l] in ['q','b']:
                            return True
                    
                for k in reversed(range(0,i)):
                    if T[k][j] in white or T[k][j] in ['k','n','p','b']:
                        break
                    if T[k][j]=='q' or T[k][j]=='r':
                        return True
            J1=[[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1],[i+1,j+2],[i-1,j+2],[i+1,j-2],[i-1,j-2]]
            J2=[[i+1,j+1],[i+1,j-1],[i-1,j+1],[i-1,j-1],[i,j+1],[i,j-1],[i+1,j],[i-1,j]]
            for k in J1:
                if 0<=k[0]<=5 and 0<=k[1]<=5:
                    if T[k[0]][k[1]]=='n':
                        return True
            for k in J2:
                if 0<=k[0]<=5 and 0<=k[1]<=5:
                    if T[k[0]][k[1]]=='k':
                        return True          
        return False
            
                
                
        
    def movleg(self,T,i,j,c):
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        s=[]
        if T[i][j]=='0':
            return s
        count=0
        for a in T:
            for b in a:
                if b=='k' or b=='K':
                    count=count+1
        if count==1:
            s.append(T)
            return s

        if c==0:
            if T[i][j]=='r' or T[i][j]=='q':
                for k in range(i+1,6):
                    if T[k][j] in white:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[k][j]=T[i][j]
                        s.append(M)
                        break
                    if T[k][j] in black:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[k][j]=T[i][j]
                    s.append(M)
                for k in range(j+1,6):
                    if T[i][k] in white:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i][k]=T[i][j]
                        s.append(M)
                        break
                    if T[i][k] in black:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[i][k]=T[i][j]
                    s.append(M)
                for k in reversed(range(0,i)):
                    if T[k][j] in white:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[k][j]=T[i][j]
                        s.append(M)
                        break
                    if T[k][j] in black:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[k][j]=T[i][j]
                    s.append(M)
                for k in reversed(range(0,j)):
                    if T[i][k] in white:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i][k]=T[i][j]
                        s.append(M)
                        break
                    if T[i][k] in black:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[i][k]=T[i][j]
                    s.append(M)
            
            if T[i][j]=='n':
                J=[[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1],[i+1,j+2],[i-1,j+2],[i+1,j-2],[i-1,j-2]]
                for k in range(0,8):
                    if(0<=J[k][0]<=5 and 0<=J[k][1]<=5):
                        if T[J[k][0]][J[k][1]] not in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J[k][0]][J[k][1]]=T[i][j]
                            s.append(M)
            
            
            if T[i][j]=='b' or T[i][j]=='q':
                J1=[[0],[0],[0],[0],[0]]
                J2=[[0],[0],[0],[0],[0]]
                J3=[[0],[0],[0],[0],[0]]
                J4=[[0],[0],[0],[0],[0]]
                for k in range(1,6):
                    J1[k-1]=[i+k,j+k]
                    J2[k-1]=[i+k,j-k]
                    J3[k-1]=[i-k,j+k]
                    J4[k-1]=[i-k,j-k]
                #print(J1)
                for k in range(0,5):
                    if(0<=J1[k][0]<=5 and 0<=J1[k][1]<=5):
                        if T[J1[k][0]][J1[k][1]] in black:
                            break
                        if T[J1[k][0]][J1[k][1]] in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J1[k][0]][J1[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J1[k][0]][J1[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J2[k][0]<=5 and 0<=J2[k][1]<=5):
                        if T[J2[k][0]][J2[k][1]] in black:
                            break
                        if T[J2[k][0]][J2[k][1]] in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J2[k][0]][J2[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J2[k][0]][J2[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J3[k][0]<=5 and 0<=J3[k][1]<=5):
                        if T[J3[k][0]][J3[k][1]] in black:
                            break
                        if T[J3[k][0]][J3[k][1]] in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J3[k][0]][J3[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J3[k][0]][J3[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J4[k][0]<=5 and 0<=J4[k][1]<=5):
                        if T[J4[k][0]][J4[k][1]] in black:
                            break
                        if T[J4[k][0]][J4[k][1]] in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J4[k][0]][J4[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J4[k][0]][J4[k][1]]=T[i][j]
                        s.append(M)
            
            if(T[i][j]=='p'):
                if(i<5 and T[i+1][j] not in white and T[i+1][j] not in black):
                    if(i+1==5):
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i+1][j]='q'
                        s.append(M)
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i+1][j]='r'
                        s.append(M)
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i+1][j]='n'
                        s.append(M)
                    else:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i+1][j]='p'
                        s.append(M)
                if(i<5):
                    if(j<5):
                        if(T[i+1][j+1] in white):
                            if(i+1==5):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j+1]='q'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j+1]='r'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j+1]='n'
                                s.append(M)
                            else:
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j+1]='p'
                                s.append(M)
                                
                    if(j>0):
                        if(T[i+1][j-1] in white):
                            if(i+1==5):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j-1]='q'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j-1]='r'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j-1]='n'
                                s.append(M)
                            else:
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+1][j-1]='p'
                                s.append(M)
                    
                    
            
            if(T[i][j]=='k'):
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        if 0<=i+k<=5 and 0<=j+l<=5:
                            if(T[i+k][j+l] not in black):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+k][j+l]=T[i][j]
                                s.append(M)
                                
            return(s)

        if c==1:
            if T[i][j]=='R' or T[i][j]=='Q':
                for k in range(i+1,6):
                    if T[k][j] in black:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[k][j]=T[i][j]
                        s.append(M)
                        break
                    if T[k][j] in white:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[k][j]=T[i][j]
                    s.append(M)
                for k in range(j+1,6):
                    if T[i][k] in black:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i][k]=T[i][j]
                        s.append(M)
                        break
                    if T[i][k] in white:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[i][k]=T[i][j]
                    s.append(M)
                for k in reversed(range(0,i)):
                    if T[k][j] in black:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[k][j]=T[i][j]
                        s.append(M)
                        break
                    if T[k][j] in white:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[k][j]=T[i][j]
                    s.append(M)
                for k in reversed(range(0,j)):
                    if T[i][k] in black:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i][k]=T[i][j]
                        s.append(M)
                        break
                    if T[i][k] in white:
                        break
                    M=copy.deepcopy(T)
                    M[i][j]='0'
                    M[i][k]=T[i][j]
                    s.append(M)
            
            if T[i][j]=='N':
                J=[[i+2,j+1],[i+2,j-1],[i-2,j+1],[i-2,j-1],[i+1,j+2],[i-1,j+2],[i+1,j-2],[i-1,j-2]]
                for k in range(0,8):
                    if(0<=J[k][0]<=5 and 0<=J[k][1]<=5):
                        if T[J[k][0]][J[k][1]] not in white:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J[k][0]][J[k][1]]=T[i][j]
                            s.append(M)
            
            
            if T[i][j]=='B' or T[i][j]=='Q':
                J1=[[0],[0],[0],[0],[0]]
                J2=[[0],[0],[0],[0],[0]]
                J3=[[0],[0],[0],[0],[0]]
                J4=[[0],[0],[0],[0],[0]]
                for k in range(1,6):
                    J1[k-1]=[i+k,j+k]
                    J2[k-1]=[i+k,j-k]
                    J3[k-1]=[i-k,j+k]
                    J4[k-1]=[i-k,j-k]
                #print(J1)
                for k in range(0,5):
                    if(0<=J1[k][0]<=5 and 0<=J1[k][1]<=5):
                        if T[J1[k][0]][J1[k][1]] in white:
                            break
                        if T[J1[k][0]][J1[k][1]] in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J1[k][0]][J1[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J1[k][0]][J1[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J2[k][0]<=5 and 0<=J2[k][1]<=5):
                        if T[J2[k][0]][J2[k][1]] in white:
                            break
                        if T[J2[k][0]][J2[k][1]] in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J2[k][0]][J2[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J2[k][0]][J2[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J3[k][0]<=5 and 0<=J3[k][1]<=5):
                        if T[J3[k][0]][J3[k][1]] in white:
                            break
                        if T[J3[k][0]][J3[k][1]] in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J3[k][0]][J3[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J3[k][0]][J3[k][1]]=T[i][j]
                        s.append(M)
                for k in range(0,5):
                    if(0<=J4[k][0]<=5 and 0<=J4[k][1]<=5):
                        if T[J4[k][0]][J4[k][1]] in white:
                            break
                        if T[J4[k][0]][J4[k][1]] in black:
                            M=copy.deepcopy(T)
                            M[i][j]='0'
                            M[J4[k][0]][J4[k][1]]=T[i][j]
                            s.append(M)
                            break
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[J4[k][0]][J4[k][1]]=T[i][j]
                        s.append(M)
            
            if(T[i][j]=='P'):
                if(i>0 and T[i-1][j] not in white and T[i-1][j] not in black):
                    if(i-1==0):
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i-1][j]='Q'
                        s.append(M)
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i-1][j]='R'
                        s.append(M)
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i-1][j]='N'
                        s.append(M)
                    else:
                        M=copy.deepcopy(T)
                        M[i][j]='0'
                        M[i-1][j]='P'
                        s.append(M)
                if(i>0):
                    if(j<5):
                        if(T[i-1][j+1] in black):
                            if(i-1==0):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j+1]='Q'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j+1]='R'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j+1]='N'
                                s.append(M)
                            else:
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j+1]='P'
                                s.append(M)
                    if(j>0):
                        if(T[i-1][j-1] in black):
                            if(i-1==0):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j-1]='Q'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j-1]='R'
                                s.append(M)
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j-1]='N'
                                s.append(M)
                            else:
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i-1][j-1]='P'
                                s.append(M)
            
            if(T[i][j]=='K'):
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        if 0<=i+k<=5 and 0<=j+l<=5:
                            if(T[i+k][j+l] not in white):
                                M=copy.deepcopy(T)
                                M[i][j]='0'
                                M[i+k][j+l]=T[i][j]
                                s.append(M)
            
            
            for z in s:
                count=0
                for a in z:
                    for b in a:
                        if b=='k' or b=='K':
                            count=count+1
                if count==1:
                    #print("Here")
                    s=[]
                    s.append(z)
                    return s
                
                
                
            return(s)
                        

    def minmax(self,T,c,d,n):
        Y=Generator()
        if n==d:
            legal=[]
            rand=[]
            if(c==1):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.gvalu(legal[i],c)
                    if V>M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(c==0):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.gvalu(legal[i],c)
                    if V<M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(n==1):
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                    
                #return random.choice(rand)
            else:
                return M
        else:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax(legal[i],(c+1)%2,d,n+1)
                    if V>M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax(legal[i],(c+1)%2,d,n+1)
                    if V<M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if n==1:
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    
                    while legal!=[]:
                        print(legal[0])
                        print(Y.kingcheck(legal[0], c))
                        print("")
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M



    def minmax3(self,T,c,d,n,a,b):
        Y=Generator()
        if n==1 and n!=d:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax3(legal[i],(c+1)%2,d,n+1,a,b)
                    if V>M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax3(legal[i],(c+1)%2,d,n+1,a,b)
                    if V<M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if n==1:
                G=random.choice(rand)
                while (Y.kingcheck(G, c) and G!=[]) or (Y.kingcheck(G,(c+1)%2)==False and Y.minmax3(G,(c+1)%2,1,1,-90000,90000)==G) or (mover.count(G)==2 and c==0 and Y.evalu(G, c)<0) or (mover.count(G)==2 and c==1 and Y.evalu(G, c)>0):
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M
            
        if n==d:
            legal=[]
            rand=[]
            if(c==1):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.gvalu(legal[i],c)
                    m=M
                    if V>M:
                        M=V
                    if M>a:
                        a=M
                    #M=max(V,M)
                    #a=max(a,M)
                    if n==1:
                        if V>m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break

            if(c==0):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.gvalu(legal[i],c)
                    m=M
                    if V<M:
                        M=V
                    if M<b:
                        b=M
                    #M=min(V,M)
                    #b=min(b,M)
                    if n==1:
                        if V<m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
            if(n==1):
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                    
                #return random.choice(rand)
            else:
                return M
        else:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax3(legal[i],(c+1)%2,d,n+1,a,b)
                    m=M
                    if V>M:
                        M=V
                    if M>a:
                        a=M
                    #M=max(V,M)
                    #a=max(a,M)
                    if n==1:
                        if V>m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if (b<=a):
                        break
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax3(legal[i],(c+1)%2,d,n+1,a,b)
                    m=M
                    if V<M:
                        M=V
                    if M<b:
                        b=M
                    #M=min(V,M)
                    #b=min(b,M)
                    if n==1:
                        if V<m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
            if n==1:
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M
    
    def minmax4(self,T,c,d,n,a,b):
        Y=Generator()
        if n==1 and n!=d:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax4(legal[i],(c+1)%2,d,n+1,a,b)
                    if V>M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax4(legal[i],(c+1)%2,d,n+1,a,b)
                    if V<M:
                        rand=[]
                        M=V
                        k=i
                        rand.append(legal[k])
                    elif V==M:
                        rand.append(legal[i])
            if n==1:
                G=random.choice(rand)
                while (Y.kingcheck(G, c) and G!=[]) or (Y.kingcheck(G,(c+1)%2)==False and Y.minmax4(G,(c+1)%2,1,1,-90000,90000)==G) or (mover.count(G)==2 and c==0 and Y.gvalu(G, c)<0) or (mover.count(G)==2 and c==1 and Y.gvalu(G, c)>0):
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                    
                    
                if G==[]:
                    
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M
            
        if n==d:
            legal=[]
            rand=[]
            if(c==1):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.evalu(legal[i],c)
                    m=M
                    if V>M:
                        M=V
                    if M>a:
                        a=M
                    #M=max(V,M)
                    #a=max(a,M)
                    if n==1:
                        if V>m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
    
            if(c==0):
                for i in range(0,6):
                    for j in range(0,6):
                        s=Y.movleg(T,i,j,c)
                        for k in range(0,len(s)):
                            legal.append(s[k])
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.evalu(legal[i],c)
                    m=M
                    if V<M:
                        M=V
                    if M<b:
                        b=M
                    #M=min(V,M)
                    #b=min(b,M)
                    if n==1:
                        if V<m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
            if(n==1):
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                    
                #return random.choice(rand)
            else:
                return M
        else:
            legal=[]
            rand=[]
            for i in range(0,6):
                for j in range(0,6):
                    s=Y.movleg(T,i,j,c)
                    for k in range(0,len(s)):
                        legal.append(s[k])
            if(c==1):
                k=0
                M=-9000
                for i in range(0,len(legal)):
                    V=Y.minmax4(legal[i],(c+1)%2,d,n+1,a,b)
                    m=M
                    if V>M:
                        M=V
                    if M>a:
                        a=M
                    #M=max(V,M)
                    #a=max(a,M)
                    if n==1:
                        if V>m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if (b<=a):
                        break
            if(c==0):
                k=0
                M=9000
                for i in range(0,len(legal)):
                    V=Y.minmax4(legal[i],(c+1)%2,d,n+1,a,b)
                    m=M
                    if V<M:
                        M=V
                    if M<b:
                        b=M
                    #M=min(V,M)
                    #b=min(b,M)
                    if n==1:
                        if V<m:
                            rand=[]
                            m=V
                            k=i
                            rand.append(legal[k])
                        elif V==m:
                            rand.append(legal[i])
                    if(b<=a):
                        break
            if n==1:
                G=random.choice(rand)
                while Y.kingcheck(G, c) and G!=[]:
                    rand.remove(G)
                    legal.remove(G)
                    if rand==[]:
                        G=[]
                        break
                    G=random.choice(rand)
                if G==[]:
                    
                    while legal!=[]:
                        if(Y.kingcheck(legal[0], c)):
                            legal.remove(legal[0])
                        else:
                            if legal[0]!=T:
                                return legal[0]
                            else: legal.remove(T)
                    return T
                return G
                #return random.choice(rand)
            else:
                return M            

        
                                    

    def game(self,T,c):
        Y=Generator()
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        legal=[]
        str=""
        if(c==1):
            print("White's Move")
            G=Y.minmax4(T, c, 4, 1,-90000,90000)
        else:
            print("Black's Move")
            G=Y.minmax3(T, c, 4, 1,-90000,90000)
        mover.append(G)
        if len(mover)>10:
            mover.pop(0)
        for i in range(0,6):
            print(G[i])
            for j in range(0,6):
                str=str+G[i][j]
                str=str+" "
            if i!=5:
                str=str+","
        return str

    def gvalu(self,T,c): 
        e=0
        v=[5,3,3,9,90,1]
        V=[5,3,3,9,90,1]
        if c==0:
            V[4]=900
        if c==1:
            v[4]=900
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        b=[[1,1,1,1,1,1],[1,1.1,1.1,1.1,1.1,1],[1,1.2,1.2,1.2,1.2,1],[1.1,1.3,1.3,1.3,1.3,1.1],[1.5,1.5,1.5,1.5,1.5,1.5],[1,1,1,1,1,1]]
        br=[[1,1,1,1,1,1],[0.9,0.9,0.9,0.9,0.9,0.9],[0.8,0.8,0.8,0.8,0.8,0.8],[0.8,0.8,0.8,0.8,0.8,0.8],[1.1,1.1,1.1,1.1,1.1,1.1],[1,1,1,1,1,1]]
        bn=[[1,1,1,1,1,1],[1,1.01,1.01,1.01,1.01,1],[1,1.01,1.01,1.01,1.01,1],[1.2,1.3,1.3,1.3,1.3,1.2],[1,1.1,1.1,1.1,1.1,1],[1,1,1,1,1,1,1]]
        B=[[1,1,1,1,1,1],[1.5,1.5,1.5,1.5,1.5,1.5],[1.1,1.3,1.3,1.3,1.3,1.1],[1,1.2,1.2,1.2,1.2,1],[1,1.1,1.1,1.1,1.1,1],[1,1,1,1,1,1]]
        BR=[[1,1,1,1,1,1],[1.1,1.1,1.1,1.1,1.1,1.1],[0.8,0.8,0.8,0.8,0.8,0.8],[0.8,0.8,0.8,0.8,0.8,0.8],[0.9,0.9,0.9,0.9,0.9,0.9],[1,1,1,1,1,1]]
        BN=[[1, 1, 1, 1, 1, 1, 1],[1, 1.1, 1.1, 1.1, 1.1, 1],[1.2, 1.3, 1.3, 1.3, 1.3, 1.2],[1, 1.01, 1.01, 1.01, 1.01, 1],[1, 1.01, 1.01, 1.01, 1.01, 1],[1, 1, 1, 1, 1, 1]]
        for i in range(0,6):
            for j in range(0,6):
                for k in range(0,6):
                    if T[i][j]==black[k]:
                        if T[i][j]=='p':
                            e=e-v[k]*b[i][j]
                        
                        #elif T[i][j]=='r':
                            #e=e-v[k]*br[i][j]
                            
                        elif T[i][j]=='n':
                            e=e-v[k]*bn[i][j]
                        else:
                            e=e-v[k]
                    if T[i][j]==white[k]:
                        if T[i][j]=='P':
                            e=e+V[k]*B[i][j]
                        #elif T[i][j]=='R':
                            #e=e+V[k]*BR[i][j]
                        elif T[i][j]=='N':
                            e=e+V[k]*BN[i][j]
                        else:
                            e=e+V[k]
        return(e)
    def evalu(self,T,c):
        e=0
        v=[5,3,3,9,90,1]
        V=[5,3,3,9,90,1]
        if c==0:
            V[4]=900
        if c==1:
            v[4]=900
        black=['r','n','b','q','k','p']
        white=['R','N','B','Q','K','P']
        b=[[1,1,1,1,1,1],[1,1.1,1.1,1.1,1.1,1],[1,1.2,1.2,1.2,1.2,1],[1.1,1.3,1.3,1.3,1.3,1.1],[1.5,1.5,1.5,1.5,1.5,1.5],[1,1,1,1,1,1]]
        br=[[1,1,1,1,1,1],[0.9,0.9,0.9,0.9,0.9,0.9],[0.8,0.8,0.8,0.8,0.8,0.8],[0.8,0.8,0.8,0.8,0.8,0.8],[1.1,1.1,1.1,1.1,1.1,1.1],[1,1,1,1,1,1]]
        bn=[[1,1,1,1,1,1],[1,1.01,1.01,1.01,1.01,1],[1,1.01,1.01,1.01,1.01,1],[1.2,1.3,1.3,1.3,1.3,1.2],[1,1.1,1.1,1.1,1.1,1],[1,1,1,1,1,1,1]]
        B=[[1,1,1,1,1,1],[1.5,1.5,1.5,1.5,1.5,1.5],[1.1,1.3,1.3,1.3,1.3,1.1],[1,1.2,1.2,1.2,1.2,1],[1,1.1,1.1,1.1,1.1,1],[1,1,1,1,1,1]]
        BR=[[1,1,1,1,1,1],[1.1,1.1,1.1,1.1,1.1,1.1],[0.8,0.8,0.8,0.8,0.8,0.8],[0.8,0.8,0.8,0.8,0.8,0.8],[0.9,0.9,0.9,0.9,0.9,0.9],[1,1,1,1,1,1]]
        BN=[[1, 1, 1, 1, 1, 1, 1],[1, 1.1, 1.1, 1.1, 1.1, 1],[1.2, 1.3, 1.3, 1.3, 1.3, 1.2],[1, 1.01, 1.01, 1.01, 1.01, 1],[1, 1.01, 1.01, 1.01, 1.01, 1],[1, 1, 1, 1, 1, 1]]
        for i in range(0,6):
            for j in range(0,6):
                for k in range(0,6):
                    if T[i][j]==black[k]:
                        if T[i][j]=='p':
                            e=e-v[k]*b[i][j]
                        
                        #elif T[i][j]=='r':
                            #e=e-v[k]*br[i][j]
                            
                        elif T[i][j]=='n':
                            e=e-v[k]*bn[i][j]
                        else:
                            e=e-v[k]
                    if T[i][j]==white[k]:
                        if T[i][j]=='P':
                            e=e+V[k]*B[i][j]
                        #elif T[i][j]=='R':
                            #e=e+V[k]*BR[i][j]
                        elif T[i][j]=='N':
                            e=e+V[k]*BN[i][j]
                        else:
                            e=e+V[k]
        return(e)

T=[['r','n','q','k','n','r'],['p','p','p','p','p','p'],['0','0','0','0','0','0'],['0','0','0','0','0','0'],['P','P','P','P','P','P'],['R','N','Q','K','N','R']]




#Initialize the pygame
pygame.init()


#Create the screen
screen = pygame.display.set_mode((800,800))

pygame.display.set_caption("MINI CHESS!")
icon = pygame.image.load('Chess_Logo.png')
pygame.display.set_icon(icon)

bg = pygame.image.load("images/Main Menu.png")
bg = pygame.transform.scale(bg, (600*cScale, 600*cScale))
bg01 = pygame.image.load("images/Main Menu 01.png")
bg01 = pygame.transform.scale(bg01, (600*cScale, 600*cScale))
bg02 = pygame.image.load("images/Main Menu 02.png")
bg02 = pygame.transform.scale(bg02, (600*cScale, 600*cScale))
bg03 = pygame.image.load("images/Main Menu 03.png")
bg03 = pygame.transform.scale(bg03, (600*cScale, 600*cScale))
howToPlay = pygame.image.load("images/How To Play.png")
howToPlay = pygame.transform.scale(howToPlay, (600*cScale, 600*cScale))
howToPlay01 = pygame.image.load("images/How To Play 01.png")
howToPlay01 = pygame.transform.scale(howToPlay01, (600*cScale, 600*cScale))
timerBack = pygame.image.load("images/timerBack.png")
timerBack = pygame.transform.scale(timerBack, (80*cScale,40*cScale))
timerEndB = pygame.image.load("images/timerEndB.png")
timerEndB = pygame.transform.scale(timerEndB, (300*cScale,60*cScale))
timerEndW = pygame.image.load("images/timerEndW.png")
timerEndW = pygame.transform.scale(timerEndW, (300*cScale,60*cScale))
gameB = pygame.image.load("bg.jpg")
board = pygame.image.load("Board2.png")
board = pygame.transform.scale(board, (500*cScale, 500*cScale))
font = pygame.font.Font('seguisym.ttf', int(80*cScale))
tfont = pygame.font.Font('seguisym.ttf', int(30*cScale))



                






#GAME LOOP
inMenu = True
inHowToPlay = False
running = True
active_pawn = None
updateScreen = True
counter = True


T=[[0],[0],[0],[0],[0],[0]]
str= "r n q k n r ,p p p p p p ,0 0 0 0 0 0 ,0 0 0 0 0 0 ,P P P P P P ,R N Q K N R ,"
lst1=str.split(",")
for j in range(0,6):
        T[j]=lst1[j].split()
Y=Generator()

playerChance = 0
bTtime = 90
wTtime = 90
CLOCK = pygame.time.Clock()


#Main loop

while running:
    
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(mouse[0]>=100*cScale and mouse[0]<=498*cScale and mouse[1]>=172*cScale and mouse[1]<=252*cScale and inMenu):
                print("PLAYING AGAINST AI!")
                screen.blit(gameB,(0,0))
                screen.blit(board,(50*cScale, 50*cScale))
                chessBoard.initialize(screen)
                inMenu = False
            if(mouse[0]>=100*cScale and mouse[0]<=498*cScale and mouse[1]>=259*cScale and mouse[1]<=339*cScale and inMenu):
                print("PLAYING AGAINST HUMAN!")
            if(mouse[0]>=100*cScale and mouse[0]<=498*cScale and mouse[1]>=405*cScale and mouse[1]<=488*cScale and inHowToPlay):
                screen.blit(bg, (0,0))
                inHowToPlay = False
            if(mouse[0]>=100*cScale and mouse[0]<=498*cScale and mouse[1]>=346*cScale and mouse[1]<=427*cScale and inMenu):
                screen.blit(howToPlay, (0,0))
                inHowToPlay = True
            print(mouse)
        if (event.type == pygame.MOUSEBUTTONDOWN and not inMenu):
            buttonDownBox = []
            previousLocation = []
            whichPawn = -1
            for row in chessBoard.boxes:
                for box in row:
                    if(mouse[0]>=box[0][0] and mouse[0]<=box[0][1] and mouse[1]>=box[1][0] and mouse[1]<=box[1][1]):
                        buttonDownBox = [chessBoard.boxes.index(row), row.index(box)]
                        for i in chessBoard.currentLocation:
                            if(i[0]>=box[0][0] and i[0]<=box[0][1] and i[1]>=box[1][0] and i[1]<=box[1][1]):
                                previousLocation = i
                                whichPawn = chessBoard.currentLocation.index(i)
                        break
            updateScreen = True
            #print("b = ", buttonDownBox, "Pawn = ", chessBoard.allPawnText[whichPawn])
        
        if(event.type == pygame.MOUSEMOTION and inMenu):
            if(inHowToPlay):
                if(mouse[0]>=100*cScale and mouse[0]<=498*cScale and mouse[1]>=405*cScale and mouse[1]<=488*cScale):
                    screen.blit(howToPlay01, (0,0))
                else:
                    screen.blit(howToPlay, (0,0))
            elif(mouse[0]>=100*cScale and mouse[0]<=498*cScale and mouse[1]>=172*cScale and mouse[1]<=252*cScale):
                screen.blit(bg01, (0,0))
            elif(mouse[0]>=100*cScale and mouse[0]<=498*cScale and mouse[1]>=259*cScale and mouse[1]<=339*cScale):
                screen.blit(bg02, (0,0))
            elif(mouse[0]>=100*cScale and mouse[0]<=498*cScale and mouse[1]>=346*cScale and mouse[1]<=427*cScale):
                screen.blit(bg03, (0,0))
            else:
                screen.blit(bg, (0,0))
            
            
    if inMenu and counter:
        counter = False
        screen.blit(bg,(0,0))
    
    pygame.display.update()
    
    if not inMenu and playerChance<20000:
        if(playerChance == 0):
            btime = time.time()
            wtime = time.time()
        str=Y.game(T,(playerChance+1)%2)
        if((playerChance+1)%2 == 1):
            btime = time.time()
            wtime = time.time() - wtime
            wTtime = round(wTtime - wtime,2)
            if(wTtime <= 0):
                screen.blit(timerEndB, (150*cScale,265*cScale))
                pygame.display.update()
                time.sleep(20)
                pygame.display.quit()
                print("Time Over! Black Won")
                break
        else:
            wtime = time.time()
            btime = time.time() - btime
            bTtime = round(bTtime - btime,2)
            if(bTtime <= 0):
                screen.blit(timerEndW, (150*cScale,265*cScale))
                pygame.display.update()
                time.sleep(20)
                pygame.display.quit()
                print("\n\nTime Over! White Won")
                break
        K=[[0],[0],[0],[0],[0],[0]]
        lst1=str.split(",")
        for j in range(0,6):
            K[j]=lst1[j].split()

        if(T==K):
            if(Y.kingcheck(T,0)):
                print("\n\nWHITE WON")
            elif(Y.kingcheck(T,1)):
                print("\n\nBLACK WON")
            time.sleep(20)
            pygame.display.quit()
            break
        else:
            T = copy.deepcopy(K)
        countZ = 0
        for i in T:
            for j in i:
                if(i=="0"):
                    countZ+=1
        if(countZ==34):
            print("\n\nDraw!")
            time.sleep(20)
            pygame.display.quit()
            break
        chessBoard.writer(T, screen, wTtime, bTtime)
        playerChance+=1;
        
    pygame.display.update()


