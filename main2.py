from producto import Articulo
listaArticulos: Articulo = []


def crear_articulo():    
    nombres: str = str(input("Ingrese Nombres: "))    
    codigo: str = str(input("Ingrese Codigo: "))
    precio: float= float(input("Ingrese Precio: "))
    articulo: Articulo = Articulo( nombres, codigo, precio)
    listaArticulos.append(articulo)


def listar_articulos():
    print(" | ", "PRODUCTO", " | ", "CODIGO", " | ", "PRECIO"," | ")
    for art in listaArticulos:
        Articulo.imprimir_cadena(art)


def buscar_articulo():
    codigo: str = str(input("Ingrese CODIGO para buscar: "))
    for art in listaArticulos:
        if art.codigo == codigo:
            Articulo.imprimir_cadena(art)

def editar_articulo():
    codigo: str=str(input("Editar código de artículo: "))
    for Articulo in listaArticulos:
        if Articulo.codigo==codigo:
            Articulo.nombres=str(input("Ingrese un nuevo nombre: "))



def quitar_articulo():
    codigo: str=str(input("Eliminar código de un artículo: "))
    for index,Articulo in enumerate(listaArticulos):
        if Articulo.codigo==codigo:
            listaArticulos.pop(index)
            
          


def main():
    continuar: bool = True
    while continuar:

        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print("       1: PARA AGREGAR producto")
        print("       2: PARA LISTAR producto")        
        print("       3: PARA BUSCAR producto")   
        print("       4: PARA EDITAR producto") 
        print("       3: PARA QUITAR producto")      
        print("       10: PARA SALIR")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                crear_articulo()
            case "2":
                listar_articulos()
            case "3":
                buscar_articulo()
            case "4":
                editar_articulo()
            case "5":
                quitar_articulo()
            case "10":
                continuar = False


if __name__ == '__main__':
    main()
