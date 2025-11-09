
from typing import Tuple, List, Optional
from copy import deepcopy
from search_algorithms import minimax_search, alphabeta_search

State = Tuple[int, List[List[Optional[int]]]]  # (player_to_move, 3x3 board)
Action = Tuple[int, int]                       # (row, col)

class Game:
    def initial_state(self) -> State:
        return (0, [[None, None, None], [None, None, None], [None, None, None]])

    def to_move(self, state: State) -> int:
        player, _ = state
        return player

    def actions(self, state: State) -> List[Action]:
        _, board = state
        acts: List[Action] = []
        for r in range(3):
            for c in range(3):
                if board[r][c] is None:
                    acts.append((r, c))
        return acts

    def result(self, state: State, action: Action) -> State:
        _, board = state
        r, c = action
        next_board = deepcopy(board)
        next_board[r][c] = self.to_move(state)
        return ((self.to_move(state) + 1) % 2, next_board)

    def is_winner(self, state: State, player: int) -> bool:
        _, board = state
        # rows
        for r in range(3):
            if all(board[r][c] == player for c in range(3)):
                return True
        # cols
        for c in range(3):
            if all(board[r][c] == player for r in range(3)):
                return True
        # diags
        if all(board[i][i] == player for i in range(3)):
            return True
        if all(board[i][2-i] == player for i in range(3)):
            return True
        return False

    def is_terminal(self, state: State) -> bool:
        _, board = state
        if self.is_winner(state, (self.to_move(state) + 1) % 2):
            return True
        return all(board[r][c] is not None for r in range(3) for c in range(3))

    def utility(self, state: State, player: int) -> float:
        assert self.is_terminal(state)
        if self.is_winner(state, player):
            return 1
        if self.is_winner(state, (player + 1) % 2):
            return -1
        return 0

    def print(self, state: State):
        _, board = state
        print()
        for r in range(3):
            row = [
                ' ' if board[r][c] is None else 'x' if board[r][c] == 0 else 'o'
                for c in range(3)
            ]
            print(f" {row[0]} | {row[1]} | {row[2]}")
            if r < 2:
                print("---+---+---")
        print()
        if self.is_terminal(state):
            if self.utility(state, 0) > 0:
                print("P1 won")
            elif self.utility(state, 1) > 0:
                print("P2 won")
            else:
                print("The game is a draw")
        else:
            print(f"It is P{self.to_move(state)+1}'s turn to move")


def play_ttt_with(search_fn, label: str):
    game = Game()
    state = game.initial_state()
    print(f"=== Tic-tac-toe ({label}) ===")
    game.print(state)
    while not game.is_terminal(state):
        player = game.to_move(state)
        action = search_fn(game, state)
        print(f"P{player+1}'s action: {action}")
        state = game.result(state, action)
        game.print(state)


def time_first_move():
    import time

    # Minimax on the initial empty board
    g1 = Game(); s1 = g1.initial_state()
    t0 = time.perf_counter()
    _ = minimax_search(g1, s1)
    t1 = time.perf_counter()

    # Alpha–Beta on the (fresh) initial empty board
    g2 = Game(); s2 = g2.initial_state()
    t2 = time.perf_counter()
    _ = alphabeta_search(g2, s2)
    t3 = time.perf_counter()

    return (t1 - t0), (t3 - t2)
