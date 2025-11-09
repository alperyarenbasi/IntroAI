
from halving_game import play_halving
from bucket_game import play_bucket
from tic_tac_toe import play_ttt_with, time_first_move
from search_algorithms import minimax_search, alphabeta_search

def main():
    print("=== Halving game (Minimax vs Minimax) ===")
    play_halving(N=5)  

    print("\n=== Bucket game (Minimax vs Minimax) ===")
    play_bucket()

    print("\n=== Tic-tac-toe (Minimax full play) ===")
    play_ttt_with(minimax_search, label="Minimax")

    print("\n=== Tic-tac-toe (Alpha-Beta full play) ===")
    play_ttt_with(alphabeta_search, label="Alpha-Beta")

    print("\n=== Tic-tac-toe first-move timing (seconds) ===")
    t_minimax, t_ab = time_first_move()
    print(f"Minimax first move:   {t_minimax:.6f} s")
    print(f"Alpha-Beta first move:{t_ab:.6f} s")

if __name__ == "__main__":
    main()
