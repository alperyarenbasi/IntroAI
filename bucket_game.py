from typing import Tuple, List, Union
from search_algorithms import minimax_search

State = Tuple[int, List[Union[str, int]]]  # (player_to_move, available buckets/values)
Action = Union[str, int]                   # 'A'|'B'|'C' or a chosen number

class Game:
    def initial_state(self) -> State:
        return (0, ['A', 'B', 'C'])

    def to_move(self, state: State) -> int:
        player, _ = state
        return player

    def actions(self, state: State) -> List[Action]:
        _, actions = state
        return list(actions)

    def result(self, state: State, action: Action) -> State:
        if action == 'A':
            return ((self.to_move(state) + 1) % 2, [-50, 50])
        if action == 'B':
            return ((self.to_move(state) + 1) % 2, [3, 1])
        if action == 'C':
            return ((self.to_move(state) + 1) % 2, [-5, 15])
        assert isinstance(action, int)
        return ((self.to_move(state) + 1) % 2, [action])

    def is_terminal(self, state: State) -> bool:
        _, acts = state
        return len(acts) == 1  
    
    def utility(self, state: State, player: int) -> float:
        assert self.is_terminal(state)
        _, acts = state
        assert isinstance(acts[0], int)
        return acts[0] if player == self.to_move(state) else -acts[0]

    def print(self, state: State):
        print(f"The state is {state} and ", end="")
        if self.is_terminal(state):
            print(f"P1's utility is {self.utility(state, 0)}")
        else:
            print(f"it is P{self.to_move(state)+1}'s turn")


def play_bucket():
    game = Game()
    state = game.initial_state()
    game.print(state)
    while not game.is_terminal(state):
        player = game.to_move(state)
        action = minimax_search(game, state)
        print(f"P{player+1}'s action: {action}")
        state = game.result(state, action)
        game.print(state)
