n=int(input("\nEnter the number of pokemons in the game:"))
list=[]
for i in range(n):
    pokemon_power=int(input("\nWrite the power of pokemon"))
    list.append(pokemon_power)
    print('\nminimum power of pokemons till now is:',min(list))
    print('\nmaximum power of pokemons till now is:',max(list))

