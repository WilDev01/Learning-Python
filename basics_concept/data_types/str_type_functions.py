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

data_text_capitalize_first_letter = data_text_lower.capitalize()
print(data_text_capitalize_first_letter)

