import os

def SaveComponentMain(nombre: str):
    ruta_script = os.path.abspath(__file__)
    directorio_script = os.path.dirname(ruta_script)
    directorio_superior = os.path.dirname(directorio_script)
    sub_carpeta = os.path.join(directorio_superior, "src")

    try:
        archivos = os.listdir(sub_carpeta)
        if "main.ts" in archivos:
            archivo_path = os.path.join(sub_carpeta, "main.ts")
            with open(archivo_path, 'r') as archivo:
                contenido = archivo.read()
            aux = contenido + "export { " + nombre + " }" + f' from "./Icons/{nombre}";' 
            
            with open(archivo_path, 'w') as archivo:
                archivo.write(aux)
    except FileNotFoundError:
        print("error")
    

def SaveComponent(nombre: str, codigo: str):
    ruta_script = os.path.abspath(__file__)
    directorio_script = os.path.dirname(ruta_script)
    directorio_superior = os.path.dirname(directorio_script)
    sub_carpeta = os.path.join(directorio_superior, "src")
    iconos = os.path.join(sub_carpeta, "Icons")
    plantilla = 'import { FC } from "react"; \nimport { SvgComponentProps } from "./TypeIcon";\nexport const ' + nombre +  ': FC<SvgComponentProps> = ({height,width,color = "#000",fill = "none",...props}) =>'
    plantilla += f"\n({codigo});"
    archivo = os.path.join(iconos, f"{nombre}.tsx")
    
    with open(archivo, 'w') as ar:
        ar.write(plantilla)
    
    

