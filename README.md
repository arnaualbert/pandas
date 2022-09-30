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