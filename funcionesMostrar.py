import funciones

def bannerBienvenida():
    funciones.clear()
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

def menu():
    funciones.clear()
    print("________________________________")
    print("[1]: Mostrar dicionario completo")
    print("[2]: Añadir al dicionario")
    print("[3]: Modificar el dicionario")
    print("[4]: Eliminar el dicionario")
    print("[0]: Exit->")
    print("________________________________")

# case 1:
def opcioMostrarDicionario():
    funciones.clear()
    print("--------------------------------")
    print("Has seleccionado mostrar: ")
    print("Dicionario completo")
    print("--------------------------------")
    print(" ")

# case 2:
def opcioAnadir():
    funciones.clear()
    print("--------------------------------")
    print("Has seleccionado añadir: ")
    print("Dicionario completo...")
    print("--------------------------------")
    print(" ")
    
# case 3:
def opcioMostrarModificarDic():
    funciones.clear()
    print("--------------------------------")
    print("Has seleccionado modificar: ")
    print("Dicionario completo...")
    print("--------------------------------")
    print(" ")    
    
# case 4:    
def opcioMostrarEliminarKey():
    funciones.clear()
    print("--------------------------------")
    print("Has seleccionado eliminar: ")
    print("Eliminar el Key...")
    print("--------------------------------")
    print(" ")

def opcioMostrarEliminarReff():
    funciones.clear()
    print("--------------------------------")
    print("Has seleccionado eliminar: ")
    print("Eliminar la referencia...")
    print("--------------------------------")
    print(" ")
    
def menuModificarDic():
    print("________________________________")
    print("[1]: Modificar Key")
    print("[2]: Modificar palabra")
    print("[3]: Modificar definicion")
    print("[0]: Exit->")
    print("________________________________")


def menuEliminarDic():
    print("________________________________")
    print("[1]: Eliminar Key")
    print("[2]: Eliminar palabra")
    print("[0]: Exit->")
    print("________________________________")

def panelModReferencia():
    print("--------------------------------")
    print("-- Modificador de referencia  --")
    print("--------------------------------")
    print("")
    
def panelCrearReferencia():
    print("--------------------------------")
    print("-- - Creador de referencia  - --")
    print("--------------------------------")
    print("")
    
def panelCrearDefinicion():
    print("--------------------------------")
    print("-- - Creador de definicion  - --")
    print("--------------------------------")
    print("")
    
def panelCrearKeyNombre():
    print("--------------------------------")
    print("-- -- -- Creador de KEY -- -- --")
    print("--------------------------------")
    print("")

