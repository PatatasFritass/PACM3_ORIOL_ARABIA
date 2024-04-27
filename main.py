import funciones
# 
# ejecutar →  python main.py
# Definimos el diccionario
diccionario = funciones.generarDic()
def main():
    # Funcion para mostrar el baner de bienvenida
    funciones.bannerBienvenida()
    
    
    while True:
        funciones.clear()
        funciones.menu()
        
        opcion = input("-> ")
        
        
        
        match int(opcion):
            case 1:
                funciones.opcioMostrar1()
                funciones.imprimirDic(diccionario)
                # opcion = input("Selecciona una opción (1-3): ")
            case 2:
                print("Has seleccionado 'Añadir al dicionario'")
                #diccionario.update(palabraIndx.update(palabraDesc))
            case 3:
                print("Has seleccionado 'Modificar el dicionario'")
                
            case 0:
                print("has seleccionado salir")
                break
            case _:
                print("Valor no valido")
        input("Pulsa Enter para continuar...")
        
    
    
if __name__ == "__main__":
    main()   
