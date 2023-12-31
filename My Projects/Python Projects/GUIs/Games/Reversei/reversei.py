# Reversi

import random
import sys

def drawBoard(board):

    # This function prints out the board that it was passed. Returns None.

    HLINE = '  +---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)

    for y in range(8):

        print(VLINE)
        print(y+1, end=' ')

        for x in range(8):
            print('| %s' % (board[x][y]), end=' ')

        print('|')
        print(VLINE)
        print(HLINE)


def resetBoard(board):
    # Blanks out the board it is passed, except for the original starting position.
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

 29.     # Starting pieces:

 30.     board[3][3] = 'X'

 31.     board[3][4] = 'O'

 32.     board[4][3] = 'O'

 33.     board[4][4] = 'X'

 34.

 35.

 36. def getNewBoard():

 37.     # Creates a brand new, blank board data structure.

 38.     board = []

 39.     for i in range(8):

 40.         board.append([' '] * 8)

 41.

 42.     return board

 43.

 44.

 45. def isValidMove(board, tile, xstart, ystart):

 46.     # Returns False if the player's move on space xstart, ystart is invalid.

 47.     # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.

 48.     if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):

 49.         return False

 50.

 51.     board[xstart][ystart] = tile # temporarily set the tile on the board.

 52.

 53.     if tile == 'X':

 54.         otherTile = 'O'

 55.     else:

 56.         otherTile = 'X'

 57.

 58.     tilesToFlip = []

 59.     for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:

 60.         x, y = xstart, ystart

 61.         x += xdirection # first step in the direction

 62.         y += ydirection # first step in the direction

 63.         if isOnBoard(x, y) and board[x][y] == otherTile:

 64.             # There is a piece belonging to the other player next to our piece.

 65.             x += xdirection

 66.             y += ydirection

 67.             if not isOnBoard(x, y):

 68.                 continue

 69.             while board[x][y] == otherTile:

 70.                 x += xdirection

 71.                 y += ydirection

 72.                 if not isOnBoard(x, y): # break out of while loop, then continue in for loop

 73.                     break

 74.             if not isOnBoard(x, y):

 75.                 continue

 76.             if board[x][y] == tile:

 77.                 # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.

 78.                 while True:

 79.                     x -= xdirection

 80.                     y -= ydirection

 81.                     if x == xstart and y == ystart:

 82.                         break

 83.                     tilesToFlip.append([x, y])

 84.

 85.     board[xstart][ystart] = ' ' # restore the empty space

 86.     if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.

 87.         return False

 88.     return tilesToFlip

 89.

 90.

 91. def isOnBoard(x, y):

 92.     # Returns True if the coordinates are located on the board.

 93.     return x >= 0 and x <= 7 and y >= 0 and y <=7

 94.

 95.

 96. def getBoardWithValidMoves(board, tile):

 97.     # Returns a new board with . marking the valid moves the given player can make.

 98.     dupeBoard = getBoardCopy(board)

 99.

100.     for x, y in getValidMoves(dupeBoard, tile):

101.         dupeBoard[x][y] = '.'

102.     return dupeBoard

103.

104.

105. def getValidMoves(board, tile):

106.     # Returns a list of [x,y] lists of valid moves for the given player on the given board.

107.     validMoves = []

108.

109.     for x in range(8):

110.         for y in range(8):

111.             if isValidMove(board, tile, x, y) != False:

112.                 validMoves.append([x, y])

113.     return validMoves

114.

115.

116. def getScoreOfBoard(board):

117.     # Determine the score by counting the tiles. Returns a dictionary with keys 'X' and 'O'.

118.     xscore = 0

119.     oscore = 0

120.     for x in range(8):

121.         for y in range(8):

122.             if board[x][y] == 'X':

123.                 xscore += 1

124.             if board[x][y] == 'O':

125.                 oscore += 1

126.     return {'X':xscore, 'O':oscore}

127.

128.

129. def enterPlayerTile():

130.     # Lets the player type which tile they want to be.

131.     # Returns a list with the player's tile as the first item, and the computer's tile as the second.

132.     tile = ''

133.     while not (tile == 'X' or tile == 'O'):

134.         print('Do you want to be X or O?')

135.         tile = input().upper()

136.

137.     # the first element in the list is the player's tile, the second is the computer's tile.

138.     if tile == 'X':

139.         return ['X', 'O']

140.     else:

141.         return ['O', 'X']

142.

143.

144. def whoGoesFirst():

145.     # Randomly choose the player who goes first.

146.     if random.randint(0, 1) == 0:

147.         return 'computer'

148.     else:

149.         return 'player'

150.

151.

152. def playAgain():

153.     # This function returns True if the player wants to play again, otherwise it returns False.

154.     print('Do you want to play again? (yes or no)')

155.     return input().lower().startswith('y')

156.

157.

158. def makeMove(board, tile, xstart, ystart):

159.     # Place the tile on the board at xstart, ystart, and flip any of the opponent's pieces.

