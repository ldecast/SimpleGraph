# SimpleGraph
### Hecho por: Luis Danniel Ernesto Castellanos Galindo
_Carnet: 201902238_

**Descripción del programa:** la funcionalidad principal de la aplicación SimpleGraphgenerador de gráficas con 
un conjunto de gráficas específicas que nos permita por medio de una sintaxis sencilla obtener gráficas detalladas
y con un aspecto profesional. Esta herramienta está pensada para poder llegar a más usuarios y que puedan generar
gráficas obteniendo un resultado satisfactorio y de muy buena calidad que logre cumplir con los requerimientos de 
la mayoría de los casos.

#### Clases:
- Main.py: menú en consola que permite al usuario seleccionar la opción que desee.
- Automata.py: clase que se encarga de leer el archivo de texto y realizar un análisis léxico y sintáctico
para obtener los datos.
- Reportador.py: genera archivos .csv con la lista de errores y tokens respectivamente que fueron recabados
por el autómata.
- Graficador.py: implementa el uso de Graphviz para realizar los gráficos, árbol sintáctico y demás que el 
usuario desee y genera un archivo.dot
- Web.py: convierte el .dot a SVG y genera una página HTML sencilla con la gráfica resultante.
