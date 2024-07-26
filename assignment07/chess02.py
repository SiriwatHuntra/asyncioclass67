import time
import asyncio 

judit_compute = 0.1
opponent_compute = 0.5
opponent = 24
move_board = 30

async def main(i):
    start_board = time.perf_counter()

    for j in range(move_board):
        time.sleep(judit_compute)
        print(f"Board {i}-{j} Judit make move.")
        await asyncio.sleep(opponent_compute)
        print(f"Board {i}-{j} Opponent make move.")

    time_complete = time.perf_counter() - start_board
    print(f'{time.ctime()} - Board {i} finish in ', time_complete, "seconds." )

async def async_io():
    start_game = time.perf_counter()

    task = []
    for i in range(opponent):
        task += [main(i)]
    await asyncio.gather(*task)    

    elapsed = time.perf_counter() - start_game
    print(f'{time.ctime()} - All board done in ', elapsed, "seconds." )

if __name__=="__main__":
    asyncio.run(async_io())




