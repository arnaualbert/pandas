# Read scimago ranking
import pandas as pd
entries: pd.DataFrame = pd.read_csv("scimagojr 2021 Subject Area - Medicine.csv", sep=";")
print(entries) # lo printea todo
print(entries.loc[:,"Rank"]) # solo printea los rank
print(entries.loc[:,"Rank"].dtype) # printa el tipus del Rank
print(entries.dtypes) # printa tots els tipus
print(entries.index)#Mostra els index de cada fila
entries_high = entries.loc[:,"H index"] >= 450
entries_ok = entries.loc[entries_high,:]
print(entries_ok)
#ensenyar les 5 primeres
#Ordenació per valors axis=0 columnes 
entries_top = entries_ok.sort_values(by=['H index'], 
                                    axis=0, 
                                    ascending=False)
print(entries_top.head(5))