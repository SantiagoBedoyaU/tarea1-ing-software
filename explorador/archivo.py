from .extension import Extension


class Archivo:
    """
    Contiene la informacion de un archivo como su ruta, nombre, extension
    y contenido
    """

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.file_name = file_path.split("/")[-1]
        self.ext = Extension(self.file_name.split(".")[-1])
        self.content = None
        self.leer_archivo()
        self.limpiar()

    def leer_archivo(self):
        with open(self.file_path) as file:
            self.content = file.read()

    def limpiar(self):
        """
        Limpia el contenido de caracteres de simbolos como parentesis, comas
        y saltos de linea
        """
        symbols = ["(", ")", ",", "\n"]
        for symbol in symbols:
            self.content = self.content.replace(symbol, "")

    def contar_palabra(self, word: str) -> int:
        words = self.content.split(" ")
        return words.count(word)
