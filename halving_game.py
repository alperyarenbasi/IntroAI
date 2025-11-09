from typing import Tuple, List, Optional
from search_algorithms import minimax_search

State = Tuple[int, int]      # (player_to_move, number)
Action = str                 # '--' or '/2'

class Game:
    def __init__(self, N: int):
        self.N = N

    def initial_state(self) -> State:
        return (0, self.N)

    def to_move(self, state: State) -> int:
        player, _ = state
        return player

    def actions(self, state: State) -> List[Action]:
        return ['--', '/2']

    def result(self, state: State, action: Action) -> State:
        _, number = state
        if action == '--':
            return ((self.to_move(state) + 1) % 2, number - 1)
        elif action == '/2':
            return ((self.to_move(state) + 1) % 2, number // 2)
        raise ValueError("Unknown action")

    def is_terminal(self, state: State) -> bool:
        _, number = state
        return number == 0

    def utility(self, state: State, player: int) -> float:
        assert self.is_terminal(state)
        return 1 if self.to_move(state) == player else -1

    def print(self, state: State):
        _, number = state
        if self.is_terminal(state):
            print(f"The number is {number} and ", end="")
            if self.utility(state, 0) > 0:
                print("P1 won")
            else:
                print("P2 won")
        else:
            print(f"The number is {number} and it is P{self.to_move(state)+1}'s turn")


def play_halving(N: int = 5):
    game = Game(N)
    state = game.initial_state()
    game.print(state)
    while not game.is_terminal(state):
        player = game.to_move(state)
        action: Optional[Action] = minimax_search(game, state)
        print(f"P{player+1}'s action: {action}")
        assert action is not None
        state = game.result(state, action)
        game.print(state)
