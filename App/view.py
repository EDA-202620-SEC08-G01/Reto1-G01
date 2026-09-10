import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10) 

from App import logic
from tabulate import tabulate


def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
        Carga los datos del archivo en el catálogo.
    """
    if logic.al.size(control["array"]) == 0:
        filename = "chocolate_sale_100_ptc.csv"

        tiempo, total, pedido_menor, pedido_mayor, primeros_5, ultimos_5 = logic.load_data(control, filename)

        print("\nTiempo de carga:", round(tiempo, 3), "[ms]")
        print("Total de pedidos cargados:", total)

        print("\n--- Pedido de menor Amount ---")
        print("Order_ID:", pedido_menor["Order_ID"])
        print("Product:", pedido_menor["Product"])
        print("Country:", pedido_menor["Country"])
        print("Channel:", pedido_menor["Channel"])
        print("Order_Date:", pedido_menor["Order_Date"])
        print("Price_per_Box:", pedido_menor["Price_per_Box"])
        print("Amount:", pedido_menor["Amount"])

        print("\n--- Pedido de mayor Amount ---")
        print("Order_ID:", pedido_mayor["Order_ID"])
        print("Product:", pedido_mayor["Product"])
        print("Country:", pedido_mayor["Country"])
        print("Channel:", pedido_mayor["Channel"])
        print("Order_Date:", pedido_mayor["Order_Date"])
        print("Price_per_Box:", pedido_mayor["Price_per_Box"])
        print("Amount:", pedido_mayor["Amount"])

        print("\n--- Primeros 5 pedidos ---")
        for i in range(logic.al.size(primeros_5)):
            p = logic.al.get_element(primeros_5, i)
            print(p["Order_ID"], p["Product"], p["Country"], p["Channel"], p["Order_Date"], p["Price_per_Box"], p["Amount"])

        print("\n--- Últimos 5 pedidos ---")
        for i in range(logic.al.size(ultimos_5)):
            p = logic.al.get_element(ultimos_5, i)
            print(p["Order_ID"], p["Product"], p["Country"], p["Channel"], p["Order_Date"], p["Price_per_Box"], p["Amount"])

    return control

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    encontrado = None
    total = logic.al.size(control["array"])
    for i in range(total):
        pedido = logic.al.get_element(control["array"], i)
        if pedido["Order_ID"] == id:
            encontrado = pedido
            break

    if encontrado is not None:
        print("Order_ID:", encontrado["Order_ID"])
        print("Product:", encontrado["Product"])
        print("Country:", encontrado["Country"])
        print("Channel:", encontrado["Channel"])
        print("Order_Date:", encontrado["Order_Date"])
        print("Price_per_Box:", encontrado["Price_per_Box"])
        print("Amount:", encontrado["Amount"])
    else:
        print("Unknown")

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    precio_minimo = float(input("Ingrese el precio mínimo del rango: "))
    precio_maximo = float(input("Ingrese el precio máximo del rango: "))

    catalog = load_data(control)
    respuestas = logic.req_2(precio_minimo, precio_maximo, catalog)

    tiempo, cantidad, prom_descuento, prom_marketing, prom_precio, mas_reciente, mayor, menor = respuestas

    print("\n" + "="*50)
    print("RESULTADOS DEL REQUERIMIENTO 2")
    print("="*50)
    print("Tiempo de ejecución:", round(tiempo, 3), "ms")
    print("Cantidad de pedidos en el rango:", cantidad)
    print("Promedio del porcentaje de descuento:", round(prom_descuento, 3), "%")
    print("Promedio del gasto en marketing: $", round(prom_marketing, 3))
    print("Promedio del precio por caja: $", round(prom_precio, 3))

    print("\n--- Pedido más reciente ---")
    if mas_reciente is not None:
        print("Producto:", mas_reciente["Product"])
        print("País:", mas_reciente["Country"])
        print("Canal:", mas_reciente["Channel"])
        print("Fecha:", mas_reciente["Order_Date"])
        print("Precio por caja:", mas_reciente["Price_per_Box"])
        print("Monto:", mas_reciente["Amount"])
    else:
        print("Unknown")

    print("\n--- Pedido de mayor monto ---")
    if mayor is not None:
        print("Producto:", mayor["Product"])
        print("País:", mayor["Country"])
        print("Canal:", mayor["Channel"])
        print("Fecha:", mayor["Order_Date"])
        print("Precio por caja:", mayor["Price_per_Box"])
        print("Monto:", mayor["Amount"])
    else:
        print("Unknown")

    print("\n--- Pedido de menor monto ---")
    if menor is not None:
        print("Producto:", menor["Product"])
        print("País:", menor["Country"])
        print("Canal:", menor["Channel"])
        print("Fecha:", menor["Order_Date"])
        print("Precio por caja:", menor["Price_per_Box"])
        print("Monto:", menor["Amount"])
    else:
        print("Unknown")
    
def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    filtro = input("Ingrese el tipo de filtro (MAYOR o MENOR): ").strip().upper()
    producto = input("Ingrese el nombre del producto: ").strip()
    fecha_inicial = input("Ingrese la fecha inicial (AAAA-MM-DD): ").strip()
    fecha_final = input("Ingrese la fecha final (AAAA-MM-DD): ").strip()
    
    catalog = load_data(control)
    respuestas = logic.req_5(catalog, filtro, producto, fecha_inicial, fecha_final)
    
    print("\n" + "="*50)
    print("RESULTADOS DEL REQUERIMIENTO 5")
    print("="*50)
    print("Tiempo de ejecución:", respuestas[0], "ms")
    print("Filtro aplicado:", filtro)
    print("Cantidad de pedidos encontrados:", respuestas[1])
    print("Precio promedio por caja:", respuestas[2])
    print("Promedio de cajas enviadas:", respuestas[3])
    print("Promedio de inversión en mercadeo:", respuestas[4])
    
    print("\n--- DETALLE DEL PEDIDO RESULTANTE ---")
    print("Precio por caja:", respuestas[5])
    print("Cajas enviadas:", respuestas[6])
    print("Monto total:", respuestas[7])
    print("Canal:", respuestas[8])
    print("Fecha del pedido:", respuestas[9])
    print("Inversión en mercadeo:", respuestas[10])


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
