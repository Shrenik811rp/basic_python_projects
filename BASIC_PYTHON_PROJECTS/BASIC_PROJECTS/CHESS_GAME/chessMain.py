'''
Main driver files
handle user input and displaying current game status
'''

import pygame as p
from pygame.constants import KEYDOWN
import chessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8 # nos of rows and columns 

SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

IMAGES ={}


'''
Loading images only once into a dictionary
'''

def loadImages():
    pieces = ['bB','bK','bN','bp','bQ','bR',
    'wB','wK','wN','wp','wQ','wR']

    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png") , (SQ_SIZE,SQ_SIZE))


'''
The main driver updates graphics and user input
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH,HEIGHT))
    clock = p.time.Clock()

    #base color is white
    screen.fill(p.Color('white'))
    #calling the gameState function from chessEngine
    gmState = chessEngine.gameState()



    '''valid moves'''
    validMoves = gmState.getValidMoves()

    '''when valid move made generate new valid moves 
    until user doesnt make a valid move dont set moveMade to true'''

    #flag variable when move is made
    moveMade = False


    #print(gmState.board)
    loadImages() #call only once before while loop

    #while user doesnt quit keep looping
    running = True

    #what square is selected as destination
    squareSelect = ()

    # keep track of which square player clicks
    playerClicks = []
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            #listen for mouse event    
            elif e.type == p.MOUSEBUTTONDOWN:
                #keep track of mouse position while moving
                # use predefined func get_pos() to get location of mouse click
                location = p.mouse.get_pos()

                mouseCol = location[0] //SQ_SIZE
                mouseRow = location[1] //SQ_SIZE

                '''Invalid moves when source click and desitination click is same
                empty the count moves
                '''
                #make sure that source and destination squares are not the same so user doesnt select the same square
                if squareSelect == (mouseRow,mouseCol):
                    squareSelect = () #deselect
                    playerClicks = [] #clear player click
                else:
                    squareSelect = (mouseRow,mouseCol)

                    #append first and second click
                    playerClicks.append(squareSelect)
                
                #after second click like after choosing destination square
                if len(playerClicks) == 2:
                    move = chessEngine.Move(playerClicks[0],playerClicks[1],gmState.board)

                    #print from source box clicked to destination box
                    print(move.getChessNotation())

                    if move in validMoves:
                        #move the piece
                        gmState.makeMove(move)
                        moveMade = True

                    #set the list back to empty once done
                    squareSelect=() # reset user clicks to 0 so that count works
                    playerClicks = []


            elif e.type == p.KEYDOWN:
                #handles the undo Move when z
                if e.key == p.K_z:
                    print("undo key ( 'Z' ) pressed")
                    gmState.undoMove()
                    moveMade = True
        

    #when move made
        if moveMade:
            '''once move is made we need to generate new set of vlaid moves 
            
            Then set the moveMade back to false to make another move using that piece
            '''
            validMoves = gmState.getValidMoves()
            moveMade = False





        #keep dispaying screen
        drawGameState(screen,gmState)
        #rate of refresh    
        clock.tick(MAX_FPS)
        p.display.flip()


'''
Function deals with graphics
'''
def drawGameState(screen,gmState):
    # function draws all the squares
    drawSquare(screen)
    # draws the chess pieces
    drawPieces(screen,gmState.board)


#function that draws all the squares on the screen
def drawSquare(screen):
    colors = [p.Color("white"),p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            ''' when we add row and column index if we get even number we in white box and if odd the we are in black box
            so if remainder is 0 the white
            if remainder is 1 the black box
            '''
            color = colors[((row+column)%2)]
            '''
            draw.rect (surface,color,dimension)
            '''
            p.draw.rect(screen,color,p.Rect(column*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE))

'''looping through all the piece list and displaying them within the screen'''
def drawPieces(screen,board):
    for row in range(DIMENSION):
        for column  in range(DIMENSION):
            piece = board[row][column]

            '''
            If the box doesnt contain this empty string then place the piece according to the nested list in chessEngine
            '''
            if piece != '--':

                '''
                screen.blit -> overlap the pieces image over the chess board squares withing the required squares
                '''
                screen.blit(IMAGES[piece],p.Rect(column*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE))


if __name__ == "__main__":
    main()





