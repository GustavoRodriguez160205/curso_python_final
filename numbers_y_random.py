import random

# Declaración de tipos de números
# Número entero
numero_entero = 105

# Número decimal (float)
numero_decimal = 3.15

# Número complejo (con parte real e imaginaria)
numero_complejo = 5 + 2j

# Mostrar el tipo de dato de cada variable
print(f'Es un número entero: {numero_entero}, tipo: {type(numero_entero)}')
print(f'Es un número decimal: {numero_decimal}, tipo: {type(numero_decimal)}')
print(f'Es un número complejo: {numero_complejo}, tipo: {type(numero_complejo)}')

# Conversión de tipos de números
decimal_desde_entero = float(numero_entero)  # Convierte entero a float
entero_desde_decimal = int(numero_decimal)    # Convierte float a entero
complejo_desde_entero = complex(numero_entero) # Convierte entero a complejo
complejo_desde_decimal = complex(numero_decimal) # Convierte float a complejo

print(f'Decimal desde entero: {decimal_desde_entero}')
print(f'Entero desde decimal: {entero_desde_decimal}')
print(f'Complejo desde entero: {complejo_desde_entero}')
print(f'Complejo desde decimal: {complejo_desde_decimal}')

# Generación de números aleatorios
aleatorio = random.randrange(1, 10)  # El número de stop no es incluyente
print(f'Número aleatorio entre 1 y 9: {aleatorio}')

# Número aleatorio par
aleatorio_par = random.randrange(2, 12, 2)  # Número par del 2 al 10 (incluido)
print(f'Número aleatorio par entre 2 y 10: {aleatorio_par}')

# Número aleatorio impar
aleatorio_impar = random.randrange(1, 10, 2)  # Número impar del 1 al 9
print(f'Número aleatorio impar entre 1 y 9: {aleatorio_impar}')

# Ejemplo de conversión de tipos
numero = 7.8
entero = int(numero)  # Resulta en 7
print(f'Convertido a entero: {entero}')
complejo = complex(numero)  # Resulta en (7.8+0j)
print(f'Convertido a complejo: {complejo}')

# Generar un número aleatorio entre 20 y 50
numero_aleatorio = random.randrange(20, 51)  # El 51 no está incluido
print(f'Número aleatorio entre 20 y 50: {numero_aleatorio}')

# Generar una lista de 5 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randrange(1, 101) for _ in range(5)]
print(f'Lista de 5 números aleatorios entre 1 y 100: {numeros_aleatorios}')
