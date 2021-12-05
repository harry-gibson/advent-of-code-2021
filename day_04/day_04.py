import numpy as np

class BingoBoard:
    
    def __init__(self, board_array):
        self.board = board_array
        self.marks = np.zeros_like(board_array, dtype=np.bool_)
        self.last_play = None
        self.bingoed = False
        
    def play(self, number) -> bool:
        self.marks = self.marks | (self.board == number)
        self.last_play = number
        return self.is_bingo()
    
    def is_bingo(self) -> bool:
        if self.bingoed:
            return None
        is_bingo_now = np.any([self.marks.all(axis=0), self.marks.all(axis=1)])
        self.bingoed = self.bingoed or is_bingo_now
        return is_bingo_now
    
    def score(self) -> int:
        return self.board[~self.marks].sum() * self.last_play

with open('input.txt') as f:
    items = f.read().split('\n\n')

numbers = [int(i) for i in items[0].split(',')]
boards = [BingoBoard(np.fromstring(board_txt, sep=' ').reshape((5,5)))
         for board_txt in items[1:]]

for turn, number in enumerate(numbers):
    for board in boards:
        if board.play(number):
            print(f"Bingo! Part 1 answer: {board.score()}")
            done = True
            break
    else:
        continue
    break

boards = [BingoBoard(np.fromstring(board_txt, sep=' ').reshape((5,5)))
         for board_txt in items[1:]]
n_finished = 0
for turn, number in enumerate(numbers):
    for board in boards:
        if board.play(number):
            n_finished += 1
            if n_finished == len(boards):
                break
    else:
        continue
    print (f"Part 2 answer: {board.score()}")
    break