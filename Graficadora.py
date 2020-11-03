import os
import Gramatica
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

            directorio = str("Grafo [" + name + "]")+'.dot'
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

            pre = directorio[:directorio.index('.dot')]
            os.system('dot -Tpdf \"'+directorio+'\" -o \"'+pre+'.pdf\"')
            os.startfile('\"'+pre+'.pdf\"')
            input("Gráfica generada! Presione Enter para continuar...")
    

    def Graficar_matriz(self, lista_tokens, name):

        if Gramatica.Gramatica().Revisar_Gramatica(lista_tokens) == True:
            titulo = self.get_lexema(lista_tokens,'tk_Nombre')
            forma = self.get_lexema(lista_tokens,'tk_Forma')
            doble_enlace = self.get_lexema(lista_tokens,'tk_Boolean')
            etiquetaDefecto = self.get_lexema(lista_tokens,'tk_EtiquetaDefecto')
            colorDefecto = self.get_lexema(lista_tokens,'tk_ColorDefecto')
            # nodos = self.get_node(lista_tokens,'tk_EtiquetaNodo',"nodo")
            # indices = self.get_lista(lista_tokens,'tk_EtiquetaNodo')
            # coloresNodos = self.get_node(lista_tokens,'tk_Color',"colorNodo")
            
            filas = int(self.get_lexema(lista_tokens,'tk_Fila'))
            columnas = int(self.get_lexema(lista_tokens,'tk_Columna'))
            dimension = filas * columnas


            directorio = str("Grafo [" + name + "]")+'.dot'
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
                grafo.write(str(index) + "[label= \""+etiquetaDefecto.replace("'",'')+"\" fillcolor=\""+Gramatica.Gramatica().convert_hexadecimal(colorDefecto.lower())+"\"];\n")
                index +=1

            # index = 0
            # for i in range(len(nodos)):
            #     label = ""
            #     color = ""
            #     if nodos[i] == "#":
            #         label = etiquetaDefecto
            #     else:
            #         label = nodos[i]
                
            #     if coloresNodos[i] == "#":
            #         color = colorDefecto
            #     else:
            #         color = coloresNodos[i]
                
            #     if indices[i] == 1:
            #         grafo.write(str(index) + "[label= \""+label.replace("'",'')+"\" fillcolor=\""+Gramatica.Gramatica().convert_hexadecimal(color.lower())+"\"];\n")
            #         index +=1
            #     else:
            #         numero = 1
            #         for j in range(indices[i]):
            #             grafo.write(str(index) + "[label= \""+label.replace("'",'')+" "+str(numero)+"\" fillcolor=\""+Gramatica.Gramatica().convert_hexadecimal(color.lower())+"\"];\n")
            #             numero +=1
            #             index +=1

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


            grafo.write('}')
            grafo.close()

            pre = directorio[:directorio.index('.dot')]
            os.system('dot -Tpdf \"'+directorio+'\" -o \"'+pre+'.pdf\"')
            os.startfile('\"'+pre+'.pdf\"')
            input("Gráfica generada! Presione Enter para continuar...")
    

