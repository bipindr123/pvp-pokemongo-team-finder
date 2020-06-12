f = open("res.txt","r")
pokemons = {}

while True:
    line = f.readline()
    if not line:
        break
    line2 = f.readline()
    line2 = int(line2[:-1])
    pokemons[line2] = line

x = list(pokemons)
x.sort()

for i in range(10):
    print(x[i])
    print(pokemons.get(x[i]))
    