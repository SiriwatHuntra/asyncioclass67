import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')
    i = 0
    # Iterate through all json files in the directory.
    for path in pathlist:
        async with aiofiles.open(f'{path}', mode='r') as f:
            content = await f.read()

        pokemon = json.loads(content)
        name = pokemon['name']
        moves = [move['move']['name'] for move in pokemon['moves']]
        
        async with aiofiles.open(f'{pokemonmove_directory}/{name}_move.txt', mode='w') as f:
            await f.write('\n'.join(moves))

        #print(path)


asyncio.run(main())
