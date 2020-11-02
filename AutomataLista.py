import Reportador
import Graficadora

class AutomataLista:

    def token(self, lexema):
        a = lexema.lower()
        if 'lista' == a:
            return 'lista'
        elif 'nodo' == a:
            return 'nodo'
        elif 'nodos' in a:
            return 'nombre'
        elif 'peso' in a:
            return 'peso'
        elif 'inicio' in a:
            return 'inicio'
        elif 'fin' in a:
            return 'fin'
        elif 'estado' in a:
            return 'estado'
        elif 'color' in a:
            return 'color'

    
    def get_lexema(self, lexema):
        if lexema.count('>') > 1:
            a = [idx for idx, x in enumerate(lexema) if x=='<']
            b = [idx for idx, x in enumerate(lexema) if x=='>']
            c = lexema[a.pop()+1:b.pop()]
            return c
        elif lexema.count('>') == 1:
            a = lexema[lexema.index('<')+1:lexema.index('>')]
            return a


    def aceptar(self, entrada, opcion):
        
        try:
            file = open(entrada, 'r', encoding= "utf-8-sig") 
            aux_lex = []
            fila = 0
            columna = 0
            aux_col = 0
            aux_estado = 0
            aux_fila = 0
            lexema = ""
            estado = 0
            tokens = 0
            token_lista = []
            errores = 0
            error_lista = []

            for linea in file.readlines():
                fila = fila + 1
                columna = 0
                for caracter in linea:
                    columna = columna + 1
                    if caracter == "\n":
                        continue
                    elif caracter == "\t":
                        continue
                    elif caracter == " ":
                        continue


                    lexema = lexema + caracter

                    #Comentarios
                    if caracter == "/" and estado > -1:
                        aux_estado = estado
                        aux_fila = fila
                        estado = -1
                    if estado == -1:
                        if caracter == "/":
                            estado = -2
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Falta otro '/' para tomarlo como comentario"])
                            estado = 0
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    if estado == -2:
                        if fila > aux_fila:
                            estado = aux_estado
                        else:
                            lexema = lexema[0:len(lexema)-1]
                    

                    if estado == 0:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 1
                            aux_col = columna
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 0
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 1:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 1
                        elif caracter == "(":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "pr_lista"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 2
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 1
                            lexema = lexema[0:len(lexema)-1]
                            continue
                        
                    elif estado == 2:
                        if caracter == "'":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                            lexema = lexema[-1]
                            estado = 3
                            aux_col = columna
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 2
                            lexema = lexema[0:len(lexema)-1]
                            continue
                        
                    elif estado == 3:                        
                        if caracter == "'":
                            estado = 4
                        else:
                            estado = 3

                    elif estado == 4:
                        if caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Nombre"])
                            lexema = lexema[-1]
                            estado = 5
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 4
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 5:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            aux_col = columna
                            estado = 6
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 5
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 6:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 6
                        elif caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Forma"])
                            lexema = lexema[-1]
                            estado = 7
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 6
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 7:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            aux_col = columna
                            estado = 8
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 7
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 8:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 8
                        elif caracter == ")":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Boolean"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 9
                        else:
                            errores +=1
                            estado = 8
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 9:
                        if caracter == "{":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 10
                        else:
                            errores +=1
                            estado = 9
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            lexema = lexema[0:len(lexema)-1]
                            continue

                    elif estado == 10:
                        if caracter.lower() == "n":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_LlaveA"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 11
                        else:
                            errores +=1
                            estado = 10
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            lexema = lexema[0:len(lexema)-1]
                            continue            

                    elif estado == 11:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 11
                            
                        elif caracter == "(":
                            if lexema[len(lexema)-2].lower() == 'o':
                                tokens += 1
                                token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "pr_Nodo"])
                                lexema = lexema[-1]
                                aux_col = columna
                                estado = 13
                            elif lexema[len(lexema)-2].lower() == 's':
                                tokens += 1
                                token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "pr_Nodos"])
                                lexema = lexema[-1]
                                aux_col = columna
                                estado = 13
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 11
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 13:
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 14
                        elif caracter == "'":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 16
                        elif caracter == "#":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 17
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 13
                            lexema = lexema[0:len(lexema)-1]
                            continue

                    elif estado == 14:
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 14
                        elif caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Num"]) #podria probar poner columna de una
                            lexema = lexema[-1]
                            estado = 15
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 14
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 15:
                        if caracter == "'":
                            aux_col = columna
                            estado = 16
                        elif caracter == "#":
                            aux_col = columna
                            estado = 17
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 16
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 16:
                        if caracter == "'":
                            estado = 17
                        else:
                            estado = 16

                    elif estado == 17:
                        if caracter == ")":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Etiqueta"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 18
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 17
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 18:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 19
                        elif caracter == "#":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 19
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 18
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 19:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 19
                        elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 19
                        elif caracter == ";":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Color"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 20
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 19
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 20:
                        if caracter.lower() == "n":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_puntoComa"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 11
                        elif caracter == "}":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_puntoComa"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 21
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 20
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 21:
                        if caracter.lower() == "d":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_LlaveC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 22
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 21
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 22:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 22
                        elif caracter == "(":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "pr_defecto"])
                            lexema = lexema[-1]
                            estado = 23
                            aux_col = columna
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 22
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 23:
                        if caracter == "'":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 24
                        elif caracter == "#":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 25
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 23
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 24:
                        if caracter == "'":
                            estado = 25
                        else:
                            estado = 24
                        
                    elif estado == 25:
                        if caracter == ")":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Etiqueta"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 26
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 25
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 26:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 27
                        elif caracter == "#":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 27
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 26
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 27:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 27
                        elif caracter == ";":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Color"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 28
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 27
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    if estado == 28:
                        print("ARCHIVO CUMPLE PATRONES LÉXICOS!")
                        tokens += 1
                        token_lista.append([tokens, fila, aux_col, lexema, "tk_puntoComa"])
                        
                        if error_lista != [] and opcion == '1':
                            Reportador.Reportador().error(error_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
                        if token_lista != [] and opcion == '1':
                            Reportador.Reportador().tokens(token_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
                        file.close()
                        return entrada

                else:
                    continue
            
            # print(token_lista)

            # if error_lista != [] and opcion == '1':
            #     Reportador.Reportador().error(error_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
            # if token_lista != [] and opcion == '1':
            #     Reportador.Reportador().tokens(token_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
            
            # if opcion == '2' or opcion == '4':
            #     Graficador.Graficador().mapa_sin_traza(rutas,estaciones,nombre)
            
            # file.close()
            # return entrada

        except FileNotFoundError:
            return False