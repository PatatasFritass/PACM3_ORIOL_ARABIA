import os
def clear():
    clear = lambda: os.system('cls')
    clear()
    
# Genera automaticamente un dicionario por defecto  
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
# opcio 1
def imprimirDic(dic):
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario
        print(PK)
        for SUBPK in sorted(dic[PK].keys()):
            print("\t", SUBPK, ":")
            print("\t\t", dic[PK][SUBPK])
            print()
        print()


def correcionStringsTrueOrFalse(reff):
    print("Es correcto? S / N [[",reff,"]]")
    correcion = input("-> ")
    correcion = correcion.upper()
    
def crearReferenciaAndDefinicion():
  #   key
  # "xarxa": {     ENTRADA
          # referencia : definicion
          #   ref   :   def
          # "PESCA": "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o
    clear()
    print("--------------------------------")
    print("- - -   Creador de datos   - - -")
    print("--------------------------------")
    print("")
    while True:
        print("Introduce la nueva referencia")
        referencia = input("-> ")
        print()
        if (correcionStringsTrueOrFalse(referencia)==):
            break     
         
    
    
def comprobarDicionario(dic,keyUser):
    for PK in sorted(dic[PK].keys):
        if (PK == keyUser):
            print("ERROR")
            print("Ya existe ",keyUser)
            return True
        
        elif(PK != keyUser):
            # print("Guardando ",keyUser,"...")
            return False
        
def anadirEntrada(dic):
    # while True
    print("Introduce la palabra referente:")
    key = input("-> ")
    key = key.upper()
    if (comprobarDicionario(dic,key)==False):
        print()
    else:  
        print()
           
        
        
def mostrarKeyPalabras(dic):
    num=1
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario
        print("\t[",num,"]: " ,PK)
        num+=1
    print("\t[",0,"]: !!NEW KEY!!")
    print("Introduce [",0,"] para añadir una nueva key.")
    
# esto lo guardo demomento por si me va bien guardar la cantidad actual

return num-=1

def añadirDicionario(dic):
    # paraula = "xarxa"
    # entrada = {"PESCA" : "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o rombal."}
    opcioKEY = mostrarKeyPalabras(dic)
    print("Escribe el key del grupo de palabras")
    key = input("-> ")
    # key = key.upper()
        # Esta funcion comprueba que exista la key(la palabra principal)
    if key==0:
        if comprobarDicionario(dic,key)==True:
            print("No se a podido añadir!! ")
        else:
            anadirEntrada(dic)
            # print("Añadida correctamente")
            # return dic
    

# Prints del menu!!!

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
    
def opcioAnadir():
    clear()
    print("--------------------------------")
    print("Has seleccionado añadir: ")
    print("Dicionario completo...")
    print("--------------------------------")
    print(" ")

def opcioMostrarEliminar():
    clear()
    print("--------------------------------")
    print("Has seleccionado eliminar: ")
    print("Eliminar el dicionario...")
    print("--------------------------------")
    print(" ")

def menu():
    clear()
    print("________________________________")
    print("1) Mostrar dicionario completo")
    print("2) Añadir al dicionario")
    print("3) Modificar el dicionario")
    print("4) Eliminar el dicionario")
    print("0) Exit->")
    print("________________________________")
    
    
    
    
    