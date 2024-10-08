# Ejemplo de manipulación de cadenas en Python

# Cadena de texto inicial
texto = 'Este es un curso de python'

# Diferentes tipos de comillas en Python
comillas_simples = 'Texto con comillas simples'
comillas_dobles = "Texto con comillas dobles"
comillas_triples_simples = '''Texto con comillas triples simples'''
comillas_triples_dobles = """Texto con comillas triples dobles"""

# Verificar el tipo de las variables
print(f"Tipo de comillas_dobles: {type(comillas_dobles)}")

# Acceder a un carácter específico por su índice
caracter_en_indice_9 = texto[9]
print(f'El carácter en el índice 9 es: {caracter_en_indice_9}')  # Imprime "u"

# Obtener la longitud de la cadena
longitud_texto = len(texto)
print(f'La longitud del texto es: {longitud_texto}')  # Imprime la longitud total de la cadena

# Comprobar si una palabra está en el texto
existe_python = 'python' in texto
print(f'¿Está "python" en el texto?: {existe_python}')  # Devuelve True

# Comprobar si una palabra no está en el texto
no_existe_javascript = 'JavaScript' not in texto
print(f'¿No está "JavaScript" en el texto?: {no_existe_javascript}')  # Devuelve True

# Slicing: Extraer partes de la cadena
print(f"Texto entre índices 10 y 16: '{texto[10:16]}'")  # Imprime "curso"
print(f"Texto desde el inicio hasta el índice 5: '{texto[:5]}'")  # Imprime "Este "
print(f"Texto desde el índice -4 hasta el final: '{texto[-4:]}'")  # Imprime "thon"

# Explicación del slicing texto[:-37]
# - El número negativo -37 indica que queremos contar hacia atrás desde el final de la cadena.
# - Como la longitud total del texto es menor que 37, el slicing no devuelve nada.

# Modificadores de texto

# Textos de ejemplo
texto_secundario = 'Este es un mega curso de python'
otro_de_prueba = "     Hola Mundo         "
texto_con_comas = 'No , sean , putos'

# Convertir texto a mayúsculas
mayusculas = texto_secundario.upper()
print(f'El texto en mayúsculas es: {mayusculas}')

# Convertir texto a minúsculas
minusculas = texto_secundario.lower()
print(f'El texto en minúsculas es: {minusculas}')

# Eliminar espacios en blanco al principio y al final
texto_sin_espacios = otro_de_prueba.strip()
print(f'Texto sin espacios: {texto_sin_espacios}')

# Reemplazar una palabra en el texto
reemplazo_texto = otro_de_prueba.replace('Mundo', 'Universo')
print(f'Texto reemplazado: {reemplazo_texto}')

# Separar el texto en una lista utilizando comas como delimitador
separar_por_comas = texto_con_comas.split(",")
print(f'Texto separado por comas: {separar_por_comas}')

# Concatenación de cadenas
a = 'Hola'
b = 'Mundo'
c = a + ' ' + b  # Se añade un espacio entre "Hola" y "Mundo"
print(f'Texto concatenado: {c}')

# Template Strings
precio = 19.99
producto = 'camiseta'
cantidad = 3
texto_template = f'El precio de cada {producto} es {precio:.2f}, y se compraron {cantidad} unidades.'
print(texto_template)

# Nota sobre '.2f': Esto formatea el precio para que tenga 2 decimales, útil para valores numéricos como precios.

# Escapes (uso de barra invertida \)
escape = "Mi país favorito es \"Argentina\""
salto_linea = 'Quiero hacer un \nsalto de línea'
print(salto_linea)
print(escape)

# Métodos más usados

texto_A_modificar = 'este es Un texto A MODIFICAR'

# Capitalizar el texto: convierte la primera letra a mayúscula y el resto a minúscula
primer_letra = texto_A_modificar.capitalize()
print(f'Pone la primera letra en mayúscula: {primer_letra}')

# Comprobar si el texto comienza con una letra o palabra
comienza_con_a = texto_A_modificar.startswith('A')
print(f'¿Comienza con "A"?: {comienza_con_a}')  # Esto devuelve False porque la cadena comienza con 'e'

# Corregir: Comprobar si el texto comienza con una palabra
comienza_con_este = texto_A_modificar.startswith('este')
print(f'¿Comienza con "este"?: {comienza_con_este}')  # Devuelve True

# Comprobar si el texto termina con una palabra o letra
termina_con_modificar = texto_A_modificar.endswith('MODIFICAR')
print(f'¿Termina con "MODIFICAR"?: {termina_con_modificar}')  # Devuelve True

# Pone todo a maypuscula las primeras palabras
titulo = texto_A_modificar.title()
print(f'Pone en mayúscula cada palabra {titulo}')


# Cuenta cuantas veces aparece una palabra 
contador = texto_A_modificar.count('e')
print(f'La palabra que más se repite es {contador}')

# Nos dice la posicion de la palabra
encontrador = texto_A_modificar.find('texto')
print(f'La posicion de la palabra es {encontrador}') 

if edad >= 12:
    print('No puede pasar')
    else:
        print('Puede pasar')