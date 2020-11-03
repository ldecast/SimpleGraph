import Reportador
import Graficadora

class AutomataMatriz:

    def aceptar(self, entrada, opcion):
        try:
            file = open(entrada, 'r', encoding= "utf-8-sig") 
            fila = 0
            columna = 0
            aux_col = 0
            aux_estado = 0
            aux_fila = 0
            estado = 0
            tokens = 0
            errores = 0
            token_lista = []
            error_lista = []
            lexema = ""

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
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "pr_matriz"])
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
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
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
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 3                 
                        elif caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Fila"])
                            lexema = lexema[-1]
                            estado = 4
                            aux_col = columna
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 3
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 4:
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito  #tk_coma?¿
                            lexema = lexema[-1]
                            estado = 5
                            aux_col = columna
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 4
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 5:
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 5      
                        elif caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Columna"])
                            lexema = lexema[-1]
                            estado = 6
                            aux_col = columna
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 5
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 6:
                        if caracter == "'":
                            aux_col = columna
                            estado = 7
                        elif caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Columna"])
                            lexema = lexema[-1]
                            estado = 6
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 6
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 7:
                        if caracter == "'":
                            estado = 8
                        else:
                            estado = 7
                    
                    elif estado == 8:
                        if caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Nombre"])
                            lexema = lexema[-1]
                            estado = 9
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 8
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 9:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            aux_col = columna
                            estado = 10
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 9
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 10:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 10
                        elif caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Forma"])
                            lexema = lexema[-1]
                            estado = 11
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 10
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 11:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            aux_col = columna
                            estado = 12
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 11
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 12:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 12
                        elif caracter == ")":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Boolean"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 13
                        else:
                            errores +=1
                            estado = 12
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 13:
                        if caracter == "{":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 14
                        else:
                            errores +=1
                            estado = 13
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 14:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_LlaveA"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 15
                        else:
                            errores +=1
                            estado = 14
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            lexema = lexema[0:len(lexema)-1]
                            continue       
                    
                    elif estado == 15:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 15
                        elif caracter == "(":
                            if 'fila' in  lexema.lower():
                                tokens += 1
                                token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "pr_Fila"])
                                lexema = lexema[-1]
                                aux_col = columna
                                estado = 16
                            elif 'nodo' in  lexema.lower():
                                tokens += 1
                                token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "pr_Nodo"])
                                lexema = lexema[-1]
                                aux_col = columna
                                estado = 16
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 15
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 16:
                        if '(' in lexema:
                            if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                                tokens += 1
                                token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                                lexema = lexema[-1]
                                aux_col = columna
                                estado = 17
                            elif caracter == "'":
                                tokens += 1
                                token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                                lexema = lexema[-1]
                                aux_col = columna
                                estado = 21
                            elif caracter == "#":
                                tokens += 1
                                token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                                lexema = lexema[-1]
                                aux_col = columna
                                estado = 22
                        elif ',' in lexema:
                            if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                                aux_col = columna
                                estado = 17
                            elif caracter == "'":
                                aux_col = columna
                                estado = 21
                            elif caracter == "#":
                                aux_col = columna
                                estado = 22
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 16
                            lexema = lexema[0:len(lexema)-1]
                            continue
                        
                    elif estado == 17:
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            aux_col = columna
                            estado = 17
                        elif caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_X"]) #podria probar poner columna de una
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
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            aux_col = columna
                            estado = 19
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 18
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 19:
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            aux_col = columna
                            estado = 19
                        elif caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Y"]) #podria probar poner columna de una
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
                        if caracter == "'":
                            aux_col = columna
                            estado = 21
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 20
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 21:
                        if caracter == "'":
                            estado = 22
                        else:
                            estado = 21
                    
                    elif estado == 22:
                        if caracter == ",":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Etiqueta"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 16
                        elif caracter == ")":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Etiqueta"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 23
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 22
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 23:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 24
                        elif caracter == "#":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 24
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 23
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 24:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 24
                        elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 24
                        elif caracter == ";":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_Color"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 25
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 24
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 25:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_puntoComa"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 15
                        elif caracter == "}":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_puntoComa"])
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
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#defecto
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_LlaveC"])
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
                        elif caracter == "(":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "pr_defecto"])
                            lexema = lexema[-1]
                            estado = 28
                            aux_col = columna
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 27
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 28:
                        if caracter == "'":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenA"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 29
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 28
                            lexema = lexema[0:len(lexema)-1]
                            continue
                            
                    elif estado == 29:
                        if caracter == "'":
                            estado = 30
                        else:
                            estado = 29
                    
                    elif estado == 30:
                        if caracter == ")":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_EtiquetaDefecto"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 31
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 30
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 31:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_parenC"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 32
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 31
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    elif estado == 32:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 32
                        elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 32
                        elif caracter == ";":
                            tokens += 1
                            token_lista.append([tokens, fila, aux_col, lexema[0:len(lexema)-1], "tk_ColorDefecto"])
                            lexema = lexema[-1]
                            aux_col = columna
                            estado = 33
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,"Desconocido: "+caracter])
                            estado = 32
                            lexema = lexema[0:len(lexema)-1]
                            continue
                    
                    if estado == 33:
                        print("ANÁLISIS LÉXICO COMPLETADO!")
                        tokens += 1
                        token_lista.append([tokens, fila, aux_col, lexema, "tk_puntoComa"])
                        lexema = ''

                else:
                    continue
            
            # if error_lista != [] and opcion == '1':
            #     Reportador.Reportador().error(error_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
            # if token_lista != [] and opcion == '1':
            #     Reportador.Reportador().tokens(token_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
                # Reportador.Reportador().tks(self.Pasar_tokens(token_lista), entrada[entrada.rfind('\\')+1:entrada.index('.')])

            
            if opcion == '2' and estado == 33:
                Graficadora.Graficadora().Graficar_matriz(self.Pasar_tokens(token_lista), entrada[entrada.rfind('\\')+1:entrada.index('.')])
                print(self.Pasar_tokens(token_lista))
            
            file.close()
            return entrada

        except FileNotFoundError:
            return False
    

    def Pasar_tokens(self, lista):
        nueva = []
        for i in range(len(lista)):
            nueva.append([lista[i][4].replace(',',''),lista[i][3].replace(',','')])
        return nueva