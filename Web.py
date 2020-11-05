import os
import webbrowser

class Web:

    def lista_html(self, grafo):

        pre = grafo[:grafo.index('.dot')]
        os.system('dot -Tsvg \"'+grafo+'\" -o \"'+pre+'.svg\"')

        f  = open(pre+'.html','w')
        contenido = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <style> body{ background-color: #7f8c8d; } .foot{ position: absolute; right:40px; bottom:10px; } </style>
    <title>LFP P2</title>
  </head>
  <body>
  <div class="container-fluid pt-3 pb-1 text-center bg-warning">
    <h1 class="display-3"> Lenguajes formales y de programacion </h1>
    <h1 class="display-4 my-4"><b>Proyecto #2</b></h1>
    </div>

        <div class="row text-center">
            <div class="col-12 text-center">
                <h2 class="pt-5 pb-4 " >Lista generada:</h2>
                <img class="border rounded" src=\""""+ pre +""".svg">
            </div>
        </div>
    
    <div class = "foot"> <p> Luis Danniel Ernesto Castellanos Galindo - 201902238 </p> </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>"""

        f.write(contenido)
        f.close()
        webbrowser.open_new_tab(pre+'.html')
        
        input("Gráfica generada! Presione Enter para continuar...")




    def matriz_html(self, grafo):
        
        pre = grafo[:grafo.index('.dot')]
        os.system('dot -Tsvg \"'+grafo+'\" -o \"'+pre+'.svg\"')

        f  = open(pre+'.html','w')
        contenido = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <style> body{ background-color: #7f8c8d; } .foot{ position: absolute; right:40px; bottom:10px; } </style>
    <title>LFP P2</title>
  </head>
  <body>
  <div class="container-fluid pt-3 pb-1 text-center bg-warning">
    <h1 class="display-3"> Lenguajes formales y de programacion </h1>
    <h1 class="display-4 my-4"><b>Proyecto #2</b></h1>
    </div>

        <div class="row text-center">
            <div class="col-12 text-center">
                <h2 class="pt-5 pb-4 " >Lista generada:</h2>
                <img class="border rounded" src=\""""+ pre +""".svg">
            </div>
        </div>
    
    <div class = "foot"> <p> Luis Danniel Ernesto Castellanos Galindo - 201902238 </p> </div>
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
  </body>
</html>"""

        f.write(contenido)
        f.close()
        webbrowser.open_new_tab(pre+'.html')
        
        input("Matriz generada! Presione Enter para continuar...")
