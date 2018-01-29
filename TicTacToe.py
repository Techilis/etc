# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 02:49:33 2018

@author: User
"""

#Tic Tae Toe
import random

def drawBoard(board):
    #To print out board
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input('Do you want to be X or O').upper()
        #First element = player, second element = computer
        if letter == 'X':
            return ['X','O']
        else:
            return ['O','X']

def whoGoesFirst():
    #Randomly choose
    if random.randint(0,1) == 1:
        return 'player'
    else:
        return 'computer'
        
def playAgain():
    #True is player want to play again
    return input('Do you want to play again? (yes or no)').lower()

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    #True is player wins, bo for board, le for letter
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or #top
    (bo[4] == le and bo[5] == le and bo[6] == le) or #middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or #bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or #left
    (bo[8] == le and bo[5] == le and bo[2] == le) or #middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or #right
    (bo[7] == le and bo[5] == le and bo[3] == le) or #diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) #diagonal
    
def getBoardCopy(board):
    #Make duplicate and return it
    dupeBoard = []
    
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, move):
    #Return true if move is free on board
    return board[move] == ' '

def getPlayerMove(board):
    #Get player's move
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board,movesList):
    #Returns valid move from list on board
    #Returns None if not vaid
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
        
def getComputerMove(board, computerLetter):
    #Given board and computer letter, determine where to move and return that move
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #First check if can win
    for i in range(1,10):
        copy = getBoardCopy(board)  
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    
    #Second check if player can win with their next move and block
    for i in range(1,10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
            
    #Third check for center, corner and space, in that order
    if isSpaceFree(board, 5):
        return 5
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
    
def isBoardFull(board):
    #Return true if full
    for i in range(1,10):
        if isSpaceFree(board, i):
            return False
    return True

#Start game
print('Welcome to Tic Tac Toe!')

while True:
    #Reset board
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            #Player's turn
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Congrats, you won')
                gameIsPlaying = False
                
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Game is drawn')
                    break
                else:
                    turn = 'computer'
        
        else:
            #Computer's turn
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('You lose')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('Drawn')
                    break
                else:
                    turn = 'player'
    if not playAgain():
        break
    
                
                
        
    
