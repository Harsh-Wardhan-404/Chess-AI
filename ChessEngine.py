class GameState():
    def __init__(self):

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.whiteToMove = True
        self.moveLog = []


    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append((move))
        self.whiteToMove = not self.whiteToMove # swap players


        #Undo the last Moves:
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove

    '''All moves considering checks'''
    def getValidMoves(self):
        return self.getAllPossibleMoves()


    '''All moves without considering checks'''
    def getAllPossibleMoves(self):
        moves = []
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0] # access first character of a piece eg- bk:b wp:w...to know whose turn it is
                if (turn == 'w' and self.whiteToMove) and (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    if piece == 'p':
                        self.getPawnMoves(r, c, moves)
                    elif piece == 'r':
                        self.getRookMoves(r, c, moves)

        return moves

    def getPawnMoves(self, r, c, moves):
        pass


    def getRookMoves(self, r, c, moves):
        pass


class Move():

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()} # This basically swaps the key and value from above dictionary
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol*100 + self.endRow * 10 + self.endCol
        print(self.moveID)

    #Overrriding the equals method

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID


    def getChessNotation(self):
        return self.getRankFile(self.startRow, self.startCol) +"->" +self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]