'''
Algorithm to solve the sudoku puzzle

1. Find empty slots
2. Fill it with a number from 1-9
3. Check if the number is in its correct place

4. IF 
- Digit is in a valid place repeat steps from 1-3
   ELSE
- Reset the square to previous state and go back to previous state

5. Backtracking - soon as solution cannot be completed.

'''


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

'''
Valid position for a number on the sudoku board
'''

def valid_pos(my_board,number,position):

    #check row for duplicate number
    for row in range(len(my_board[0])):

        '''
        Check each column and see if that number is equal to anyother number on the column 
        '''
        if my_board[position[0]][row] == number and position[1] != row:
            return False
    
    #check column for duplicate number

    for row in range(len(my_board)):
        #loop through every row and not the exact position we inserted it
        if my_board[row][position[1]] == number and position[0] != row:
            return False


    #determine which box we are in currently

    '''
    (0,1)|(0,2)|(0,3)
         |     |
    ------------------     
    (1,1)|(1,2)|(1,3)
         |     |
    ------------------     
    (2,1)|(2,2)|(2,3)
         |     |

    we are considering the major big threboxes of three rows and three columns

    '''
    #so here after dividing we will get either
    #0,1,2
    box_x = position[1] // 3
    box_y = position[0] // 3


    #loop through those individula 9 big major boxes of 3x3 

    '''
    The for loop goes through any of the index elements in that 3x3 box.
    '''
    for row in range(box_y*3,box_y*3+3):
        for col in range(box_x*3,box_x*3+3):

            #here we are checking for a duplicate in that 3x3 matrix box
            if my_board[row][col]== number and (row,col) != position:
                return False

    '''
    Else if it passes all these checks then return that there is no duplicate element in that box
    '''
    return True

    


def print_board(my_board):
    for row in range(len(my_board)):

        #print this line after every three rows
        if row%3==0 and row !=0:
            print("\t- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
        
        #print this line after every 3 columns
        for col in range(len(my_board[0])):
            if col%3==0 and col != 0:
                #end="" doesnt print \n 
                print(" |",end="")
            
            if col == 8:
                print("\t"+str(my_board[row][col]))
            else:
                print("\t"+str(my_board[row][col])+ " ",end="")

'''
Function to find empty slots in the sudoku board

'''

def find_empty(my_board):
    #loop through the whole board 
    for row in range(len(my_board)):
        for col in range(len(my_board[0])):

            #empty slot is set to 0
            #so if we see any "0" that means its empty
            if my_board[row][col] == 0:
                return (row,col)

    return None


'''
Main backtracking algorithm
'''
def solve(my_board):


    print("\n")
    print_board(my_board)
    print("\n")


    '''search for empty space on the board'''
    find = find_empty(my_board) 

    #if no empty space found 
    if not find:
        print("No new empty slots found...")
        return True

    #if empty space found return row and column    
    else:
        row , col = find


    '''
    Check if any of the numbers from 1-9 are the valid solutions for that spot on the board
    '''
    for i in range(1,10):


        '''
        If the number is in its valid position then we add it there
        '''
        if valid_pos(my_board,i,(row,col)):
            print("\t\t\t\tNumber added row-wise...")
            my_board[row][col] = i


            '''
            Then we'll recursively call solve to keep finding a numbers valid position
            '''
            if solve(my_board):
                return True

            #if we cant solve it with the value then reset the board by placing that place with 0 which means its empty
            else:
                my_board[row][col] = 0
    
    #if we loop through all the numbers and none of the positions are valid we return False
    return False


print("\n\t\t\t\tSUDOKU SOLVER\n")
print("\nInitial board: '0' means empty\n")
print_board(board)
solve(board)
print("\nFinal solved board: \n")
print_board(board)




