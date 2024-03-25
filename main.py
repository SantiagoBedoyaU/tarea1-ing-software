from explorador.explorador import Explorador

try:
    folder_path = input("Ingrese la ruta de la carpeta: ")
    word = input('Ingrese la palabra a buscar: ')
    explorer = Explorador(folder_path, word)
except Exception as e:
    print(e)
