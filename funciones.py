import os
import funciones
import funcionesMostrar
def clear():
    clear = lambda: os.system('cls')
    clear()
    
# Genera automaticamente un dicionario por defecto  
def generarDic():
    dic = {
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
        },
        "INSTITUTO": {
            "organización": "Grupo de científicos y tecnólogos avanzados que operan desde una base secreta, dedicados a la investigación y el avance tecnológico",
            "tecnología": "Poseen tecnologías altamente avanzadas, incluyendo androides sintéticos y teleportación",
            "misterio": "Sus actividades y objetivos a menudo están envueltos en secreto, generando especulaciones y misterios en el yermo"
        }
    }

    return dic

# -- Imprime todas las palabras con su contenido
# opcio 1
def imprimirDic(dic):
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario
        print("#############################")
        print("[[",PK,"]]")
        for SUBPK in sorted(dic[PK].keys()):
            print("\t[",SUBPK,"]:")
            print("\t\t",dic[PK][SUBPK])
            print()
        print()
        
def correcionStringsTrueOrFalse(reff):
    print("Es correcto? S / N [[",reff,"]]")
    correcion = input("-> ")
    correcion = correcion.upper()
    if (correcion=="S"):
        return True
    elif (correcion=="N"):
        print("Has selecionado [N]") 
    else:
        print("SYNTAX ERROR")

def crearReferencia():
  #   key
    # "xarxa": {     ENTRADA
          # referencia : definicion
          #   ref   :   def
          # "PESCA": "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o
    clear()
    funcionesMostrar.panelCrearReferencia()
    while True:
        print("Introduce la nueva referencia")
        ref = input("-> ")
        print()
        if (correcionStringsTrueOrFalse(ref)==True):
            return ref
 
def crearDefinicion():
    clear()
    
    while True:
        print("Introduce la nueva definicion")
        deff = input("-> ")
        print()
        if (correcionStringsTrueOrFalse(deff)==True):
            return deff       
                      
def comprobarDicionario(dic,keyUser):
    for PK in dic:
        if (PK == keyUser):
            print("ERROR")
            print("Ya existe ",keyUser)
            return True
        
        elif(PK != keyUser):
            # print("Guardando ",keyUser,"...")
            return False
        
def anadirEntrada():
    # while True
    reff=crearReferencia()
    deff=crearDefinicion()
    entrada = {reff : deff}
    return entrada
        
def mostrarKeyPalabrasAdd(dic):
    num=1
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario
        print("\t[",num,"]: " ,PK)
        num+=1
    print("\t[",0,"]: !!NEW KEY!!")
    print(" ")
    print("Introduce [",0,"] para añadir una nueva key.")
    num -=1
    # Nos retornara la cantidad de KEY que a printado
    return num

def mostrarKeyPalabrasMod(dic):
    num=1
    clear()
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario
        print("\t[",num,"]: " ,PK)
        num+=1
    print(" ")
    print("Introduce un numero para modificar una key.")
    num -=1
    # Nos retornara la cantidad de KEY que a printado
    return num

def mostrarKeyPalabrasDelete(dic):
    num=1
    clear()
    
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario
        print("\t[",num,"]: " ,PK)
        num+=1
    print(" ")
    print("Introduce un numero para eliminar una key.")
    num -=1
    # Nos retornara la cantidad de KEY que a printado
    return num

def mostrarReffPalabrasMod(dic,keyNUM):
    auxK=0
    funcionesMostrar.panelModReferencia()
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario
        auxK+=1
        if (auxK==keyNUM):
            num=0
            for SUBPK in sorted(dic[PK].keys()):
                num+=1
                print("\t[",num,"]: " ,SUBPK)
            
            print()
            num -=1
            return num
        
def crearKeyNombre():
    while True:
        print("Introduce la nueva KEY")
        keyNombre = input("-> ")
        print()
        if (correcionStringsTrueOrFalse(keyNombre)==True):
            return keyNombre  

