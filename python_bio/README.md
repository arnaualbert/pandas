# Pandas Notes

## Iniciar Pandas

```python
import pandas 
```

## Series

Una serie es un array que puede tener todo tipos de datos

Para printar un valor especifico de la serie se hace con su index por ejemplo para printar el numero 7 de las serie seria : print(myvar[1])

```python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# print:
# 0    1
# 1    7
# 2    2
# dtype: int64

# print del primer valor de la serie

print(myvar[0])

# print:
#1
```

### Labels de series

Para crear el propio Label (index) se hace con la funcion index y con una lista(array)

```python
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

#print :
# x    1
# y    7
# z    2
# dtype: int64

# si ahora queremos llamar al 7 lo haremos de la siguiente manera

print(myvar["y"])

#print:
#7
```

### Key/Values Objects as Series

Tambien se pueden crear series a partir de un diccionario

Las claves de los diccionarios se vuelven los indices

```python
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

# print:
# day1    420
# day2    380
# day3    390
# dtype: int64

```

Se puede llamar a los indices que tu quieras poniendo la llave del diccionario

```python
import pandas as pd

calories = {"day1": 400, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = [ "day2", "day3"])

print(myvar)

# print
# day2    380
# day3    390
# dtype: object
```

## DataFrame

Un DataFrame es una tabla

Las series vienen a ser una columna en cambio un dataframe es la tabla entera

```python
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)

# print :
#     cars  passings
# 0    BMW         3
# 1  Volvo         7
# 2   Ford         2


```

Asi se crea un dataframe

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

#print 
#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45
```

Para acceder una fila de un dataframe lo que seria una serie se hace con el loc

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)

#print 
#    calories  duration
# 0       420        50
# 1       380        40
# 2       390        45

# para acceder asolo la line 0 de el dataframe seria asi:

print(df.loc[0])
#   print
#   calories    420
#   duration     50
#   Name: 0, dtype: int64

# tambien se pueden acceder a mas de una
print(df.loc[0,1])
# print

#      calories  duration
#   0       420        50
#   1       380        40
```
Se pueden poner nombres a los indices

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
# print
#         calories  duration
#   day1       420        50
#   day2       380        40
#   day3       390        45
```
Con nombres en los indices tambien se puede usar el loc

```python
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
# print
#         calories  duration
#   day1       420        50
#   day2       380        40
#   day3       390        45

#refer to the named index:
print(df.loc["day2"])

# print 
#   calories    380
#   duration     40
#   Name: 0, dtype: int64
```
Se puede cargar un archivo en un dataframe

```python
import pandas as pd

df = pd.read_csv('data.csv')

print(df) 

# print
#        Duration  Pulse  Maxpulse  Calories
#   0          60    110       130     409.1
#   1          60    117       145     479.0
#   2          60    103       135     340.0
#   3          45    109       175     282.4
#   4          45    117       148     406.0
#   ..        ...    ...       ...       ...
#   164        60    105       140     290.8
#   165        60    110       145     300.4
#   166        60    115       145     310.2
#   167        75    120       150     320.4
#   168        75    125       150     330.4
  
#   [169 rows x 4 columns]

```

### Funciones en un dataframe

Hay diferentes funciones que se puedan aplicar sobre un dataframe como las siguientes

