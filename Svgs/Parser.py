import re
def Parser(codigo: str):
    palabras_to_parse = ["width=", "height=", "fill=", "stroke="]
    palabras_code = ['{width}', '{height}', '{fill}', '{color}']

    for i in range(len(palabras_to_parse)):
        palabra = palabras_to_parse[i]
        patron = rf'{palabra}"[^"]*"'
        coincidencias = re.findall(patron, codigo)
        if len(coincidencias) == 1:
            for palabra in coincidencias:
                codigo = codigo.replace(palabra, f"{palabras_to_parse[i]}{palabras_code[i]}", 1)
        elif len(coincidencias) > 1 and palabra == "fill=":
            for palabra in coincidencias:
                codigo = codigo.replace(palabra, f"{palabras_to_parse[i]}{palabras_code[3]}", 1)
        elif len(coincidencias) > 1 and palabra == "width=":
            codigo = codigo.replace(coincidencias[0], f"{palabras_to_parse[i]}{palabras_code[i]}", 1) 
    
    
    codigo = codigo.replace(">", " {...props}>", 1)
    return codigo

