import asyncio
import httpx
import datetime


async def main():
    # start = datetime.datetime.now()
    
    pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'

    async with httpx.AsyncClient() as client:

        resp = await client.get(pokemon_url)

        pokemon = resp.json()
        # print(pokemon['name'])
        
        # end = datetime.datetime.now()
    
        # delta = end - start
        return pokemon['name']


# array
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


start = datetime.datetime.now()


for i in a:
    # asyncio.run(main())
    print(datetime.datetime.now(), "Response:", asyncio.run(main()))

# asyncio.run(main())

end = datetime.datetime.now()
delta = end - start

print("Total Time:", delta)