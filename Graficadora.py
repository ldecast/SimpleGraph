import os
class Graficadora:

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

    def get_lexema(self,lista_tokens,token):
        a = ''
        for i in range(len(lista_tokens)):
            for j in range(len(lista_tokens[i])):
                if token in lista_tokens[i][j]:
                    a = lista_tokens[i][j+1]
        return a
    
    def get_node(self,lista_tokens,token, tipo):
        a = []
        for i in range(len(lista_tokens)):
            for j in range(len(lista_tokens[i])):
                if tipo == "nodo":
                    if token == lista_tokens[i][j]:
                        a.append(lista_tokens[i][1])
                elif tipo == "colorNodo":
                    if token == lista_tokens[i][j]:
                        a.append(lista_tokens[i][1])
        return a
    
    def get_lista(self, lista_tokens, token):
        a = []
        for i in range(len(lista_tokens)):
            for j in range(len(lista_tokens[i])):
                if token == lista_tokens[i][j]:
                    if lista_tokens[i-1][0] == "tk_Num":
                        a.append(int(lista_tokens[i-1][1]))
                    else:
                        a.append(1)
        return a

    def Graficar_lista(self, lista_tokens, name):

        if self.Revisar_Gramatica(lista_tokens) == True:
            titulo = self.get_lexema(lista_tokens,'tk_Nombre')
            forma = self.get_lexema(lista_tokens,'tk_Forma')
            lista_doble = self.get_lexema(lista_tokens,'tk_Boolean')
            etiquetaDefecto = self.get_lexema(lista_tokens,'tk_EtiquetaDefecto')
            colorDefecto = self.get_lexema(lista_tokens,'tk_ColorDefecto')
            nodos = self.get_node(lista_tokens,'tk_EtiquetaNodo',"nodo")
            indices = self.get_lista(lista_tokens,'tk_EtiquetaNodo')
            coloresNodos = self.get_node(lista_tokens,'tk_Color',"colorNodo")

            directorio = str("Grafo [" + name + "]")+'.dot'
            grafo = open(directorio,'w',encoding="utf8")
            grafo.write('digraph D {\n')
            grafo.write("rankdir=\"LR\";\n")
            grafo.write("splines=false;\n")
            grafo.write("bgcolor=\"#abb2b9\";\n")
            grafo.write("label=\"" + titulo.replace("'",'') + "\" fontname=\"Century Gothic\" labelloc=\"b\";\n")
            grafo.write("node[width=\"1.5\" shape = \""+ self.convert_node(forma) +"\" style=filled fontname= \"Century Gothic\" color= \"#283747\"];\n")
            grafo.write("edge[fontname=\"Sans-Serif\"];\n")

            index = 0
            for i in range(len(nodos)):
                label = ""
                color = ""
                if nodos[i] == "#":
                    label = etiquetaDefecto
                else:
                    label = nodos[i]
                
                if coloresNodos[i] == "#":
                    color = colorDefecto
                else:
                    color = coloresNodos[i]
                
                if indices[i] == 1:
                    grafo.write(str(index) + "[label= \""+label.replace("'",'')+"\" fillcolor=\""+self.convert_hexadecimal(color.lower())+"\"];\n")
                    index +=1
                else:
                    numero = 1
                    for j in range(indices[i]):
                        grafo.write(str(index) + "[label= \""+label.replace("'",'')+" "+str(numero)+"\" fillcolor=\""+self.convert_hexadecimal(color.lower())+"\"];\n")
                        numero +=1
                        index +=1

            for i in range(index-1):
                if lista_doble.lower() == "falso":
                    grafo.write(str(i)+"->"+str(i+1)+"\n")
                elif lista_doble.lower() == "verdadero":
                    grafo.write(str(i)+"->"+str(i+1)+"->"+str(i)+"\n")


            grafo.write('}')
            grafo.close()

            pre = directorio[:directorio.index('.dot')]
            os.system('dot -Tpdf \"'+directorio+'\" -o \"'+pre+'.pdf\"')
            os.startfile('\"'+pre+'.pdf\"')
            input("Gráfica generada! Presione Enter para continuar...")
    

    def Revisar_tk(self,lista_tokens):
        for i in range(len(lista_tokens)):
            if lista_tokens[i][0] == "lista":
                print(lista_tokens[i][0],"aceptada")
            if lista_tokens[i][1] == "lista":
                print(lista_tokens[i][0],"aceptada")
        
    def Revisar_Gramatica(self, lista_tokens):
        errores = []
        for i in range(len(lista_tokens)):
            for j in range(len(lista_tokens[i])):
                if 'pr_lista' == lista_tokens[i][j]:
                    if lista_tokens[i][j+1].lower() != "lista":
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
                if 'tk_llaveA' == lista_tokens[i][j]:
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
                        errores.append(lista_tokens[i][j+1])#podria usar numeros y trabajar con error global pasando la lista
        if errores != []:
            print("ERRORES SINTACTICOS ENCONTRADOS")
            print(errores)
            return False
        else:
            return True







                                    
