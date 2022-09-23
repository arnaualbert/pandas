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

