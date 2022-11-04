import numpy as np
import pandas as pd
pokedex: pd.DataFrame = pd.read_csv("./pokedex.csv", sep=",")
print(pokedex)
pokemonNames: pd.Series = pokedex['Name']
print(pokemonNames)
print(pokedex.loc[:,['Name','HP']])
print(pokedex.loc[ [152,153] , : ] )