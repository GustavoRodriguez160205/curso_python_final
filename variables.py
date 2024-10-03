# --- Definición de Variables ---
# Las variables son contenedores donde guardamos valores.
# Pueden ser de diferentes tipos: texto (string), número (int, float), etc.

# --- Nombres de Variables ---
# Reglas para nombrar variables:
# 1. Pueden empezar con una letra o un guión bajo
mi_variable = 'mi primer texto en Python'  
_miVariable = 'mi segundo texto en Python' 

# 2. No pueden comenzar con un número
# 5Variable = 5  # Esto daría error

# 3. Solo se permiten caracteres alfanuméricos y guiones bajos
mivariable123_ = 'texto'  # Variable válida, aunque puede ser difícil de leer
_123_mivariable = 'texto'  # También válida, pero poco clara

# 4. Distingue entre mayúsculas y minúsculas
miVariable = 'Texto1'  

# 5. No usar palabras reservadas de Python como nombres de variables
# and = 'Puto'  # Esto daría error porque 'and' es una palabra reservada





# --- Convenciones para Nombrar Variables ---
# 1. CamelCase: Cada palabra empieza con mayúscula a partir de la segunda
camelCase = 'Comienza con minúscula y cada palabra que le sigue comienza en mayúscula'

# 2. PascalCase: Todas las palabras empiezan con mayúscula
PascalCase = 'Comienza con mayúscula y cada palabra que le sigue comienza en mayúscula'

# 3. SnakeCase: Las palabras se separan por guiones bajos
snake_case = 'Comienza con minúscula y las palabras están separadas por guiones bajos'



# --- Multiasignación ---
# Permite asignar el mismo valor a varias variables
a = b = c = 'Gustavo'  # Ahora a, b y c tienen el valor 'Gustavo'




# --- Imprimir Valores por Pantalla ---
# Definimos algunas variables de texto
txt = 'Curso'
txt2 = 'de'
txt3 = 'JavaScript'

# Definimos algunas variables numéricas
num1 = 1
num2 = 2
num3 = 6

# --- Sumar Números ---
# Sumar los números y mostrar el resultado
#print(num1 + num2 + num3)  # Resultado de la suma

# --- Imprimir Números ---
# Imprimir los números separados por espacios
#print(num1, num2, num3)  # Imprime: 1 2 6

# --- Imprimir texto y números ---
#print( txt3 , num3)


# --- Variables Globales vs Scope ---

# Variable global
numero_global = 10

def operar():
    # Variable local
    numero_local = 5
    
    # Modificamos la variable global dentro de la función
    global numero_global
    numero_global += numero_local  # Suma el valor de la variable local a la global
    
    print("Dentro de la función:")
    print("Número global:", numero_global)  # Imprime el valor actualizado de la variable global
    print("Número local:", numero_local)     # Imprime la variable local

# Llamamos a la función
operar()

# Imprimimos la variable global fuera de la función
print("Fuera de la función:")
print("Número global:", numero_global)
