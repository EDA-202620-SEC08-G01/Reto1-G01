import time
import csv
import os
from DataStructures.List import array_list as al
from DataStructures.List import liststructure as lt

csv.field_size_limit(2147483647)

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/GoodReads'

def new_logic(user_data_structure):
    
    global data_structure
    
    if user_data_structure == "1":
        data_structure = al
    else:
        data_structure = lt
        
    pedidos = {"Order_ID": None,
               "Product": None,
               "Country": None,
               "Channel": None,
               "Order_Date": None,
               "Discount_Pct": None,
               "Price_per_Box": None,
               "Marketing_Spend": None,
               "Boxes_Shipped": None,
               "Amount": None}
    
    pedidos["Order_ID"] = lt.new_ilst()
    pedidos["Product"] = lt.new_ilst()
    pedidos["Country"] = lt.new_ilst()
    pedidos["Channel"] = lt.new_ilst()
    pedidos["Order_Date"] = lt.new_ilst()
    pedidos["Discount_Pct"] = lt.new_ilst()
    pedidos["Price_per_Box"] = lt.new_ilst()
    pedidos["Marketing_Spend"] = lt.new_ilst()
    pedidos["Boxes_Shipped"] = lt.new_ilst()
    pedidos["Amount"] = lt.new_ilst()
    
    
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    return pedidos


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    booksfile = data_dir + '/chocolate_sale_100_ptc'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for pedido in input_file:
        add_book(catalog, book)
    return book_size(catalog), author_size(catalog)
    pass


# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, Contry, Channel):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    #pass
    start_time = get_time()
    tamaño=data_structure.size(catalog["Order_ID"])
    N=0
    suma_precio=0
    suma_descuento=0
    suma_marketing=0
    suma_cajas=0
    
    productos = {}
    años = {}

    for i in range(tamaño):
        pais = data_structure.get_element(catalog["Country"], i)
        canal = data_structure.get_element(catalog["Channel"], i)
        
        if pais == Contry and canal == Channel:
            N += 1
            
            precio = float(data_structure.get_element(catalog["Price_per_Box"], i))
            descuento = float(data_structure.get_element(catalog["Discount_Pct"], i))
            marketing = float(data_structure.get_element(catalog["Marketing_Spend"], i))
            cajas = int(data_structure.get_element(catalog["Boxes_Shipped"], i))
            
            suma_precio += precio
            suma_descuento += descuento
            suma_marketing += marketing
            suma_cajas += cajas
            
            prod = data_structure.get_element(catalog["Product"], i)
            productos[prod] = productos.get(prod, 0) + 1
            
            date_val = str(data_structure.get_element(catalog["Order_Date"], i))
            year = date_val[:4]
            años[year] = años.get(year, 0) + 1

    
    
    if N == 0:
        return delta_time(start_time, end_time), 0, 0, 0, 0, 0, "Unknown", "Unknown"

    Prom_precio = suma_precio / N
    Prom_descuento = suma_descuento / N
    Prom_marketing = suma_marketing / N
    Prom_cajas = suma_cajas / N
    
    Moda_producto = max(productos, key=productos.get)
    Moda_año = max(años, key=años.get)
    end_time = get_time()
    pop_time = delta_time(start_time, end_time)

    return pop_time, N, Prom_precio, Prom_cajas, Prom_descuento, Prom_marketing, Moda_año, Moda_producto
    
    
    



def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog, Fecha_inicial, Fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    #pass



# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
