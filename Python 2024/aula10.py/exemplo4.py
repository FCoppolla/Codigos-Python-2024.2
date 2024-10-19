#criando uma lista simples com 3 pokemons
pokemons = ["Pikachu", "charmander" ,"bulbasaur" ]

#exibindo lista
print("lista de pokemons:", pokemons)

#acessando o primeiro pokemon da lista
print("primeiro pokemon", pokemons[0])

#adicionando um novo pokemon a lista
pokemons.append("squirtle")
print("lista de pokemons após adicionar o squirtle:" , pokemons)

# removendo o pokemon "charmander" da lista
pokemons.remove("charmander")
print("lista de pokemons ápos remover o charmander:",  pokemons )

#exibindo o tamanho da lista
print("numero de pokemons da lista:" , len (pokemons))

