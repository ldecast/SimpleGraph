class Gramatica:

    formas = [
                "circulo",
                "rectangulo",
                "triangulo",
                "punto",
                "hexagono",
                "diamante"
    ]

    booleano = [
        "verdadero",
        "falso"
    ]

    colores = [
        "#",
        "azul","azul2","azul3",
        "rojo","rojo2","rojo3",
        "amarillo","amarillo2","amarillo3",
        "anaranjado","anaranjado2","anaranjado3",
        "cafe","cafe2","cafe3",
        "gris","gris2","gris3",
        "morado","morado2","morado3",
        "verde","verde2","verde3",
        "blanco"
    ]

    def convert_node(self,forma):
        if forma == "circulo":
            return "circle"
        elif forma == "rectangulo":
            return "rect"
        elif forma == "triangulo":
            return "triangle"
        elif forma == "punto":
            return "point"
        elif forma == "hexagono":
            return "hexagon"
        elif forma == "diamante":
            return "diamond"

    def convert_hexadecimal(self,color):
        if color == "azul":
            return "#aed6f1"
        elif color == "azul2":
            return "#2980b9"
        elif color == "azul2":
            return "#2980b9"
        elif color == "azul3":
            return "#154360"
        elif color == "rojo":
            return "#e6b0aa"
        elif color == "rojo2":
            return "#cb4335"
        elif color == "rojo3":
            return "#641e16"
        elif color == "amarillo":
            return "#fcf3cf"
        elif color == "amarillo2":
            return "#f1c40f"
        elif color == "amarillo3":
            return "#b7950b"
        elif color == "anaranjado":
            return "#edbb99"
        elif color == "anaranjado2":
            return "#e67e22"
        elif color == "anaranjado3":
            return "#873600"
        elif color == "cafe":
            return "#ca6f1e"
        elif color == "cafe2":
            return "#d35400"
        elif color == "cafe3":
            return "#873600"
        elif color == "gris":
            return "#ccd1d1"
        elif color == "gris2":
            return "#839192"
        elif color == "gris3":
            return "#424949"
        elif color == "morado":
            return "#d7bde2"
        elif color == "morado2":
            return "#8e44ad"
        elif color == "morado3":
            return "#4a235a"
        elif color == "verde":
            return "#a9dfbf"
        elif color == "verde2":
            return "#229954"
        elif color == "verde3":
            return "#0b5345"
        elif color == "blanco":
            return "#ffffff"
        elif color == "#":
            return ""
        else:
            return ""
        
    
    def Revisar_Gramatica(self, lista_tokens):
        errores = []
        for i in range(len(lista_tokens)):
            for j in range(len(lista_tokens[i])):
                if 'pr_lista' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != "lista":
                        errores.append(lista_tokens[i][j+1])
                if 'pr_matriz' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != "matriz":
                        errores.append(lista_tokens[i][j+1])
                if 'pr_Fila' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != "fila":
                        errores.append(lista_tokens[i][j+1])
                if 'tk_parenA' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != "(":
                        errores.append(lista_tokens[i][j+1])
                if 'tk_Forma' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() not in self.formas:
                        errores.append(lista_tokens[i][j+1])
                if 'tk_Boolean' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() not in self.booleano:
                        errores.append(lista_tokens[i][j+1])
                if 'tk_parenC' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != ")":
                        errores.append(lista_tokens[i][j+1])
                if 'tk_LlaveA' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != "{":
                        errores.append(lista_tokens[i][j+1])
                if 'pr_Nodo' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != "nodo":
                        errores.append(lista_tokens[i][j+1])
                if 'pr_Nodos' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != "nodos":
                        errores.append(lista_tokens[i][j+1])
                if 'tk_Color' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() not in self.colores:
                        errores.append(lista_tokens[i][j+1])
                if 'tk_ColorDefecto' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() not in self.colores:
                        errores.append(lista_tokens[i][j+1])
                if 'tk_puntoComa' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != ";":
                        errores.append(lista_tokens[i][j+1])
                if 'tk_puntoComa' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != ";":
                        errores.append(lista_tokens[i][j+1])
        if errores != []:
            print("ERRORES SINTACTICOS ENCONTRADOS")
            print(errores)
            return False
        else:
            return True