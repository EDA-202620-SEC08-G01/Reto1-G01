import time

import csv
csv.field_size_limit(2147483647)

import os

from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

csv.field_size_limit(2147483647)

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/GoodReads'

def new_logic():
    
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    catalog = {"array": al.new_list(), "single_linked": sl.new_list()}
    return catalog


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


def req_1(catalog, nom_producto):
    """
    Retorna el resultado del requerimiento 1
    """
    Tiempo_inicial = get_time()
    
    n = al.size(catalog["Product"])
    
    contador = 0
    sum_price = 0; min_price = None; max_price = None
    sum_discount = 0; min_discount = None; max_discount = None
    sum_boxes = 0; min_boxes = None; max_boxes = None
    sum_marketing = 0; min_marketing = None; max_marketing = None
    conteo_años = {}
    max_amount = None
    ubicacion_max_amount = None
    less_amount = None
    ubicacion_less_amount = None
    
    for i in range (1, n+1): #Del primer elemento hasta el último, sabiendo que el for excluye el ultimo del rango
        
        if nom_producto == al.get_element(catalog["Product"], i):
            
            contador+=1
        
            price = float(al.get_element(catalog["Price_per_Box"],i))
            sum_price += price
            if min_price == None:
                min_price = price
            else:
                min_price = min(min_price, price)
            
            if max_price == None:
                max_price = price
            else:
                max_price = max(max_price, price)
                
              
                
            discount = float(al.get_element(catalog["Discount_Pct"],i))
            sum_discount+= discount
            if min_discount == None:
                min_discount = discount
            else:
                min_discount = min(min_discount,discount)
            
            if max_discount == None:
                max_discount = discount
            else:
                max_discount = max(max_discount,discount)
                
            
            boxes = float(al.get_element(catalog["Boxes_Shipped"],i))
            sum_boxes+= boxes
            if min_boxes == None:
                min_boxes = boxes
            else:
                min_boxes = min(min_boxes,boxes)    
                
            if max_boxes == None:
                max_boxes = boxes
            else:
                max_boxes = max(max_boxes,boxes)    



            marketing = float(al.get_element(catalog["Marketing_Spend"],i))
            sum_marketing+= marketing
            if min_marketing == None:
                min_marketing = marketing
            else:
                min_marketing = min(min_marketing,marketing)
            
            
            if max_marketing == None:
                max_marketing = marketing
            else:
                max_marketing = max(max_marketing,marketing)
                
            
            
            fecha = al.get_element(catalog["Order_Date"],i)
            año = fecha[:4]
            if año in conteo_años:
                conteo_años[año] = conteo_años[año] + 1 
            else:
                conteo_años[año] = 1
            
            
            amount = float(al.get_element(catalog["Amount"],i))
            if (max_amount == None) or (amount > max_amount):
                max_amount = amount
                ubicacion_max_amount = i
            
            if (less_amount == None) or (amount < less_amount):
                less_amount = amount
                ubicacion_less_amount = i

    
    if contador == 0:
        return "No existe ese nombre en los datos"

    año_top = None
    max_conteo = 0
    
    for año in conteo_años:
        if conteo_años[año] > max_conteo:
            max_conteo = conteo_años[año]
            año_top = año
            
    a = al.get_element(catalog["Order_ID"],ubicacion_max_amount)
    b = al.get_element(catalog["Country"],ubicacion_max_amount)
    c = al.get_element(catalog["Order_Date"],ubicacion_max_amount) 
    d = al.get_element(catalog["Price_per_Box"],ubicacion_max_amount) 
    
    info_mayor_amount = "Mayor amount = "+str(a)+" "+str(b)+" "+str(c)+" "+str(d)+" "+str(max_amount)
    
    e = al.get_element(catalog["Order_ID"],ubicacion_less_amount)
    f = al.get_element(catalog["Country"],ubicacion_less_amount)
    g = al.get_element(catalog["Order_Date"],ubicacion_less_amount) 
    h = al.get_element(catalog["Price_per_Box"],ubicacion_less_amount) 
    
    info_menor_amount = "Menor amount = "+str(e)+" "+str(f)+" "+str(g)+" "+str(h)
    
    prom_price = sum_price / contador
    prom_discount = sum_discount / contador
    prom_boxes = sum_boxes / contador
    prom_marketing = sum_marketing / contador
    
    
    Tiempo_final = get_time()
    Tiempo_total = delta_time(Tiempo_inicial,Tiempo_final)
    
    return Tiempo_total, contador, prom_price, max_price, min_price, prom_discount, max_discount, min_discount, prom_boxes, max_boxes, min_boxes, prom_marketing, max_marketing, min_marketing, año_top, info_mayor_amount, info_menor_amount


