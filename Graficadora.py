import os
import Gramatica
import Web
class Graficadora:

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
                elif tipo == "filaNodo":
                    if token == lista_tokens[i][j]:
                        if lista_tokens[i-4][0] != "pr_Nodo":
                            a.append(lista_tokens[i][1])
                elif tipo == "filaColor":
                    if token == lista_tokens[i][j]:
                        if lista_tokens[i-6][0] != "pr_Nodo":
                            a.append(lista_tokens[i][1])
                elif tipo == "NodoS":
                    if token == lista_tokens[i][j]:
                        if lista_tokens[i-1][0] == "tk_Y":
                            a.append(lista_tokens[i][1])
                elif tipo == "ColorNodoS":
                    if token == lista_tokens[i][j]:
                        if lista_tokens[i-3][0] == "tk_Y":
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

        if Gramatica.Gramatica().Revisar_Gramatica(lista_tokens) == True:
            titulo = self.get_lexema(lista_tokens,'tk_Nombre')
            forma = self.get_lexema(lista_tokens,'tk_Forma')
            lista_doble = self.get_lexema(lista_tokens,'tk_Boolean')
            etiquetaDefecto = self.get_lexema(lista_tokens,'tk_EtiquetaDefecto')
            colorDefecto = self.get_lexema(lista_tokens,'tk_ColorDefecto')
            nodos = self.get_node(lista_tokens,'tk_EtiquetaNodo',"nodo")
            indices = self.get_lista(lista_tokens,'tk_EtiquetaNodo')
            coloresNodos = self.get_node(lista_tokens,'tk_Color',"colorNodo")

            directorio = str(name)+'.dot'
            grafo = open(directorio,'w',encoding="utf8")
            grafo.write('digraph D {\n')
            grafo.write("rankdir=\"LR\";\n")
            grafo.write("splines=false;\n")
            grafo.write("bgcolor=\"#abb2b9\";\n")
            grafo.write("label=\"" + titulo.replace("'",'') + "\" fontname=\"Century Gothic\" labelloc=\"b\";\n")
            grafo.write("node[width=\"1.5\" shape = \""+ Gramatica.Gramatica().convert_node(forma) +"\" style=filled fontname= \"Century Gothic\" color= \"#283747\"];\n")
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
                    grafo.write(str(index) + "[label= \""+label.replace("'",'')+"\" fillcolor=\""+Gramatica.Gramatica().convert_hexadecimal(color.lower())+"\"];\n")
                    index +=1
                else:
                    numero = 1
                    for j in range(indices[i]):
                        grafo.write(str(index) + "[label= \""+label.replace("'",'')+" "+str(numero)+"\" fillcolor=\""+Gramatica.Gramatica().convert_hexadecimal(color.lower())+"\"];\n")
                        numero +=1
                        index +=1

            for i in range(index-1):
                if lista_doble.lower() == "falso":
                    grafo.write(str(i)+"->"+str(i+1)+"\n")
                elif lista_doble.lower() == "verdadero":
                    grafo.write(str(i)+"->"+str(i+1)+"->"+str(i)+"\n")

            grafo.write('}')
            grafo.close()

            Web.Web().lista_html(directorio)
    


    def Graficar_matriz(self, lista_tokens, name):

        if Gramatica.Gramatica().Revisar_Gramatica(lista_tokens) == True:
            titulo = self.get_lexema(lista_tokens,'tk_Nombre')
            forma = self.get_lexema(lista_tokens,'tk_Forma')
            doble_enlace = self.get_lexema(lista_tokens,'tk_Boolean')
            etiquetaDefecto = self.get_lexema(lista_tokens,'tk_EtiquetaDefecto')
            colorDefecto = self.get_lexema(lista_tokens,'tk_ColorDefecto')
            nodosFila = self.get_node(lista_tokens,'tk_Etiqueta',"filaNodo")
            coloresFila = self.get_node(lista_tokens,'tk_Color',"filaColor")
            nodos = self.get_node(lista_tokens,'tk_Etiqueta',"NodoS")
            colorNodo = self.get_node(lista_tokens,'tk_Color',"ColorNodoS")
            
            filas = int(self.get_lexema(lista_tokens,'tk_Fila'))
            columnas = int(self.get_lexema(lista_tokens,'tk_Columna'))
            dimension = filas * columnas

            directorio = str(name)+'.dot'
            grafo = open(directorio,'w',encoding="utf8")
            grafo.write('digraph D {\n')
            grafo.write("rankdir=\"LR\";\n")
            grafo.write("splines=false;\n")
            grafo.write("bgcolor=\"#abb2b9\";\n")
            grafo.write("label=\"" + titulo.replace("'",'') + "\" fontname=\"Century Gothic\" labelloc=\"b\";\n")
            grafo.write("node[width=\"1.8\" shape = \""+ Gramatica.Gramatica().convert_node(forma) +"\" style=filled fontname= \"Century Gothic\" color= \"#283747\"];\n")
            grafo.write("edge[fontname=\"Sans-Serif\"];\n")

            index = 0
            for i in range(dimension):
                grafo.write(str(i) + "[label= \""+etiquetaDefecto.replace("'",'')+"\" fillcolor=\""+Gramatica.Gramatica().convert_hexadecimal(colorDefecto.lower())+"\"];\n")

            if doble_enlace.lower() == "falso":
                aux = 0
                for f in range(filas):
                    for i in range(columnas-1):
                        grafo.write(str(aux)+"->"+str(aux+1)+"\n")
                        aux+=1
                    aux+=1

                aux2 = 0
                for f in range(filas-1):
                    for i in range(columnas-1):
                        grafo.write(str(aux2)+"->"+str(aux2+columnas)+ " {rank=same;"+str(aux2)+";"+str(aux2+columnas)+";"+"}\n")
                        aux2+=1
                    aux2+=1
                
                #experimental
                aux2 = 0
                for f in range(filas-1):
                    for i in range(columnas-1):
                        if aux2 >= dimension:
                            break
                        else:
                            grafo.write(str(aux2+columnas-1)+"->"+str(aux2+columnas-1+columnas)+ " {rank=same;"+str(aux2+columnas-1)+";"+str(aux2+columnas-1+columnas)+";"+"}\n")
                            aux2+=columnas
                    aux2+=columnas
            
            elif doble_enlace.lower() == "verdadero":
                aux = 0
                for f in range(filas):
                    for i in range(columnas-1):
                        grafo.write(str(aux)+"->"+str(aux+1)+"->"+str(aux)+"\n")
                        aux+=1
                    aux+=1

                aux2 = 0
                for f in range(filas-1):
                    for i in range(columnas-1):
                        grafo.write(str(aux2)+"->"+str(aux2+columnas)+"->"+str(aux2)+ " {rank=same;"+str(aux2)+";"+str(aux2+columnas)+";"+"}\n")
                        aux2+=1
                    aux2+=1
                
                #experimental
                aux2 = 0
                for f in range(filas-1):
                    for i in range(columnas-1):
                        if aux2 >= dimension:
                            break
                        else:
                            grafo.write(str(aux2+columnas-1)+"->"+str(aux2+columnas-1+columnas)+"->"+str(aux2+columnas-1)+ " {rank=same;"+str(aux2+columnas-1)+";"+str(aux2+columnas-1+columnas)+";"+"}\n")
                            aux2+=columnas
                    aux2+=columnas

            
            index2 = 1
            nodo = ''
            colorFila = ''
            for j in range (len(nodosFila)):
                if index2 > columnas:
                    index2 = 0
                    coloresFila.pop(0)
                if nodosFila[j] == "#":
                    nodo = etiquetaDefecto.replace("'",'')
                else:
                    nodo = nodosFila[j].replace("'",'')

                if coloresFila[0] == "#":
                    colorFila = Gramatica.Gramatica().convert_hexadecimal(colorDefecto)
                else:
                    colorFila = Gramatica.Gramatica().convert_hexadecimal(coloresFila[0])

                grafo.write(str(index)+"[label=\""+ nodo +"\" fillcolor=\""+ colorFila +"\"];\n")
                index += 1
                index2 += 1

            index3 = 1
            nodo = ''
            colorN = ''
            for j in range (len(nodos)):
                if index3 > 1:
                    index3 = 0
                    colorNodo.pop(0)
                if nodos[j] == "#":
                    nodo = etiquetaDefecto.replace("'",'')
                else:
                    nodo = nodos[j].replace("'",'')

                if colorNodo[0] == "#":
                    colorN = Gramatica.Gramatica().convert_hexadecimal(colorDefecto)
                else:
                    colorN = Gramatica.Gramatica().convert_hexadecimal(colorNodo[0])

                grafo.write(str(index)+"[label=\""+ nodo +"\" fillcolor=\""+ colorN +"\"];\n")
                index += 1
                index3 += 1

            grafo.write('}')
            grafo.close()
            
            Web.Web().matriz_html(directorio)
            
    