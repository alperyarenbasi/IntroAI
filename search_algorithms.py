from math import inf

def minimax_search(game, state):
    player = game.to_move(state)

    def max_value(s):
        if game.is_terminal(s):
            return game.utility(s, player), None
        v, move = -inf, None
        for a in game.actions(s):
            v2, _ = min_value(game.result(s, a))
            if v2 > v:
                v, move = v2, a
        return v, move

    def min_value(s):
        if game.is_terminal(s):
            return game.utility(s, player), None
        v, move = inf, None
        for a in game.actions(s):
            v2, _ = max_value(game.result(s, a))
            if v2 < v:
                v, move = v2, a
        return v, move

    _, move = max_value(state)
    return move


def alphabeta_search(game, state):
    player = game.to_move(state)

    def max_value(s, alpha, beta):
        if game.is_terminal(s):
            return game.utility(s, player), None
        v, best = -inf, None
        for a in game.actions(s):
            v2, _ = min_value(game.result(s, a), alpha, beta)
            if v2 > v:
                v, best = v2, a
            if v >= beta:
                return v, best
            alpha = max(alpha, v)
        return v, best

    def min_value(s, alpha, beta):
        if game.is_terminal(s):
            return game.utility(s, player), None
        v, best = inf, None
        for a in game.actions(s):
            v2, _ = max_value(game.result(s, a), alpha, beta)
            if v2 < v:
                v, best = v2, a
            if v <= alpha:
                return v, best
            beta = min(beta, v)
        return v, best

    _, move = max_value(state, -inf, inf)
    return move
