# Cadenas de Texto
        #01234567 cuenta espacios tmb
texto = 'Este es un curso de python'

# Tipos de Comillas
comillasSimples = 'Este es un texto'
comillasDobles = "Este es un texto en comillas dobles"
comillasTriples = '''Este es un texto en comillas simples triples'''
comillasDoblesTriples = """Este es un texto en comillas dobles  triples"""

# Type : Nos devuelve que tipo es
print(type(comillasDobles))

# Podemos selecionar un caracter por índice
carac = texto[9]
print(f'El caracter es : {carac}')


# Para sacar la longitud de una cadena de texto

longitud = len(texto)
print(f'La longitud de el texto es : {longitud}')

# In para saber si está incluido en el texto
print('python' in texto) # Devuelve true si esta , false si no
