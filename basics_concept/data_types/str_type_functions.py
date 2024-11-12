# Str functions
# Funciones str

data_text = "This is the text for the test"

# Basic operations
# Operaciones basicas

# Concatenate
# Concatenate is used to join different text into one, although it can also be joined with other types of data are finally parsed to str
# Concatenar se utuliza para unir diferentes textos en uno, aunque tambien se puede unir con otros tipos de datos que al final se parsean a str

data_text_concat_with_other_text = data_text + ", one text"

data_text_two = "the text into other var"
data_text_concat_with_other_var = data_text + data_text_two 

data_text_concat_with_others_data_types = data_text + str(2) + " " + str(True) + " " + str(2.0)

print(
    data_text_concat_with_other_text,
    data_text_concat_with_other_var,
    data_text_concat_with_others_data_types
)

# Repeat
# Repeating is a process in which a text is repeated with *
# Repetir es un proceso en el que se repite un texto con *

data_text_repeat = data_text * 4
print("@@@@", data_text_repeat)

# Len
# Len is a function that counts the characters in the text
# Len es una función en la que se cuentan los caracteres que tiene el texto
print(len(data_text))

# Case handling
# Manipulaciòn de caso

# Lower
# Minúsculas
# The lower() method in Python is used to convert a string to lowercase. It takes no arguments and returns a new string with all uppercase characters converted to lowercase. 
# El método lower() de Python se utiliza para convertir una cadena a minúsculas. No acepta argumentos y devuelve una nueva cadena con todos los caracteres en mayúscula convertidos a minúsculas.
print("___________________________ \n")
data_text_lower = data_text.lower()
print(data_text_lower)

# Upper
# Mayúsculas
# The upper() method in python is used to convert a string to uppercase. It rakes no argument and returns a new string with all lowercase characters converted to uppercase.
# El método lower() de Python se utiliza para convertir una cadena a mayúsculas. No acepta argumentos y devuelve una nueva cadena con todos los caracteres en minusculas convertidos a mayusculas.
data_text_upper = data_text.upper()
print(data_text_upper)

# Capitalize first letter
# Capitalizar primera letra
# The capitalize method capitalize the first letter of the text
# El metodo capitaze capitaliza la primera letra del texto
data_text_capitalize_first_letter = data_text_lower.capitalize()
print(data_text_capitalize_first_letter)

# Capitalize every word
# Capitalizar cada palabra
# The Python title() function is used to change the initial character in each word to Uppercase and the subsequent characters to Lowercase and then returns a new string.
# La función title() de Python se utiliza para cambiar el carácter inicial de cada palabra a mayúsculas y los caracteres subsiguientes a minúsculas y luego devuelve una nueva cadena.
data_text_title = data_text.title()
print(data_text_title)

# Swapcase
# Caso de intercambio
# The swapcase() function is a built-in method in Python that can be used with the string data type. This function allows you to convert uppercase letters to lowercase and vice versa within a string.
# La función swapcase() es un método integrado en Python que se puede utilizar con el tipo de datos string. Esta función permite convertir letras mayúsculas en minúsculas y viceversa dentro de una cadena.
data_text_swapcase = data_text_title.swapcase()
print(data_text_swapcase)

# splitting and joining chains
# división y unión de cadenas

# Split
# Dividir
# The split() function still works if the separator is not specified by considering white spaces, as the separator to separate the given string or given line.
# La función split() aún funciona si no se especifica el separador considerando los espacios en blanco como el separador para separar la cadena o la línea dada.
data_text_split = data_text.split()
print(data_text_split)

# Dividir por lineas
# splitlines
# splitlines() is a built-in string method in Python that is used to split a multi-line string into a list of lines. It recognizes different newline characters such as \n , \r , or \r\n and splits the string at those points.
# splitlines() es un método de cadena integrado en Python que se utiliza para dividir una cadena de varias líneas en una lista de líneas. Reconoce diferentes caracteres de nueva línea, como \n , \r o \r\n, y divide la cadena en esos puntos.

data_text_splitline = data_text.splitlines()
print(data_text_splitline)

# Join
# Unir
# Join in Python is a built-in method used to join the elements of an iterable, separated by a string separator that you specify. So, whenever you want to join the elements of an iterable and convert it into a string, you can use string join in Python.
# Join en Python es un método integrado que se utiliza para unir los elementos de un iterable, separados por un separador de cadena que usted especifica. Por lo tanto, siempre que desee unir los elementos de un iterable y convertirlo en una cadena, puede utilizar la unión de cadenas en Python.
# Lista de elementos que quieres unir en una cadena
data_text_list = ["Hello", "world", "Python", "is", "great"]

data_text_join = " ".join(data_text_list)
print(data_text_join) 
