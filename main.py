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
        op = input("-> ")
        
        match int(op):
            case 1:
                funciones.opcioMostrarDicionario()
                funciones.imprimirDic(diccionario)
                # opcion = input("Selecciona una opción (1-3): ")
            case 2:
                funciones.opcioAnadir()
                funciones.anadirDicionario(diccionario)
                # print("Has seleccionado 'Añadir al dicionario'")
                #diccionario.update(palabraIndx.update(palabraDesc))
                
            case 3:
                funciones.opcioMostrarModificarDic()
                # print("Has seleccionado 'Modificar el dicionario'")
                
            case 4:
                funciones.opcioMostrarEliminar()
                # print("Has seleccionado 'Eliminar el dicionario'")
            
            case 0:
                print("has seleccionado salir")
                break
            case _:
                print("Valor no valido")
        input("Pulsa Enter para continuar...")
        
    
    
if __name__ == "__main__":
    main()   
