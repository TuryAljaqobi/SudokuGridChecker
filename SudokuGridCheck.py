def row_correct(sudoku:list, row_no :int):
   #row_no is the row you want to check
    
    for row in sudoku:
      for item in row:
          if sudoku[row_no].count(item) > 1 and item !=0:
              return False
    return 1

def column_correct(sudoku:list, col_no :int):
   #rcol_no is the column you want to check
    new_list = []
    for row in range(len(sudoku)):
        new_list.append(sudoku[row][col_no])
    
    for i in range(len(new_list)):
         if new_list.count(i) > 1 and i != 0:
             return False
    return 1
    

def block_correct(sudoku: list, row_no:int,  col_no: int):
    
    #Grab the block in question
    new_list = ([sudoku[i][col_no:col_no+3] for i in range(row_no,row_no+3)])
    checker_list = [] #Making this list to collect our matrix in a single list to
                      #check the sudoku range (1-9)

    

    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            number = new_list[i][j]
            if number > 0 and number in checker_list:#if in the list, return false
                return False
            checker_list.append(new_list[i][j]) # If its not in the list, add it
    
    
    return True #If it goes through the entire matrix without returning false, return True


def sudoku_grid_correct(sudoku: list):
    
    #Checking all the rows and columns
    for i in range(len(sudoku)):
        result = row_correct(sudoku, i)
        result_two = column_correct(sudoku, i)
        if (result < 1 or result_two < 1):
            return False
    
    
    # if the above is True then check the matrices
    #Check the blocks (0,0 , 0,3 , 0,6 and so on)
    for i in range(0, 7, 3):
       if block_correct(sudoku, 0 , i) == False or block_correct(sudoku, 3, i) == False \
           or block_correct(sudoku, 6, i) == False:
           return False
    
    return True

   

   


if __name__ == "__main__":
    sudoku = [
  [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
  [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
  [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
  [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
  [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
  [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
  [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
  [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
  [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],]
    print(sudoku_grid_correct(sudoku))

