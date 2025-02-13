import re
def Parser(codigo: str):
    palabras_eliminar = ["width", "height"]
    palabras_reemplazar = ["fill", "stroke"]
    
    palabras_no_cammel_case = ["xmlns:xlink", "xml:space", "stroke-linecap", "stroke-linejoin", "fill-rule", "clip-rule"]
    palabras_cammel_case = ["xmlnsXlink", "xmlSpace", "strokeLinecap", "strokeLinejoin", "fillRule", "clipRule"]
    
    # Eliminamos las palabras que no necesitamos
    for palabra in palabras_eliminar:
        codigo = re.sub(f'{palabra}=".*?"', "", codigo)
    
    # Reemplazamos las palabras que necesitamos
    for palabra in palabras_reemplazar:
        if palabra == "fill":
            codigo = re.sub(f'{palabra}="(?!none).*?"', f'{palabra}="currentColor"', codigo)
        else:
            codigo = re.sub(f'{palabra}=".*?"', f'{palabra}="currentColor"', codigo)
    
    # Reemplazamos las palabras que necesitamos
    for i in range(len(palabras_no_cammel_case)):
        codigo = re.sub(f'{palabras_no_cammel_case[i]}', f'{palabras_cammel_case[i]}', codigo)
    
    # Añadir al final del primer > el atributo {...props} solo el primero
    codigo = re.sub(">", " {...props}>", codigo, 1)
    
    return codigo