def devolverNombreKey(dic,keyNUM):
    num=1
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario   
        if(num==keyNUM):
            
            return PK
        num+=1  

def devolverNombreReff(dic,keyNUM,reffNUM): 
    auxK=0
    for PK in sorted(dic.keys()): # ← pasa por cada palabra del dicionario
        auxK+=1
        if (auxK==keyNUM): # 7
            num=0
            for SUBPK in sorted(dic[PK].keys()): # 8
                num+=1
                if (num==reffNUM):
                    return SUBPK

def anadirDicionario(dic):
    # paraula = "xarxa"
    # entrada = {"PESCA" : "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o rombal."}
    mostrarKeyPalabrasAdd(dic) 
    print("Escribe el numero del grupo de las acepciones")
    keyNUM = int(input("-> "))
    # key = key.upper()
    # me falte definir el que cuando sea 0 tiene que pedirte el nombre que tendra keyNAME 
    if keyNUM==0:
        keyNAME=crearKeyNombre()
        entrada=anadirEntrada()
            # palabra="economia"
            # acepcion="banco"
            # definicion = "Lugar donde se lleban a cabo transacciones"
            # entrada={acepcion:definicion}
        dic.update({keyNAME:entrada})
    elif(keyNUM!=0):
        
        keyNAME=devolverNombreKey(dic,keyNUM)
        print("Has elegido:[",keyNAME,"]:")
        entrada=anadirEntrada()
        # print(dic)
        
        # auxiliar = diccionari[paraula]
        aux=dic[keyNAME]
        
        # auxiliar.update(entrada)
        print(entrada)
        aux.update(entrada)
        
        # diccionari.update({paraula:auxiliar})  
        dic.update({keyNAME:aux})
                    
        print(dic[keyNAME])
        input("pausa")

        # if(comprobarDicionario(dic,keyNAME)==True):  
        #      print("No se a podido añadir!! ")
        #      print("YA EXISTE ",keyNAME,"!! ") 
        # else:
            # entrada=anadirEntrada()
            # # print(dic)
            # print(keyNAME)
            # print(entrada)
            # dic.update({keyNAME:entrada})
            
            
            
            # return dic
        # Esta funcion comprueba que exista la key(la palabra principal)
        # if comprobarDicionario(dic,key)==True:
        #     print("No se a podido añadir!! ")
        # else:    
            # print("Añadida correctamente")
            # return dic    


def modificarDic(dic):
    clear()
    funcionesMostrar.menuModificarDic()
    opcion = int(input("-> "))
    
    match opcion:
        case 1:
            # 1- Mod Key
            # diccionario["new_key"] = diccionario.pop("old_key")
            mostrarKeyPalabrasMod(dic)
            keyNUM = int(input("-> "))
            
            keyNew=crearKeyNombre()
            keyOld=devolverNombreKey(dic,keyNUM)
            dic[keyNew] = dic.pop(keyOld)
            print("")
        case 2:
            # 2- Mod palabra
            # diccionario["key"]["new_reff"] = diccionario["key"].pop("old_reff")
            # 
            mostrarKeyPalabrasMod(dic)
            keyNUM = int(input("-> "))
            opcionKey=devolverNombreKey(dic,keyNUM)
            # 
            mostrarReffPalabrasMod(dic,keyNUM)
            reffNUM = int(input("-> "))
            
            reffNew=crearReferencia()
            reffOld=devolverNombreReff(dic,keyNUM,reffNUM)
            
            dic[opcionKey][reffNew] = dic[opcionKey].pop(reffOld)
            
            print("")

        case 3:
            # 3- mod Descripcion
            # diccionario["key"]["reff"] = "Los jueves se come rabo de toro"
            print("")
            mostrarKeyPalabrasMod(dic)
            keyNUM = int(input("-> "))
            opcionKey=devolverNombreKey(dic,keyNUM)
            # 
            mostrarReffPalabrasMod(dic,keyNUM)
            reffNUM = int(input("-> "))
            opcionReff=devolverNombreReff(dic,keyNUM,reffNUM)
            #
            deff=crearDefinicion()            
            dic[opcionKey][opcionReff] = deffdeff
        case _:
            # Salir
            print("Valor no valido")            

    
    
    
    
