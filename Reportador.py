import csv

class Reportador:

    def error(self, datos, nombre):
        errores = ["No.","Línea","Columna","Descripcion"]
        datos.insert(0,errores)
        ruta = 'ERRORES '+ nombre +'.csv'
        csv_file = open(ruta, 'w', newline='', encoding="utf-8-sig")
        with csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(datos)
        print("Reporte de errores generado!")


    def tokens(self, datos, nombre):
        encabezado = ["No.","Línea","Columna","Lexema","Token"]
        datos.insert(0,encabezado)
        ruta = 'TOKENS '+ nombre +'.csv'
        csv_file = open(ruta, 'w', newline='', encoding="utf-8-sig")
        with csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(datos)    
        print("Reporte de tokens generado!")
