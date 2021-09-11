'''
Stores all info about current state of chess game
Determine valid moves in chess games
'''

class gameState():
    def __init__(self):
        '''
        first character is the color and second character is name
        -- is empty space
        '''
        self.board = [
            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
            ['bp','bp','bp','bp','bp','bp','bp','bp'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['wp','wp','wp','wp','wp','wp','wp','wp'],
            ['wR','wN','wB','wQ','wK','wB','wN','wR']
        ]

        '''Each piece is being mapped to given function and we can call the function when piece has to move'''
        self.moveFunctions = {'p':self.getPawnMoves,'R':self.getRookMoves,
        'K':self.getKingMoves,'N':self.getKnightMoves,'Q':self.getQueenMoves,'B':self.getBishopMoves}
        #keep track of moves
        self.whiteToMove = True
        self.moveLog =[]


    '''function that moves piece from one box to another'''
    def makeMove(self,move):

        #when we move make the starting row and column to empty when piece moved
        self.board[move.startRow][move.startCol] = '--'


        #move the piece to the destination row and column
        self.board[move.endRow][move.endCol] = move.pieceMoved    

        #log move
        self.moveLog.append(move)

        #switch moves between players
        self.whiteToMove = not self.whiteToMove


    ''' undo last move'''
    def undoMove(self):

        '''we can undo a move only if there are moves so should not be 0'''
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved

            self.board[move.endRow][move.endCol] = move.pieceCaptured

            #change turns
            self.whiteToMove = not self.whiteToMove


    '''All moves considering checkmate to the king'''
    def getValidMoves(self):
        return self.getAllPossibleMoves()


    '''All moves without considering checkmate to king'''

    def getAllPossibleMoves(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                turn = self.board[row][col][0]

                if (turn =='w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[row][col][1]

                    #all the moves for the respective pieces
                    self.moveFunctions[piece](row,col,moves)
        return moves



    def getPawnMoves(self,row,col,moves):
        #white pawn move
        if self.whiteToMove:
            if self.board[row-1][col] == '--':
                moves.append(Move((row,col),(row-1,col),(self.board)))

                if row == 6 and self.board[row-2][col] == '--':
                    moves.append(Move((row,col),(row-2,col),(self.board)))
            
            #stay with the given columns dont go outside screen limit

            #move to left
            if col - 1 >= 0:
                if self.board[row-1][col-1][0] == 'b':
                    #from starting square to ending square
                    moves.append(Move((row,col),(row-1,col-1),(self.board)))

            #move to right when killing enemy
            if col + 1 <= 7:
                if self.board[row-1][col+1][0] == 'b':

                    #from starting square to ending square
                    moves.append(Move((row,col),(row-1,col+1),(self.board)))


        #black pawn move
        else:
            if self.board[row+1][col] == '--':
                moves.append(Move((row,col),(row+1,col),(self.board)))

                if row == 1 and self.board[row+2][col] == '--':
                    moves.append(Move((row,col),(row+2,col),(self.board)))
            
            #stay with the given columns dont go outside screen limit

            #move to left
            if col - 1 >= 0:
                if self.board[row+1][col-1][0] == 'w':
                    #from starting square to ending square
                    moves.append(Move((row,col),(row+1,col-1),(self.board)))

            #move to right when killing enemy
            if col + 1 <= 7:
                if self.board[row+1][col+1][0] == 'w':

                    #from starting square to ending square
                    moves.append(Move((row,col),(row+1,col+1),(self.board)))

                    







    def getRookMoves(self,row,col,moves):
        pass

    def getKnightMoves(self,row,col,moves):
        pass

    def getBishopMoves(self,row,col,moves):
        pass

    def getKingMoves(self,row,col,moves):
        pass

    def getQueenMoves(self,row,col,moves):
        pass


'''
Deals with moving the pieces on click
'''
class Move():

    # row numbering in chess board

    rankRows = {'1':7,'2':6,
    '3':5,'4':4,'5':3,'6':2,
    '7':1,'8':0}

    #reversing key and values 
    rowToRank = {v:k for k,v in rankRows.items()}

     # column numbering in chess board

    filesToCols = {'a':0,'b':1,
    'c':2,'d':3,'e':4,'f':5,
    'g':6,'h':7}
    #reversing key and value pairs
    colsToRank = {v:k for k,v in filesToCols.items()}




    def __init__(self,startSq,endSq,board):

        #start location row and column
        self.startRow = startSq[0]
        self.startCol = startSq[1]

        #destination location row and column
        self.endRow = endSq[0]
        self.endCol = endSq[1]

        # what piece is selected
        self.pieceMoved = board[self.startRow][self.startCol]

        #where it moves to destination
        self.pieceCaptured = board[self.endRow][self.endCol]  

        #unique id for each move
        self.moveID = self.startRow * 1000 + self.startCol*100 + self.endRow*10 + self.endCol 

    
    '''function to overide the equal to function'''
    def __eq__(self, other):
        if isinstance(other,Move):
            return self.moveID == other.moveID
        return False






    '''display the source and destination location'''
    def getChessNotation(self):

        return ("-> Moved " + self.getRankFile(self.startRow,self.startCol) + " to "+ self.getRankFile(self.endRow,self.endCol)) 


    def getRankFile(self,row,col):

        '''In chess columns are files and rows are ranks'''
        # column->file
        # row ->rank
        return self.colsToRank[col] + self.rowToRank[row]
         










