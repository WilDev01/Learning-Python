# Declarar variables en python es tan sensillo como hacer lo siguiente
numero = 0 

# Tipos de datos

# En python no es precisamente necesario definir el tipo de datos de las variables
# Por lo que el las toma por default ejemplo si declaro un texto por defecto tomara como tipo str

texto = "hola mundo"
print(type(texto))

#Tipos de datos son los siguientes

# Tipos de datos en Python

# Tipos de datos de texto

# Str
datos = "Hola"
print(type(datos))  # str
# Descripción: `str` es un tipo de dato que representa cadenas de texto.
# Description: `str` is a data type that represents strings of text.

# Tipos de datos numéricos

# int
n = 0
print(type(n))  # int
# Descripción: `int` es un tipo de dato numérico entero.
# Description: `int` is a data type for whole numbers.

# float
f = 2.20
print(type(f))  # float
# Descripción: `float` es un tipo de dato que representa números decimales.
# Description: `float` is a data type for decimal numbers.

# complex
x = 1j
print(type(x))  # complex
# Descripción: `complex` es un tipo de dato que representa números complejos.
# Description: `complex` is a data type for complex numbers.

# Tipos de datos de colección

# list
l = ["apple", "banana", "cherry"]
print(type(l))  # list
# Descripción: `list` es una colección ordenada y mutable de elementos.
# Description: `list` is an ordered and mutable collection of items.

# tuple
t = ("apple", "banana", "cherry")
print(type(t))  # tuple
# Descripción: `tuple` es una colección ordenada e inmutable de elementos.
# Description: `tuple` is an ordered and immutable collection of items.

# range
r = range(6)
print(type(r))  # range
# Descripción: `range` genera una secuencia de números.
# Description: `range` generates a sequence of numbers.

# dict
d = {"name": "John", "age": 36}
print(type(d))  # dict
# Descripción: `dict` es un tipo de dato que almacena pares de clave-valor.
# Description: `dict` is a data type that stores key-value pairs.

# set
s = {"apple", "banana", "cherry"}
print(type(s))  # set
# Descripción: `set` es una colección no ordenada de elementos únicos.
# Description: `set` is an unordered collection of unique items.

# frozenset
fr = frozenset({"apple", "banana", "cherry"})
print(type(fr))  # frozenset
# Descripción: `frozenset` es un tipo de conjunto inmutable.
# Description: `frozenset` is an immutable version of a set.

# Tipos de datos booleanos

# bool
b = True
print(type(b))  # bool
# Descripción: `bool` representa valores de verdad: `True` o `False`.
# Description: `bool` represents truth values: `True` or `False`.

# Tipos de datos binarios

# bytes
by = b"Hello"
print(type(by))  # bytes
# Descripción: `bytes` es una secuencia inmutable de bytes.
# Description: `bytes` is an immutable sequence of bytes.

# bytearray
by_a = bytearray(5)
print(type(by_a))  # bytearray
# Descripción: `bytearray` es una secuencia mutable de bytes.
# Description: `bytearray` is a mutable sequence of bytes.

# memoryview
me = memoryview(bytes(5))
print(type(me))  # memoryview
# Descripción: `memoryview` permite acceder a los datos de un objeto de bytes sin copiar.
# Description: `memoryview` allows access to the data of a bytes object without copying it.

# NoneType

# None
n = None
print(type(n))  # NoneType
# Descripción: `None` representa la ausencia de valor.
# Description: `None` represents the absence of a value.