def req_2(precio_minimo, precio_maximo, catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    start_time = get_time()
    cantidad_pedidos = 0
    suma_discount_pct = 0
    suma_marketing_spend = 0
    suma_prices_per_box = 0
    
    pos_mayor_order_date = None
    pos_menor_amount = None
    pos_mayor_amount = None
    
    catalog = catalog["array"]
    
    size = al.size(catalog["Price_per_Box"])
    
    for i in range(size):
        precio = al.get_element(catalog["Price_per_Box"], i)
        
        if precio_minimo <= precio <= precio_maximo:
            cantidad_pedidos += 1
            suma_prices_per_box += precio
            
            order_date = al.get_element(catalog["Order_Date"], i)
            amount = al.get_element(catalog["Amount"], i)
            
            suma_discount_pct += al.get_element(catalog["Discount_Pct"], i)
            suma_marketing_spend += al.get_element(catalog["Marketing_Spend"], i)
            
            if pos_mayor_order_date is None or order_date > al.get_element(catalog["Order_Date"], pos_mayor_order_date):
                pos_mayor_order_date = i
                
            if order_date == al.get_element(catalog["Order_Date"], pos_mayor_order_date):
                if amount > al.get_element(catalog["Amount"], pos_mayor_order_date):
                    pos_mayor_order_date = i
            
            if pos_menor_amount is None or amount < al.get_element(catalog["Amount"], pos_menor_amount):
                pos_menor_amount = i

            if pos_mayor_amount is None or amount > al.get_element(catalog["Amount"], pos_mayor_amount):
                pos_mayor_amount = i

            if amount == al.get_element(catalog["Amount"], pos_mayor_amount):
                if precio < al.get_element(catalog["Price_per_Box"], pos_mayor_amount):
                    pos_mayor_amount = i
            if amount == al.get_element(catalog["Amount"], pos_menor_amount):
                if precio < al.get_element(catalog["Price_per_Box"], pos_menor_amount):
                    pos_menor_amount = i
                    
    promedio_discount_pct = suma_discount_pct / cantidad_pedidos if cantidad_pedidos > 0 else 0
    promedio_marketing_spend = suma_marketing_spend / cantidad_pedidos if cantidad_pedidos > 0 else 0
    promedio_prices_per_box = suma_prices_per_box / cantidad_pedidos if cantidad_pedidos > 0 else 0
    
    producto_mayor_order_date = al.get_element(catalog["Product"], pos_mayor_order_date) if pos_mayor_order_date is not None else None
    pais_mayor_order_date = al.get_element(catalog["Country"], pos_mayor_order_date) if pos_mayor_order_date is not None else None
    canal_mayor_order_date = al.get_element(catalog["Channel"], pos_mayor_order_date) if pos_mayor_order_date is not None else None
    fecha_mayor_order_date = al.get_element(catalog["Order_Date"], pos_mayor_order_date) if pos_mayor_order_date is not None else None
    precio_caja_mayor_order_date = al.get_element(catalog["Price_per_Box"], pos_mayor_order_date) if pos_mayor_order_date is not None else None
    monto_mayor_order_date = al.get_element(catalog["Amount"], pos_mayor_order_date) if pos_mayor_order_date is not None else None

    producto_mayor_amount = al.get_element(catalog["Product"], pos_mayor_amount) if pos_mayor_amount is not None else None
    pais_mayor_amount = al.get_element(catalog["Country"], pos_mayor_amount) if pos_mayor_amount is not None else None
    canal_mayor_amount = al.get_element(catalog["Channel"], pos_mayor_amount) if pos_mayor_amount is not None else None
    fecha_mayor_amount = al.get_element(catalog["Order_Date"], pos_mayor_amount) if pos_mayor_amount is not None else None
    precio_caja_mayor_amount = al.get_element(catalog["Price_per_Box"], pos_mayor_amount) if pos_mayor_amount is not None else None
    monto_mayor_amount = al.get_element(catalog["Amount"], pos_mayor_amount) if pos_mayor_amount is not None else None

    producto_menor_amount = al.get_element(catalog["Product"], pos_menor_amount) if pos_menor_amount is not None else None
    pais_menor_amount = al.get_element(catalog["Country"], pos_menor_amount) if pos_menor_amount is not None else None
    canal_menor_amount = al.get_element(catalog["Channel"], pos_menor_amount) if pos_menor_amount is not None else None
    fecha_menor_amount = al.get_element(catalog["Order_Date"], pos_menor_amount) if pos_menor_amount is not None else None
    precio_caja_menor_amount = al.get_element(catalog["Price_per_Box"], pos_menor_amount) if pos_menor_amount is not None else None
    monto_menor_amount = al.get_element(catalog["Amount"], pos_menor_amount) if pos_menor_amount is not None else None

    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)
    
    return (tiempo_ejecucion, cantidad_pedidos, promedio_discount_pct, promedio_marketing_spend, promedio_prices_per_box, producto_mayor_order_date, pais_mayor_order_date, canal_mayor_order_date, fecha_mayor_order_date, precio_caja_mayor_order_date, monto_mayor_order_date, producto_mayor_amount, pais_mayor_amount, canal_mayor_amount, fecha_mayor_amount, precio_caja_mayor_amount, monto_mayor_amount, producto_menor_amount, pais_menor_amount, canal_menor_amount, fecha_menor_amount, precio_caja_menor_amount, monto_menor_amount)


