import time

judit_compute = 0.1
opponent_compute = 0.5
opponent = 1
move_board = 30

def main(i):
    for j in range(move_board):
        time.sleep(judit_compute)
        print(f"Judit done {j} moving in board {i}")
        time.sleep(opponent_compute)
        print(f"Opponent done {j} moving in board {i}")
        j += 1
        

if __name__=="__main__":
    start_game = time.perf_counter()
    for i in range(opponent):
        main(i)
        i += 1
    elapsed = time.perf_counter() - start_game
    print(f'{time.ctime()} - All board done in ', elapsed, "seconds." )