160.     # Returns False if this is an invalid move, True if it is valid.

161.     tilesToFlip = isValidMove(board, tile, xstart, ystart)

162.

163.     if tilesToFlip == False:

164.         return False

165.

166.     board[xstart][ystart] = tile

167.     for x, y in tilesToFlip:

168.         board[x][y] = tile

169.     return True

170.

171.

172. def getBoardCopy(board):

173.     # Make a duplicate of the board list and return the duplicate.

174.     dupeBoard = getNewBoard()

175.

176.     for x in range(8):

177.         for y in range(8):

178.             dupeBoard[x][y] = board[x][y]

179.

180.     return dupeBoard

181.

182.

183. def isOnCorner(x, y):

184.     # Returns True if the position is in one of the four corners.

185.     return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

186.

187.

188. def getPlayerMove(board, playerTile):

189.     # Let the player type in their move.

190.     # Returns the move as [x, y] (or returns the strings 'hints' or 'quit')

191.     DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()

192.     while True:

193.         print('Enter your move, or type quit to end the game, or hints to turn off/on hints.')

194.         move = input().lower()

195.         if move == 'quit':

196.             return 'quit'

197.         if move == 'hints':

198.             return 'hints'

199.

200.         if len(move) == 2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:

201.             x = int(move[0]) - 1

202.             y = int(move[1]) - 1

203.             if isValidMove(board, playerTile, x, y) == False:

204.                 continue

205.             else:

206.                 break

207.         else:

208.             print('That is not a valid move. Type the x digit (1-8), then the y digit (1-8).')

209.             print('For example, 81 will be the top-right corner.')

210.

211.     return [x, y]

212.

213.

214. def getComputerMove(board, computerTile):

215.     # Given a board and the computer's tile, determine where to

216.     # move and return that move as a [x, y] list.

217.     possibleMoves = getValidMoves(board, computerTile)

218.

219.     # randomize the order of the possible moves

220.     random.shuffle(possibleMoves)

221.

222.     # always go for a corner if available.

223.     for x, y in possibleMoves:

224.         if isOnCorner(x, y):

225.             return [x, y]

226.

227.     # Go through all the possible moves and remember the best scoring move

228.     bestScore = -1

229.     for x, y in possibleMoves:

230.         dupeBoard = getBoardCopy(board)

231.         makeMove(dupeBoard, computerTile, x, y)

232.         score = getScoreOfBoard(dupeBoard)[computerTile]

233.         if score > bestScore:

234.             bestMove = [x, y]

235.             bestScore = score

236.     return bestMove

237.

238.

239. def showPoints(playerTile, computerTile):

240.     # Prints out the current score.

241.     scores = getScoreOfBoard(mainBoard)

242.     print('You have %s points. The computer has %s points.' % (scores[playerTile], scores[computerTile]))

243.

244.

245.

246. print('Welcome to Reversi!')

247.

248. while True:

249.     # Reset the board and game.

250.     mainBoard = getNewBoard()

251.     resetBoard(mainBoard)

252.     playerTile, computerTile = enterPlayerTile()

253.     showHints = False

254.     turn = whoGoesFirst()

255.     print('The ' + turn + ' will go first.')

256.

257.     while True:

258.         if turn == 'player':

259.             # Player's turn.

260.             if showHints:

261.                 validMovesBoard = getBoardWithValidMoves(mainBoard, playerTile)

262.                 drawBoard(validMovesBoard)

263.             else:

264.                 drawBoard(mainBoard)

265.             showPoints(playerTile, computerTile)

266.             move = getPlayerMove(mainBoard, playerTile)

267.             if move == 'quit':

268.                 print('Thanks for playing!')

269.                 sys.exit() # terminate the program

270.             elif move == 'hints':

271.                 showHints = not showHints

272.                 continue

273.             else:

274.                 makeMove(mainBoard, playerTile, move[0], move[1])

275.

276.             if getValidMoves(mainBoard, computerTile) == []:

277.                 break

278.             else:

279.                 turn = 'computer'

280.

281.         else:

282.             # Computer's turn.

283.             drawBoard(mainBoard)

284.             showPoints(playerTile, computerTile)

285.             input('Press Enter to see the computer\'s move.')

286.             x, y = getComputerMove(mainBoard, computerTile)

287.             makeMove(mainBoard, computerTile, x, y)

288.

289.             if getValidMoves(mainBoard, playerTile) == []:

290.                 break

291.             else:

292.                 turn = 'player'

293.

294.     # Display the final score.

295.     drawBoard(mainBoard)

296.     scores = getScoreOfBoard(mainBoard)

297.     print('X scored %s points. O scored %s points.' % (scores['X'], scores['O']))

298.     if scores[playerTile] > scores[computerTile]:

299.         print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))

300.     elif scores[playerTile] < scores[computerTile]:

301.         print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))

302.     else:

303.         print('The game was a tie!')

304.

305. if not playAgain():
306.    