def req_3(catalog, Country, Channel):
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
        
        if pais == Country and canal == Channel:
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

def req_4(catalog, producto, pais):
    """
    Retorna el resultado del requerimiento 4
    """

    # TODO: Modificar el requerimiento 4
    
    total_pedidos = 0
    precio_prom_price = 0
    prom_discount = 0
    prom_marketing = 0
    prom_boxes = 0
    dict_amount = {}
    
    n = sl.size(catalog)
    
    for i in range(1, n+1):
        if (sl.get_element(catalog["Product"]) == producto) and (sl.get_element(catalog["Country"]) == pais):
    
            total_pedidos += 1
            precio_prom_price += float(sl.get_element(catalog["Price_per_box"]))
            prom_discount += float(sl.get_element(catalog["Discount_pct"]))
            prom_marketing += float(sl.get_element(catalog["Marketing_spend"]))
            prom_marketing += float(sl.get_element(catalog["Boxes_Shipped"]))
            
            dict_amount
    
    
    
    pass


def req_5(catalog, filtro, producto, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    cantidad_pedidos = 0
    suma_precio = 0
    suma_cajas = 0
    suma_inversion_mercado = 0
    actual = catalog["first"]
    orden_comparacion = None
    
    while actual is not None:
        current = actual["info"]
        if current["Product"] == producto and current["Order_Date"] >= fecha_inicial and current["Order_Date"] <= fecha_final:
            cantidad_pedidos += 1
            suma_precio += current["Price_per_Box"]
            suma_cajas += current["Boxes_Shipped"]
            suma_inversion_mercado += current["Marketing_Spend"]
            
            
            if filtro == "MAYOR":
                if orden_comparacion is None or current["Amount"] > orden_comparacion["Amount"]:
                    orden_comparacion = current
                elif current["Amount"] == orden_comparacion["Amount"] and current["Price_per_Box"] < orden_comparacion["Price_per_Box"]:
                    orden_comparacion = current     
            elif filtro == "MENOR":
                if orden_comparacion is None or current["Amount"] < orden_comparacion["Amount"]:
                    orden_comparacion = current
                elif current["Amount"] == orden_comparacion["Amount"] and current["Price_per_Box"] < orden_comparacion["Price_per_Box"]:
                    orden_comparacion = current
            else:
                orden_comparacion = -1  # Valor inválido para el filtro

        actual = actual["next"]
    
    if cantidad_pedidos > 0:
        promedio_precio = suma_precio / cantidad_pedidos
        promedio_cajas = suma_cajas / cantidad_pedidos
        promedio_inversion_mercado = suma_inversion_mercado / cantidad_pedidos
    else:
        promedio_precio = "Unknown"
        promedio_cajas = "Unknown"
        promedio_inversion_mercado = "Unknown"
        
    if orden_comparacion != -1:
        precio_caja = orden_comparacion["Price_per_Box"]
        cajas_enviadas = orden_comparacion["Boxes_Shipped"]
        monto_total = orden_comparacion["Amount"]
        canal = orden_comparacion["Channel"]
        fecha_pedido = orden_comparacion["Order_Date"]
        inversion_mercado = orden_comparacion["Marketing_Spend"]
    else:
        precio_caja = "Unknown"
        cajas_enviadas = "Unknown"
        monto_total = "Unknown"
        canal = "Unknown"
        fecha_pedido = "Unknown"
        inversion_mercado = "Unknown"
        
    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)
    
    return (tiempo_ejecucion, cantidad_pedidos, promedio_precio, promedio_cajas, promedio_inversion_mercado, precio_caja, cajas_enviadas, monto_total, canal, fecha_pedido, inversion_mercado)

