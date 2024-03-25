import os
from .archivo import Archivo
from .extension import Extension


class Explorador:
    """
    Se encarga leer los archivos que contiene una carpeta
    """
    def __init__(self, path: str, word: str) -> None:
        self.path = path
        self.word = word
        self.files: list[Archivo] = []
        self.extraer_archivos()
        self.sumatoria_palabra()

    def validar_ext(self, file_name: str) -> bool:
        """
        Valida que la extension del archivo este soportada
        """
        ext = file_name.split(".")[-1]
        return ext in [ext.value for ext in Extension]

    def extraer_archivos(self):
        """
        Extrae los archivos de una capeta, y los agrega a una lista de archivos
        """
        try:
            dir_list = os.listdir(self.path)
        except FileNotFoundError:
            raise ValueError("No se encontro la carpeta para leer")

        for file_name in dir_list:
            if self.validar_ext(file_name):
                archivo = Archivo(f"{self.path}/{file_name}")
                self.files.append(archivo)

    def sumatoria_palabra(self):
        if len(self.files) == 0:
            raise ValueError("No se encontraron archivos de texto para leer")

        counter = 0
        for archivo in self.files:
            n_word = archivo.contar_palabra(self.word)
            print(f"{archivo.file_name}: {n_word}")
            counter += n_word
        print(f"Total: {counter}")
