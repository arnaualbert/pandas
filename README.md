Pandas Notes

### Iniciar Pandas

```python
import pandas 
```

### DataFrame

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

### Series

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