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
     #TODO: Imprimir el resultado del requerimiento 3
    print("\n" + "="*40)
    print("        REQUERIMIENTO 3")
    print("="*40)
    
    # 1. Pedir parámetros al usuario
    pais = input("Ingrese el País a buscar (ej. United States): ")
    canal = input("Ingrese el Canal a buscar (ej. Online): ")
    
    # 2. Llamar a la lógica correctamente
    resultados = logic.req_3(control, pais, canal)
    
    # 3. Desempacar y mostrar resultados
    if resultados:
        # Extraemos en el mismo orden exacto del return de logic.req_3
        tiempo, n, p_precio, p_desc, p_mkt, p_cajas, moda_prod, moda_anio = resultados
        
        print("\n--- RESULTADOS ---")
        print(f"Tiempo de ejecución: {tiempo:.4f} ms")
        
        if n == 0:
            print("\nNo se encontraron pedidos para la combinación de país y canal ingresada.")
        else:
            print(f"Total de pedidos (N): {n}")
            print(f"Promedio de Price_per_Box:      ${p_precio:.2f}")
            print(f"Promedio de Discount_Pct:       {p_desc:.2f}%")
            print(f"Promedio de Marketing_Spend:    ${p_mkt:.2f}")
            print(f"Promedio de Boxes_Shipped:      {p_cajas:.2f} cajas")
            print(f"Producto más frecuente:         {moda_prod}")
            print(f"Año con más pedidos:            {moda_anio}")
    else:
        print("\nError: No se obtuvieron resultados del controlador.")
    print("="*40)


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
    Función que imprime la solución del Requerimiento 6 en consola    """
    print("\n" + "="*40)
    print("        REQUERIMIENTO 6")
    print("="*40)
    
    # 1. Pedir parámetros al usuario
    start_date = input("Ingrese la Fecha de Inicio (YYYY-MM-DD): ")
    end_date = input("Ingrese la Fecha de Fin (YYYY-MM-DD): ")
    
    # 2. Llamar a la lógica correctamente
    resultados = logic.req_6(control, start_date, end_date)
    
    # 3. Desempacar y mostrar resultados
    if resultados:
        # Extraemos en el orden del return de logic.req_6
        tiempo, n, canal_usado, canal_recaudador, info_canales = resultados
        
        print("\n--- RESULTADOS GLOBALES ---")
        print(f"Tiempo de ejecución: {tiempo:.4f} ms")
        
        if n == 0:
            print("\nNo se encontraron pedidos dentro de ese rango de fechas.")
        else:
            print(f"Número total de pedidos en el filtro: {n}")
            
            # Reporte del canal más usado
            print("\nCANAL MÁS USADO:")
            print(f" - Nombre: {canal_usado['Nombre']}")
            print(f" - Total de pedidos: {canal_usado['Total_Pedidos']}")
            print(f" - Total de recaudo: ${canal_usado['Total_Recaudo']:,.2f}")
            
            # Reporte del canal que más recauda
            print("\nCANAL CON MAYOR RECAUDACIÓN:")
            print(f" - Nombre: {canal_recaudador['Nombre']}")
            print(f" - Total de pedidos: {canal_recaudador['Total_Pedidos']}")
            print(f" - Total de recaudo: ${canal_recaudador['Total_Recaudo']:,.2f}")
            
            # Reporte detallado por cada canal
            print("\n--- DETALLE POR CADA CANAL EN EL RANGO ---")
            for canal, datos in info_canales.items():
                print(f"\n> Canal: {canal}")
                print(f"  Promedio Precio por Caja: ${datos['Precio_promedio']:,.2f}")
                print(f"  Promedio Inversión Mercadeo: ${datos['Promedio_marketing']:,.2f}")
                
                # Pedido más costoso
                p_max = datos['Pedido_mas_costoso']
                print("  Pedido MÁS COSTOSO (por Amount):")
                print(f"    Order_ID: {p_max['Order_ID']} | Product: {p_max['Product']} | Country: {p_max['Country']}")
                print(f"    Order_Date: {p_max['Order_Date']} | Boxes_Shipped: {p_max['Boxes_Shipped']} | Amount: ${p_max['Amount']:,.2f}")
                
                # Pedido más barato
                p_min = datos['Pedido_mas_barato']
                print("  Pedido MÁS BARATO (por Amount):")
                print(f"    Order_ID: {p_min['Order_ID']} | Product: {p_min['Product']} | Country: {p_min['Country']}")
                print(f"    Order_Date: {p_min['Order_Date']} | Boxes_Shipped: {p_min['Boxes_Shipped']} | Amount: ${p_min['Amount']:,.2f}")

    else:
        print("\nError: No se obtuvieron resultados del controlador.")
    print("="*40)

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
