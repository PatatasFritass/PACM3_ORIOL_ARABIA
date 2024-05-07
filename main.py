import funciones
import funcionesMostrar
# 
# ejecutar →  python main.py
# Definimos el diccionario
diccionario = funciones.generarDic()
def main():
    # Funcion para mostrar el baner de bienvenida
    funcionesMostrar.bannerBienvenida()
    while True:
        funciones.clear()
        funcionesMostrar.menu()
        op = int(input("-> "))
        match op:
            case 1:
                # \|/
                funcionesMostrar.opcioMostrarDicionario()
                funciones.imprimirDic(diccionario)
                # opcion = input("Selecciona una opción (1-3): ")
            case 2:
                # \|/
                funcionesMostrar.opcioAnadir()
                funciones.anadirDicionario(diccionario)
                # print("Has seleccionado 'Añadir al dicionario'")
                #diccionario.update(palabraIndx.update(palabraDesc))
            case 3:
                funcionesMostrar.opcioMostrarModificarDic()
                funciones.modificarDic(diccionario)
                # funciones.ModificarDic()
                # print("Has seleccionado 'M
                # odificar el dicionario'")
            case 4:
                funcionesMostrar.opcioMostrarEliminar()
                funciones.eliminarMenu(diccionario)
                # print("Has seleccionado 'Eliminar el dicionario'")
            case 0:
                print("has seleccionado salir")
                break
            case _:
                print("Valor no valido")
        input("Pulsa Enter para continuar...")
    
if __name__ == "__main__":
    main()   
