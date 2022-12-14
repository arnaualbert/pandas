import numpy as np
import pandas as pd

# Demo series.
# np.nan es equivalente a not avaliable, más eficiente.
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# Serie amb index predeterminat (0,1,2,...)
list_temp = [12.5,17.3,20.5,np.nan]
serie_temp = pd.Series(data=list_temp, dtype=float )
print(serie_temp)

# Serie amb index personalitzat.
index_temp = ['jan','feb','mar','apr']
serie_temp_mensuals = pd.Series(data=list_temp, dtype=float, index=index_temp)
print(serie_temp_mensuals)

# Serie, valors String
#index_series = ['jan','feb','mar','apr']
list_bestseries = ['Casa Papel', 'Casa Dragon', 'Merli', 'Plats Bruts']
serie_bestseries = pd.Series(data=list_bestseries, dtype="string")
print(serie_bestseries)

#serie noms animals
list_animales = ['Gat', 'Gos', 'Tortuga', 'Serpiente']
legs_list = [4,4,4,0]
serie_animales= pd.Series(data=legs_list, dtype=float, index=list_animales)
print(serie_animales)

# Test dataframes
# Com en el cas de les series,.
dict_animals = {'num_legs': [2, 4, 0, 8, 6], 'num_wings': [2, 0, 0, 0, 4], 'can_fly': [True, False, False, False, True]}
name_animals = ['falcon', 'dog', 'snail', 'spider', 'butterfly']
df_animals = pd.DataFrame(data=dict_animals, index=name_animals)
print(df_animals)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)




animals_df = pd.Series(data=['falcon', 'dog', 'snail', 'spider'], dtype="string")
df3 = pd.DataFrame(
    {
        "A": [1.0] + [np.nan] * 2 + [3.0],
        "B": pd.date_range("20220101", periods=4, freq='D'),
        "C": animals_df,
        "D": pd.Categorical(["Male", "Female", "NS/NC", "Female"]),
        "E": "foo",
    }
)
print(df3)