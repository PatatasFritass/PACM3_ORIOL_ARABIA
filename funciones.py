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
        },
        "INSTITUTO": {
            "organización": "Grupo de científicos y tecnólogos avanzados que operan desde una base secreta, dedicados a la investigación y el avance tecnológico",
            "tecnología": "Poseen tecnologías altamente avanzadas, incluyendo androides sintéticos y teleportación",
            "misterio": "Sus actividades y objetivos a menudo están envueltos en secreto, generando especulaciones y misterios en el yermo"
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
    print("--------------------------------")
    print("-- - Creador de referencia  - --")
    print("--------------------------------")
    print("")
    while True:
        print("Introduce la nueva referencia")
        ref = input("-> ")
        print()
        if (correcionStringsTrueOrFalse(ref)==True):
            return ref
 
def crearDefinicion():
    clear()
    print("--------------------------------")
    print("-- - Creador de definicion  - --")
    print("--------------------------------")
    print("")
    while True:
        print("Introduce la nueva definicion")
        deff = input("-> ")
        print()
        if (correcionStringsTrueOrFalse(deff)==True):
            return deff       
               
           
def comprobarDicionario(dic,keyUser):
    for PK in sorted(dic[PK].keys):
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
    entrada = {rff : deff}
    return entrada
        
def mostrarKeyPalabras(dic):
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
# esto lo guardo por el momento por si me va bien guardar la cantidad actual  

def anadirDicionario(dic):
    # paraula = "xarxa"
    # entrada = {"PESCA" : "Ormeig de pescar constituït per un teixit de fils nuats formant una retícula quadrada o rombal."}
    qttKEY = mostrarKeyPalabras(dic) 
    print("Escribe el numero del grupo de las acepciones")
    key = input("-> ")
    key = key.upper()
        
    if key==0:
        
        # Esta funcion comprueba que exista la key(la palabra principal)
        if comprobarDicionario(dic,key)==True:
            print("No se a podido añadir!! ")
        else:
            entrada=anadirEntrada()
            dic.update({key:entrada})
            # print("Añadida correctamente")
            # return dic
    

# Prints del menu!!!

def bannerBienvenida():
    clear()
    print("--------------------------------")
    print("Creat Per Oriol Arabia")
    print("Este es el proyecto de Pyton")
    print("--------------------------------")
    print("")
    dibujo = """
        ⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄⡀⠀⢿⡿⣁⠀⢆⡘⠤⡘⠠⢰⠃⡄⠂⠄⠀⠀⠀⠀⡀⡆⠌⢄⠀⠀⢠⡇⠂⡌⠄⠀⠀⠀⠀⠀⠀⠡⣖⠀⢃⠸⠀⠸⣟⡄⠘⡽⡜⡄⠀⠀⠀⠈⠦⠀⠀⠀⠸
        ⣿⣿⣿⣿⣿⣿⡿⠁⠈⢻⡝⣟⣷⡿⢁⠤⢀⠢⢌⠰⡀⠂⡟⠠⡄⠈⠀⠀⣀⠤⠐⣰⠌⡈⢄⠂⡡⣺⠄⡇⠰⠈⡄⢃⠰⢀⠰⢀⠂⢽⠂⢼⠐⡠⠄⣿⡼⡀⠱⢹⡰⠀⠀⠀⠀⠀⣆⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⠁⢄⠠⢀⣹⣞⡿⢁⢊⠰⢀⠎⡐⢂⠁⢳⠋⠴⠁⠀⣠⠞⡠⢁⣺⡇⠤⢁⠢⠘⢠⡿⢰⡏⠄⢃⡐⢈⠰⢈⠰⢸⠌⣸⠌⢺⡐⠤⢈⣽⣧⢩⡄⢉⢧⠡⠉⡍⠒⠤⣸⡀⠀⠀
        ⣿⣿⣿⣿⣿⣿⠩⡐⠌⢿⡯⣿⠇⡌⠢⢡⠈⡔⠈⠂⠃⢾⢈⠒⠀⡴⢁⡾⠑⣸⢻⢀⠒⢠⠂⡉⢼⡇⢸⡇⠌⠄⡄⢃⠰⢈⠰⠸⡂⢼⢈⢹⠆⠰⢸⢿⠸⡆⢷⢈⠸⣄⠃⠤⢉⡐⠨⣧⠀⡀
        ⣿⣿⣿⣿⣿⣿⡟⣿⣻⢾⡷⣿⠐⡄⢃⠆⠈⠐⠁⠀⠀⣾⠸⠀⢀⡇⣼⠇⢡⡏⣇⠢⠘⡀⠆⢡⡎⡇⢺⣇⠘⢠⠐⠨⡐⢂⠢⢡⡇⠾⢈⢸⡃⡘⢼⢸⠀⢻⠈⣇⠌⣷⢈⡐⠂⠤⢱⢿⠀⠔
        ⣿⣿⣿⣿⣿⣿⣯⡚⢧⡻⣽⡏⠰⡈⢄⠈⠀⡀⠀⠀⠀⣿⢸⢀⢂⢸⡟⡈⢼⢳⠁⢂⡁⠆⡑⢺⢱⡇⣼⢿⠈⠄⡈⠡⢐⠠⢁⢺⡄⡟⡀⢺⢁⡴⡿⢸⢄⠈⡇⢺⡆⢸⡆⠤⢉⠰⢐⣸⠈⠔
        ⣿⣿⣿⣿⣿⣿⣿⣷⠁⢿⣹⡇⠡⠌⠀⠀⠀⠀⠀⠀⢀⡿⣸⠀⢂⣿⢃⠐⡞⡼⢈⣄⣐⣤⡴⡯⢼⠴⡿⢼⠾⠶⠶⠶⣤⠂⠌⣹⢰⡇⡐⡏⢸⢡⡇⡽⡀⠑⢳⠐⣷⠀⢿⡇⠌⡐⠂⡽⢈⡐
        ⣿⣿⣿⣿⣿⣿⣿⡏⠠⣄⣿⠄⠀⠀⠀⠀⠀⡅⠀⠠⢠⡟⣧⠈⣰⣿⠀⣼⠴⡗⢉⠉⡐⢠⢷⠃⢸⢠⠃⢸⣿⠀⢀⠂⢸⠀⢂⡏⣼⠁⣸⠁⡏⡜⡇⡧⠬⣴⣼⣀⢿⢇⢸⣹⠀⠀⡁⠇⡃⠄
        ⣿⣿⣿⣿⣿⣿⣿⣇⡷⠊⢸⠀⠀⠀⢠⣦⣄⠇⡈⢁⠆⣿⣧⠐⣽⡇⠐⣾⢰⡇⢂⠡⢈⡏⡞⠀⡼⣸⠀⠀⣿⠀⠀⠂⣏⠐⢸⢡⡟⢀⡏⣼⢱⠁⣧⠁⠀⠀⠈⡟⣻⠺⣤⣿⡆⠐⠀⡇⠄⡈
        ⣿⣿⣿⣿⣿⣿⣿⣿⣄⠂⣿⠀⠀⢠⠃⢿⣣⠐⠠⠌⠠⣿⣿⠀⢿⠃⢌⣿⠸⡇⢀⢂⡼⡼⠀⢀⢧⡯⠄⡀⣿⠀⠌⢰⡇⠈⣼⡿⠁⡞⣸⢇⠇⢰⡟⠀⠀⠀⠈⡇⡝⠀⢇⡟⡧⣄⠂⡇⠀⢰
        ⣿⣿⣿⣿⣿⡿⢭⢿⣿⣶⣻⡆⠀⡏⠠⠸⡽⣏⠐⡈⡐⢿⣻⡠⣿⠈⢸⡍⣆⣧⣾⣾⣿⣿⣶⣾⣾⣆⠄⠀⣿⡆⠀⣸⠁⣸⡿⢁⡞⡕⡹⡌⠀⣼⢁⠤⠤⢀⣀⡇⡇⠀⠸⣼⡇⠀⠑⣷⠈⣸
        ⣿⣿⣿⣿⣿⡹⢎⣗⡻⣿⣷⣇⠘⣇⠄⡁⢻⣽⡆⠡⠠⢹⣿⡓⣿⣴⣿⣿⣿⣿⡿⣟⣿⢫⣟⣏⠉⠙⠛⠶⣿⢿⠀⡞⢀⡟⢡⣾⠊⣰⠟⠀⣼⠃⣐⣤⣴⣦⣤⣧⣇⣠⠀⣿⡇⠀⡁⡏⠀⡿
        ⣿⣿⣿⡟⣧⣛⡭⢶⡙⣿⢻⣿⡄⢻⡔⠠⡈⢧⢿⡆⢡⠈⢿⣇⣷⣿⡿⠛⣯⢽⡳⢧⡞⠀⠀⣽⡀⠀⠀⠀⠛⠘⠻⢣⣞⣴⠟⠁⠠⠏⠀⠐⠁⢸⣿⢿⣟⠿⣿⡿⣿⣷⣤⣸⡂⠀⢸⠃⢰⠇
        ⣿⣿⡿⣹⣧⡓⢾⢷⡟⢸⣯⢹⣷⡌⢻⣄⠱⣌⠳⣿⣦⠲⠾⣿⣿⣿⠁⠈⣟⠊⢿⡧⢿⠃⡜⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⣟⡑⢀⡻⡴⢷⠈⠻⣿⣿⣟⠋⡟⢀⡎⠄
        ⣿⣿⠳⣽⠲⣝⡿⢸⡇⣸⠙⣷⢺⣿⣧⡻⣷⣌⢢⡙⢽⣷⣤⠘⢧⠙⢦⡀⢻⡌⠀⢠⢁⠒⢯⡀⠀⠀⠀⠀⠀⡀⠀⢀⠀⢀⠀⠀⠀⠀⠀⠀⠀⡏⣷⣹⡏⠵⡙⣺⠀⠀⠸⣿⣿⣾⢁⡾⠀⣲
        ⣿⢫⡝⣾⢹⣾⢃⢹⡇⢼⠂⣿⣹⠋⢉⡿⣾⣿⣷⣌⠲⣽⢿⣿⣮⣷⣀⠈⠀⠙⠗⠒⠚⡋⠉⠀⠀⠀⠀⣺⠂⠀⠀⢀⠀⠠⠐⣀⡀⠂⠀⠀⠀⢷⢈⠩⠀⡡⠲⠏⠀⠀⣸⢟⣽⣫⡟⢁⣴⢏
        ⣏⢷⣙⣮⠟⡐⠢⢼⡇⢸⡿⢧⣟⠀⡇⡄⣤⢩⢿⣛⢷⣤⣭⣛⢿⣮⠉⠳⠦⣤⠁⠁⡡⢈⢄⠡⠅⡆⠂⠀⠀⡈⠀⢈⡠⠆⠨⢀⠀⠀⠀⠄⠐⠈⠙⡲⢷⡼⡆⠀⠄⡐⠁⣿⣿⣋⣴⣾⢋⣾
        ⣞⢺⣼⠏⡐⠌⡁⣿⡇⢸⡇⠼⣿⠀⢷⠀⢹⡆⣿⡉⠚⠶⣭⣻⣿⡟⠢⢄⢤⢇⡀⡅⠦⠠⡴⠀⠀⠐⢐⠀⠆⠃⠄⠖⠉⠂⠅⠊⠁⢒⠄⠐⣀⠀⠂⠉⣀⠁⡄⠁⠈⠐⢸⣿⢫⣿⡳⣵⡿⢿
        ⣎⡿⢼⠂⡅⢊⠔⣿⣵⢺⡏⠄⣿⣧⡈⠓⢌⠷⢾⡇⢁⠢⢀⢹⠑⣷⠈⡠⠏⠤⠨⣁⢃⠕⠋⡫⢗⠉⠈⡂⠁⠀⢂⠐⢁⠣⠀⠁⠀⠘⠒⠥⠴⢄⢀⠐⠁⠀⠐⠀⠀⠈⡿⣬⡿⢣⡓⣸⣇⢻
        ⣾⣃⡯⢼⣀⠣⣈⣿⡽⣺⠛⢠⠹⡻⣿⣦⡀⠑⠪⣇⠂⠔⡈⡾⠊⣿⠎⠵⠃⡓⠀⡀⠉⠄⠆⠁⠉⠀⠈⠡⠂⠀⠀⡀⢈⣀⠊⣡⠂⠀⡐⠛⠊⢁⠰⠖⠃⠀⠁⢀⡀⢰⠟⡞⠡⢠⢰⣿⠸⣸
        ⣿⣿⣳⢯⣿⣿⣿⣷⣽⣹⡇⠌⣷⢳⢋⠻⢿⣦⣀⡟⡀⠊⢰⡇⠂⣿⡇⠠⠁⠀⠁⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⡔⠁⠀⠉⠢⢀⠀⠀⠀⠀⠈⠈⠁⢀⠠⠊⠀⠈⢺⡞⠠⢁⢂⣯⡏⠵⡘
        ⣿⣿⡜⣿⣿⣿⣿⣿⢾⣻⣧⡂⢹⣏⣿⡄⠌⢻⣿⣧⠀⠡⣸⠠⠁⣾⡇⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⢀⡠⠐⠁⠀⠀⠀⠀⠀⠀⠀⠉⠫⣦⠀⠀⢀⠔⠁⠀⠀⠀⡀⠀⠙⢦⢁⡞⣼⡙⢦⠑
        ⣿⣿⡽⣹⣿⣿⣿⣿⡯⣷⣯⢿⣄⠻⣜⣷⡈⠄⢻⣷⠈⢠⡗⠠⠁⣿⢸⣄⠀⠀⠀⠀⠀⠀⢀⡔⠊⠉⠀⠀⠀⠀⠀⠀⡰⠂⠤⣀⠀⠀⢀⣃⠀⣰⠁⠀⠀⡴⢴⣧⠀⡀⠀⠀⠙⢦⡏⡝⢢⠌
        ⡿⣿⣿⣽⣿⢿⣿⣿⡷⣣⢿⣯⣻⢷⣽⢞⣿⡄⠂⣿⠀⣸⠃⠠⢁⣷⠸⡇⠑⢤⡀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⣀⠔⠀⠀⠀⠀⠈⢧⡀⢿⣿⣾⡿⠁⡠⢊⣴⣿⢸⡷⣄⣐⠀⢀⠄⠙⠓⠧⣌
        ⣿⣷⣿⣿⣿⣿⣿⣿⡿⣵⢫⣷⣏⣟⣾⣻⣾⣿⣆⢿⠀⡿⠀⠀⠂⣼⠐⣿⡀⢀⡼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⢄⡀⠀⠀⠀⠀⠑⠮⠿⠛⠒⢈⣴⣿⣿⡏⡾⢁⠈⣿⠖⠁⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⣿⣿⣿⣯⣟⣷⢯⣿⣿⣿⢰⠃⠀⠀⠐⢸⠀⣻⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⠄⡀⠀⠀⠀⢀⣠⣾⣿⣿⣿⣿⣃⠇⢂⢡⠏⠀⠀⠀⠀⢀⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⢾⡻⢷⣯⣿⣼⠀⠀⠀⢀⡼⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⣤⣀⡀⠀⠀⠀⠀⠈⠢⣤⣾⣿⣿⣿⣿⣿⣿⣿⢸⠠⡱⠃⠀⠀⠀⣠⣶⠋⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢾⣽⣯⣞⣽⡟⠀⣠⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⣷⣤⡀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣷⣿⢀⡜⠁⠀⠀⣠⡞⡱⠁⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢯⢿⣿⣿⣿⣧⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⢀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⡀⠀⠀⠀⠹⢿⣿⣿⣿⣿⡼⠀⠀⢀⣾⣿⡟⠀⠀⠀⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡻⣞⢾⡹⡿⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠂⢄⡀⠀⠀⣠⣿⣿⣿⣿⣦⣄⠀⠀⠀⠻⣿⣿⡟⢀⠀⣡⠂⢺⣿⡣⢀⢀⠄⠀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣝⣾⣿⣧⢶⡶⣿⢿⣿⣦⣤⣀⣀⣀⣤⣀⣴⣶⣤⣤⣄⡀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⢠⣾⣿⣾⡷⣰⠉⡆⣹⣿⣿⣶⣿⣆⡀⢀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣯⢷⣏⡿⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣽⣿⡿⠕⠉⢆⢱⢸⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⡽⣾⣹⡞⣷⡽⣞⡽⣯⢿⣹⢯⣿⣿⣿⣿⣯⣿⡿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⢪⢿⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⡽⣶⢯⡽⣞⣳⢯⡽⣞⣯⣽⢫⣿⡟⣿⣻⢿⡽⣿⣿⣿⣿⣻⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢷⣛⡾⣽⣹⡽⢾⣹⠷⣞⣞⠿⣼⣿⡘⣯⣾⣿⢿⣹⢯⣟⡿⣿⢿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠈⠻⣿⣿⣿⣿⣿
        I ♥ PYTON
    """
    print(dibujo)   
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