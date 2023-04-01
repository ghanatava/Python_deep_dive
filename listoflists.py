board=[['_']*3 for i in range(3)]
print(board)
board[1][2]='X'
print(board)

#A tempting but wrong shortcut, list with 3 reference to same list is useless
weird_board=[['_']*3]*3
weird_board[1][0]='0'
print(weird_board) #output [['0','_','_'],['0','_','_'],['0','_','_']]