def eliminarMenu(dic):
    clear()
    
    funcionesMostrar.menuEliminarDic()
    opcion = int(input("-> "))
    
    match opcion:
        case 1:
            # 1- Mod Key
            # diccionario["new_key"] = diccionario.pop("old_key")
            funcionesMostrar.opcioMostrarEliminarKey()
            mostrarKeyPalabrasDelete(dic)
            keyNUM = int(input("-> "))
            
            key=devolverNombreKey(dic,keyNUM)
            dic.pop(key)
            print("")
        case 2:
            # 2- Mod palabra
            # diccionario["key"]["new_reff"] = diccionario["key"].pop("old_reff")
            # 
            funcionesMostrar.opcioMostrarEliminarReff
            mostrarKeyPalabrasDelete(dic)
            keyNUM = int(input("-> "))
            opcionKey=devolverNombreKey(dic,keyNUM)
            # 
            mostrarReffPalabrasMod(dic,keyNUM)
            reffNUM = int(input("-> "))
            
            opcionReff=devolverNombreReff(dic,keyNUM,reffNUM)
            
            dic[opcionKey].pop(opcionReff)
            
            print("")     
        case _:
             # Salir
            print("Valor no valido")   
    

    
        
                                                                                                                                            
#                                                                                     ██████                                              
#                                                                                   ▓▓░░░░  ▓▓                                            
#                                                                 ▓▓██            ▓▓        ░░▓▓▓▓██                                      
#                                                               ▓▓██      ▓▓▓▓▓▓██            ░░░░  ██                                    
#                                                             ░░░░██    ██░░░░░░                      ▓▓                                  
#                                                             ██  ░░▓▓▓▓                              ░░██                                
#                                                             ██    ░░░░    ▓▓██      ▓▓██              ░░▓▓                              
#                                                             ██          ██░░░░██████░░░░██                ██                            
#                                                             ██        ██░░░░░░░░░░░░░░░░▓▓▒▒    ▒▒▒▒▒▒    ██                            
#                                                             ██▒▒    ██░░░░░░░░░░░░░░░░░░░░▒▒████▓▓▒▒▒▒██  ░░██                          
#                                                           ▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░██    ██                          
#                                                           ██    ██▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░    ██                          
#                                                             ▒▒░░▒▒██▒▒░░░░░░░░░░░░░░░░▓▓▓▓░░░░░░░░▓▓        ██                          
#                                                               ██░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░██        ██                          
#                                                             ██░░░░░░██░░░░░░██░░░░░░░░░░░░░░░░░░░░░░██      ██                          
#                                                             ██░░░░████░░░░░░██░░░░░░██████░░░░░░░░░░░░████  ██                          
#                                                             ██░░░░████░░░░██░░░░░░░░░░░░██░░░░░░░░░░██░░░░████                          
#               ██████                                      ██░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██████                            
#             ██░░░░░░██                                    ██░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██                            
#           ██░░░░░░░░██                                    ██░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░████                              
#           ██░░░░░░░░██                                    ██░░░░░░░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██                            
#           ██░░░░░░██                                      ██░░░░██████░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██                            
#           ██░░░░░░██                                        ██░░██    ████████████    ██░░░░░░░░░░░░░░░░░░██                            
#             ██░░░░▒▒██                                      ██░░░░██                ████░░░░░░░░░░░░░░░░██                              
#             ██░░░░░░██                                      ██░░░░░░▓▓██      ▓▓▓▓██░░░░░░░░░░░░░░░░████                                
#             ██░░░░░░▒▒▓▓                                      ██░░░░░░░░▓▓▓▓██░░░░░░░░░░░░░░░░░░░░██                                    
#     ▓▓▓▓▓▓████▓▓▓▓██░░░░▓▓                                    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                                      
#   ▓▓░░░░░░░░░░░░░░░░▓▓░░▒▒██                                    ▓▓░░░░░░▓▓██░░░░░░░░░░░░░░░░░░████                                      
#   ██░░░░░░░░░░░░░░░░▒▒▓▓░░▒▒▓▓                                  ████░░░░░░░░░░░░░░░░░░░░░░▓▓▓▓██░░▓▓▓▓                                  
#   ██░░░░░░░░░░░░░░░░░░██░░░░████▓▓▓▓▓▓▓▓▒▒              ▓▓▓▓▓▓▓▓████▓▓░░░░░░░░░░░░░░░░░░▓▓▒▒██░░  ░░████▓▓                              
#     ██████████████░░░░██░░░░██░░██▒▒▒▒▒▒▒▒██████████████▒▒▒▒▒▒▒▒▒▒██  ████░░░░░░░░██░░░░░░░░██      ██▒▒▒▒████                          
#   ▓▓░░░░░░░░░░░░▒▒▓▓▓▓▒▒░░░░██░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  ░░░░▓▓▓▓▓▓▓▓░░░░░░░░██░░      ██▒▒▒▒▒▒▒▒▓▓▓▓                      
#   ██░░░░░░░░░░░░░░░░░░██░░░░██░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          ██░░░░██████        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██                    
#   ██░░░░░░░░░░░░░░░░░░██░░░░██░░██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██            ▓▓▓▓░░░░░░        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  
#   ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░██░░░░██░░██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓                        ▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒              
#     ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒░░▓▓▓▓░░██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                  ▒▒██▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒            
#     ██░░░░░░░░░░░░░░░░██░░██░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██              ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██          
#       ██░░░░░░░░░░░░░░██░░██░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒██            ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██        
#         ██████████████░░░░██░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████▒▒▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓        
#           ██░░░░░░░░░░░░████░░██▓▓▓▓▓▓▓▓▓▓████████      ██▒▒▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██      
#             ████████████    ██████████████              ██▒▒▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██    
#                                                         ██▒▒▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██  
#                                                         ██▒▒▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██
#                                                         ██▒▒▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██
#                                                         ██▒▒▒▒▒▒▒▒▒▒▒▒██        ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██  ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██
#                                                         ██▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██      ██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██
#                                                         ██▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██      ██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██
#                                                         ██▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██      ██▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██  
#                                                         ██▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██    ██▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██  
#                                                         ██▒▒▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██    ██▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██    
#                                                           ██▒▒▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██  ▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██    
#                                                           ████▒▒▒▒▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██    ██▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
#                                                           ██░░████▒▒██          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██  ██▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
#                                                           ██  ░░░░████          ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
#                                                           ██      ░░            ░░██████████████░░░░░░  ██  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        
#                                                           ██                      ░░░░░░░░░░░░░░        ████▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓          
#                                                           ██                                            ████░░▒▒██████▓▓▓▓▓▓            
#                                                           ░░▓▓                                          ██▒▒░░░░▒▒▒▒░░██▓▓              
#                                                             ██▓▓                                        ██░░░░░░░░░░░░██▒▒▒▒            
#                                                             ██▓▓▓▓▓▓██                              ▒▒██████░░░░░░░░▓▓░░░░▓▓            
#                                                             ██▒▒▓▓▓▓▒▒▒▒▒▒▒▒██          ▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██░░░░░░▓▓██░░░░▓▓            
#                                                             ██▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓██░░░░░░████▓▓░░▓▓            
#                                                             ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░▒▒▒▒░░░░▓▓            
#                                                             ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▒▒              
#                                                             ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██░░░░░░░░░░                
#                                                               ████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓██████                            
#                                                                   ████████████████████████████████████  