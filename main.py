import funciones
# 
# ejecutar →  python main.py
def main():
    # Funcion para mostrar el baner de bienvenida
    funciones.bannerBienvenida()
    # Definimos el diccionario
    diccionario = {}
    
    while True:
        funciones.clear()
        funciones.menu()
        
        opcion = input("-> ")
        
        
        
        match int(opcion):
            case 1:
                opcionMostrar1()
                print(diccionario)
                # opcion = input("Selecciona una opción (1-3): ")
            case 2:
                print("Has seleccionado 'Añadir palabra'")
                #diccionario.update(palabraIndx.update(palabraDesc))
            case 3:
                print("Has seleccionado 'eliminar palabra'")
                
            case 0:
                print("has seleccionado salir")
                break
            case _:
                print("Valor no valido")
        input("Pulsa Enter para continuar...")
        
    
    
if __name__ == "__main__":
    main()   
