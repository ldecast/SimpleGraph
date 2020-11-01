import Reportador
import Graficadora

class AutomataLista:

    def token(self, lexema):
        a = lexema.lower()
        if 'ruta' in a:
            return 'ruta'
        elif 'estacion' in a:
            return 'estacion'
        elif 'nombre' in a:
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


    def aceptar(self, entrada):
        
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
                        # lexema = lexema[0:len(lexema)-1]
                        estado = -1
                    
                    if estado == -1:
                        if caracter == "/":
                            # lexema = lexema[0:len(lexema)-1]
                            estado = -2
                    
                    if estado == -2:
                        if fila > aux_fila:
                            estado = aux_estado
                        else:
                            lexema = lexema[0:len(lexema)-1]
                    

                    if estado == 0:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 1
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 0
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 1:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            # aux_col = columna
                            estado = 1
                        elif caracter == "(":
                            estado = 2
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 1
                            lexema = lexema.replace(caracter,'')
                            continue
                        
                    elif estado == 2:
                        if caracter == "'":
                            estado = 3
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 2
                            lexema = lexema.replace(caracter,'')
                            continue
                        
                    elif estado == 3:                        
                        if caracter == "'":
                            estado = 4
                        else:
                            estado = 3
                        # else:

                    elif estado == 4:
                        if caracter == ",":
                            estado = 5
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 4
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 5:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 6
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 5
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 6:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 6
                        elif caracter == ",":
                            estado = 7
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 6
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 7:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 8
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 7
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 8:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 8
                        elif caracter == ")":
                            estado = 9
                        else:
                            errores +=1
                            estado = 8
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 9:
                        if caracter == "{":
                            estado = 10
                        else:
                            errores +=1
                            estado = 9
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            lexema = lexema.replace(caracter,'')
                            continue

                    elif estado == 10:
                        if caracter.lower() == "n":
                            estado = 11
                        else:
                            errores +=1
                            estado = 10
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            lexema = lexema.replace(caracter,'')
                            continue            

                    elif estado == 11:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 11
                            
                        elif caracter.lower() == "s":
                            estado = 12
                            #agregar tk_nodos
                            # lexema = ''
                        elif caracter == "(":
                            estado = 13
                            # lexema = ''
                            #agregar tk_nodo
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 11
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 12:
                        if caracter == "(":
                            estado = 13
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 12
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 13:
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 14
                        elif caracter == "'":
                            estado = 16
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 13
                            lexema = lexema.replace(caracter,'')
                            continue

                    elif estado == 14:
                        if ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 14
                        elif caracter == ",":
                            estado = 15
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 14
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 15:
                        if caracter == "'":
                            estado = 16
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 16
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 16:
                        if caracter == "'":
                            estado = 17
                        else:
                            estado = 16

                    elif estado == 17:
                        if caracter == ")":
                            estado = 18
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 17
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 18:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 19
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 18
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 19:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 19
                        elif ord(caracter) >= 48 and ord(caracter) <=57:#es digito
                            estado = 20
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 19
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 20:
                        if caracter == ";":
                            estado = 21
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 20
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 21:
                        if caracter.lower() == "n":
                            estado = 11
                        elif caracter == "}":
                            estado = 22
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 21
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 22:
                        if caracter.lower() == "d":
                            estado = 23
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 22
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 23:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 23
                        elif caracter == "(":
                            estado = 24
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 23
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 24:
                        if caracter == "'":
                            estado = 25
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 24
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 25:
                        if caracter == "'":
                            estado = 26
                        else:
                            estado = 25
                        
                    elif estado == 26:
                        if caracter == ")":
                            estado = 27
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 26
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 27:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 28
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 27
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    elif estado == 28:
                        if ord(caracter) >= 65 and ord(caracter) <= 122:#es letra
                            estado = 28
                        elif caracter == ";":
                            estado = 29
                        else:
                            errores +=1
                            error_lista.append([errores,fila,columna,caracter,"Desconocido"])
                            estado = 28
                            lexema = lexema.replace(caracter,'')
                            continue
                    
                    if estado == 29:
                        print("ARCHIVO ACEPTADO!",lexema)                        
                        # aux_lex.append(lexema.lower())
                        estado = 0
                        # lexema = ''

                else:
                    continue


            # if error_lista != [] and opcion == '1':
            #     Reportador.Reportador().error(error_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
            # if token_lista != [] and opcion == '1':
            #     Reportador.Reportador().tokens(token_lista, entrada[entrada.rfind('\\')+1:entrada.index('.')])
            
            # for j in range(len(aux_lex)):
            #     try:
            #         if '<nombre>' in aux_lex[j] and not '<ruta>' in aux_lex[j] and not '<estacion>' in aux_lex[j]:
            #             if '/estacion' in aux_lex[j-1] or '/ruta' in aux_lex[j-1]:
            #                 nombre = aux_lex[j]
            #         if '<nombre>' in aux_lex[j] and not '<estacion>' in aux_lex[j] and not '<ruta>' in aux_lex[j]:
            #             if '<estacion>' in aux_lex[j-1] or '</estacion>' in aux_lex[j+1]:
            #                 estaciones.append(aux_lex[j])
            #             else:
            #                 rutas.append(aux_lex[j])
            #         if '<estacion>' in aux_lex[j] or '<estado>' in aux_lex[j] or '<color>' in aux_lex[j]:
            #             if not '<ruta>' in aux_lex[j-1] and not '</ruta>' in aux_lex[j+1]:
            #                 estaciones.append(aux_lex[j])
            #         if '<ruta>' in aux_lex[j] or '<peso>' in aux_lex[j] or '<inicio>' in aux_lex[j] or '<fin>' in aux_lex[j]:
            #             if not '<estacion>' in aux_lex[j-1] and not '</estacion>' in aux_lex[j+1]:
            #                 rutas.append(aux_lex[j])
                    
            #     except IndexError:
            #         pass
            
            # try:
            #     if nombre != "":                  
            #         try:
            #             rutas.remove(nombre)
            #             estaciones.remove(nombre)
            #         except ValueError:
            #             estaciones.remove(nombre)
            #             rutas.remove(nombre)
            # except ValueError:
            #     pass

            # if estacion_inicio != None and estacion_final != None:
            #     if opcion == '2' or opcion == '5':
            #         Graficador.Graficador().graficar_ruta(rutas,estaciones,estacion_inicio,estacion_final,opcion)
            #     elif opcion == '3':
            #         Graficador.Graficador().graficar_mapa(rutas,estaciones,estacion_inicio,estacion_final,nombre)
            
            # if opcion == '6':
            #     Graficador.Graficador().mapa_sin_traza(rutas,estaciones,nombre)
            
            file.close()
            return entrada

        except FileNotFoundError:
            return False