def req_6(catalog, Fecha_inicial, Fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    #pass
    start_time = get_time()
    tamaño = data_structure.size(catalog["Order_ID"])
    N = 0
    canales = {}

    for i in range(tamaño):
        fecha = str(data_structure.get_element(catalog["Order_Date"], i))
        
        if Fecha_inicial <= fecha <= Fecha_final:
            N += 1
            canal = data_structure.get_element(catalog["Channel"], i)
            
            orden = data_structure.get_element(catalog["Order_ID"], i)
            producto = data_structure.get_element(catalog["Product"], i)
            pais = data_structure.get_element(catalog["Country"], i)
            monto = float(data_structure.get_element(catalog["Amount"], i))
            precio = float(data_structure.get_element(catalog["Price_per_Box"], i))
            marketing = float(data_structure.get_element(catalog["Marketing_Spend"], i))
            cajas = int(data_structure.get_element(catalog["Boxes_Shipped"], i))
            
            pedido_actual = {
                "Order_ID": orden,
                "Product": producto,
                "Country": pais,
                "Channel": canal,
                "Order_Date": fecha,
                "Price_per_Box": precio,
                "Boxes_Shipped": cajas,
                "Amount": monto
            }
            
            if canal not in canales:
                canales[canal] = {
                    'count': 0,
                    'total_amt': 0.0,
                    'sum_price': 0.0,
                    'sum_mkt': 0.0,
                    'min_order': pedido_actual,
                    'max_order': pedido_actual
                }
            
            c = canales[canal]
            c['count'] += 1
            c['total_amt'] += monto
            c['sum_price'] += precio
            c['sum_mkt'] += marketing
            
            # Criterio de desempate para pedido mínimo de ese canal
            if monto < c['min_order']["Amount"]:
                c['min_order'] = pedido_actual
            elif monto == c['min_order']["Amount"] and precio < c['min_order']["Price_per_Box"]:
                c['min_order'] = pedido_actual
                
            # Criterio de desempate para pedido máximo de ese canal
            if monto > c['max_order']["Amount"]:
                c['max_order'] = pedido_actual
            elif monto == c['max_order']["Amount"] and precio < c['max_order']["Price_per_Box"]:
                c['max_order'] = pedido_actual

    if N == 0:
        return pop_time, 0, None, None, {}

    Canal_mas_usado = max(canales.items(), key=lambda x: x[1]['count'])
    Canal_mas_recaudador = max(canales.items(), key=lambda x: x[1]['total_amt'])
    end_time = get_time()
    pop_time = delta_time(start_time, end_time)

    return pop_time, N, Canal_mas_usado, Canal_mas_recaudador, canales



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
