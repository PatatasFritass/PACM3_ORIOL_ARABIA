import os
def clear():
    clear = lambda: os.system('cls')
    clear()
    
    
def generarDic():
    diccionario = {
        "VAULT": {
            "refugio": "Estructura subterránea diseñada para proteger a la población de Fallout",
            "experimento": "Proyecto de Vault-Tec con propósitos secretos y a menudo cuestionables",
            "símbolo": "Icono reconocible del universo de Fallout, representando seguridad y misterio"
        },
        "RADROACH": {
            "insecto": "Criatura radiactiva que ha mutado a partir de cucarachas",
            "amenaza": "Peligro común en las zonas contaminadas de Fallout",
            "fuente": "Fuente potencial de carne y componentes para la supervivencia en el yermo"
        },
        "SUPERMUTANTE": {
            "mutación": "Resultado de la exposición a altos niveles de radiación y FEV (Virus de Evolución Forzada)",
            "enemigo": "Frecuente oponente en el mundo post-apocalíptico de Fallout",
            "historia": "Creados originalmente como soldados durante la Gran Guerra, ahora son una amenaza para la humanidad"
        },
        "NCR": {
            "república": "Nueva República de California, una de las facciones principales en el mundo de Fallout",
            "gobierno": "Organización política que intenta establecer una democracia en el yermo post-apocalíptico",
            "conflicto": "A menudo se encuentra en conflicto con otras facciones por el control de territorios y recursos"
        },
        "GECK": {
            "tecnología": "Jardín del Edén Creation Kit, dispositivo de alta tecnología capaz de terraformar un área y proporcionar recursos",
            "objeto": "Objetivo deseado por muchos supervivientes debido a su potencial para reconstruir y mejorar comunidades",
            "mito": "Fuente de leyendas y rumores en el yermo, con historias sobre sus capacidades milagrosas"
        }
    }
    return diccionario

# -- Imprime todas las palabras con su contenido
def imprimirDic(dic):
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario
        print(PK)
        for SUBPK in sorted(dic[PK].keys()):
            print("\t", SUBPK, ":")
            print("\t\t", dic[PK][SUBPK])
            print()
        print()
    
def bannerBienvenida():
    clear()
    print("--------------------------------")
    print("Creat Per Oriol Arabia")
    print("Este es el proyecto de Pyton")
    print("--------------------------------")
    input("Pulsa Enter para continuar...")
    
    
    
    
def opcioMostrarDicionario():
    clear()
    print("--------------------------------")
    print("Has seleccionado mostrar: ")
    print("Dicionario completo")
    print("--------------------------------")
    print(" ")

def opcioMostrarModificarDic():
    clear()
    print("--------------------------------")
    print("Has seleccionado modificar: ")
    print("Dicionario completo...")
    print("--------------------------------")
    print(" ")       

def opcioMostrarModificar():
    clear()
    print("--------------------------------")
    print("Has seleccionado modificar: ")
    print("Dicionario completo...")
    print("--------------------------------")
    print(" ")   
    
def opcioMostrarAnadir():
    clear()
    print("--------------------------------")
    print("Has seleccionado añadir: ")
    print("Dicionario completo...")
    print("--------------------------------")
    print(" ")

def opcioMostrarEliminar():
    clear()
    print("--------------------------------")
    print("Has seleccionado añadir: ")
    print("Dicionario completo...")
    print("--------------------------------")
    print(" ")

def menu():
    clear()
    print("________________________________")
    print("1) Mostrar dicionario completo")
    print("2) Añadir al dicionario")
    print("3) Modificar el dicionario")
    print("0) Exit->")
    print("________________________________")
    
    
    
    
    