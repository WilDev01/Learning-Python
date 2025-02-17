# Why control structures?
# Que son las estructuras de control?

# Control structures are the way in which flow sequences are conducted, that is,
# they follow a series of steps in a pre-established order to meet an objective.
# Las estructuras de control son la forma como se conducen las secuencias de flujo,
# es decir que siguen una serie de pasos en el orden preestablecido para cumplir con un objetivo.

# Control structures
# Estructuras de control

# If
# Sí

# The "IF" is a control structure where it is executed only if a condition is met
# El "si" es una estructura de control donde se ejecuta solamente si se cumple una condición.
if 2<4:
    print("true")

# If it is never fulfilled, it will never enter the condition
# Si nunca se cumple, nunca entrará en la condición
if 2>4:
    print("false")

# If Else
# Si no

# The if else is a control structure where if the "if" condition is not met it enters the "else", but if it enters the if it will execute the if condition
# El "if else" es una estructura de control donde si la condicioón "if" no se cumple entra al "else", pero si entra al if va a ejecutar la condición if    
if "Hello" == "hello":
    print("hello world!")
else:
    print("hello world false")


if "Hola" == "hola":
    print("Hola mundo!")
else:
    print("hola mundo false")


if 1 == 1:
    print("Your number is one")
elif 1 == 2: 
    print("Your number is two")
else:
    print("Error")
