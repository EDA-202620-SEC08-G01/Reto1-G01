import time

import csv
csv.field_size_limit(2147483647)

import os

from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

csv.field_size_limit(2147483647)

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    
    catalog = {"array": al.new_list(), "single_linked": sl.new_list()}
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    start_time = get_time()

    with open(data_dir + filename, encoding='utf-8-sig') as f:
        archivo = csv.DictReader(f)

        pedido_menor = None
        pedido_mayor = None

        for fila in archivo:
            fila["Discount_Pct"] = float(fila["Discount_Pct"])
            fila["Price_per_Box"] = float(fila["Price_per_Box"])
            fila["Marketing_Spend"] = float(fila["Marketing_Spend"])
            fila["Boxes_Shipped"] = int(fila["Boxes_Shipped"])
            fila["Amount"] = float(fila["Amount"])

            al.add_last(catalog["array"], fila)
            sl.add_last(catalog["single_linked"], fila)

            if pedido_menor is None or fila["Amount"] < pedido_menor["Amount"]:
                pedido_menor = fila
            elif fila["Amount"] == pedido_menor["Amount"] and fila["Price_per_Box"] < pedido_menor["Price_per_Box"]:
                pedido_menor = fila

            if pedido_mayor is None or fila["Amount"] > pedido_mayor["Amount"]:
                pedido_mayor = fila
            elif fila["Amount"] == pedido_mayor["Amount"] and fila["Price_per_Box"] < pedido_mayor["Price_per_Box"]:
                pedido_mayor = fila

    total_pedidos = al.size(catalog["array"])

    primeros_5 = al.new_list()
    for i in range(min(5, total_pedidos)):
        al.add_last(primeros_5, al.get_element(catalog["array"], i))

    ultimos_5 = al.new_list()
    for i in range(max(0, total_pedidos - 5), total_pedidos):
        al.add_last(ultimos_5, al.get_element(catalog["array"], i))

    end_time = get_time()
    tiempo_carga = delta_time(start_time, end_time)

    return tiempo_carga, total_pedidos, pedido_menor, pedido_mayor, primeros_5, ultimos_5
        

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
    start_time = get_time()
    cantidad_pedidos = 0
    suma_discount_pct = 0
    suma_marketing_spend = 0
    suma_prices_per_box = 0

    pedido_mas_reciente = None
    pedido_menor_amount = None
    pedido_mayor_amount = None

    catalog = catalog["array"]
    size = al.size(catalog)

    for i in range(size):
        fila = al.get_element(catalog, i)
        precio = fila["Price_per_Box"]

        if precio_minimo <= precio <= precio_maximo:
            cantidad_pedidos += 1
            suma_prices_per_box += precio
            suma_discount_pct += fila["Discount_Pct"]
            suma_marketing_spend += fila["Marketing_Spend"]

            if pedido_mas_reciente is None or fila["Order_Date"] > pedido_mas_reciente["Order_Date"]:
                pedido_mas_reciente = fila
            elif fila["Order_Date"] == pedido_mas_reciente["Order_Date"] and fila["Amount"] > pedido_mas_reciente["Amount"]:
                pedido_mas_reciente = fila

            if pedido_menor_amount is None or fila["Amount"] < pedido_menor_amount["Amount"]:
                pedido_menor_amount = fila
            elif fila["Amount"] == pedido_menor_amount["Amount"] and precio < pedido_menor_amount["Price_per_Box"]:
                pedido_menor_amount = fila

            if pedido_mayor_amount is None or fila["Amount"] > pedido_mayor_amount["Amount"]:
                pedido_mayor_amount = fila
            elif fila["Amount"] == pedido_mayor_amount["Amount"] and precio < pedido_mayor_amount["Price_per_Box"]:
                pedido_mayor_amount = fila

    promedio_discount_pct = suma_discount_pct / cantidad_pedidos if cantidad_pedidos > 0 else 0
    promedio_marketing_spend = suma_marketing_spend / cantidad_pedidos if cantidad_pedidos > 0 else 0
    promedio_prices_per_box = suma_prices_per_box / cantidad_pedidos if cantidad_pedidos > 0 else 0

    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)

    return (tiempo_ejecucion, cantidad_pedidos, promedio_discount_pct, promedio_marketing_spend, promedio_prices_per_box, pedido_mas_reciente, pedido_mayor_amount, pedido_menor_amount)


def req_3(catalog, Country, Channel):
    """
    Retorna el resultado del requerimiento 3 usando sl (Single Linked List)
    """
    start_time = get_time()
    
    # 1. Acceder a la lista enlazada
    catalog = catalog["single_linked"]
    
    # 2. Obtener el tamaño usando la librería sl
    tamaño = sl.size(catalog)
    
    N = 0
    suma_precio = 0
    suma_descuento = 0
    suma_marketing = 0
    suma_cajas = 0

    conteo_productos = {}
    conteo_anios = {}

    # 3. Recorrer usando sl.get_element(catalog, i)
    for i in range(tamaño):
        fila = sl.get_element(catalog, i)
        
        # Filtrar por País y Canal
        if fila["Country"] == Country and fila["Channel"] == Channel:
            N += 1
            suma_precio += fila["Price_per_Box"]
            suma_descuento += fila["Discount_Pct"]
            suma_marketing += fila["Marketing_Spend"]
            suma_cajas += fila["Boxes_Shipped"]
            
            # Conteo para el producto más frecuente
            prod = fila["Product"]
            conteo_productos[prod] = conteo_productos.get(prod, 0) + 1
            
            # Conteo para el año con más pedidos
            fecha = fila["Order_Date"]
            anio = str(fecha).split("-")[0] if fecha else "Desconocido"
            conteo_anios[anio] = conteo_anios.get(anio, 0) + 1

    # 4. Calcular promedios y modas
    if N > 0:
        p_precio = suma_precio / N
        p_desc = suma_descuento / N
        p_mkt = suma_marketing / N
        p_cajas = suma_cajas / N
        
        moda_prod = max(conteo_productos, key=conteo_productos.get) if conteo_productos else "Desconocido"
        moda_anio = max(conteo_anios, key=conteo_anios.get) if conteo_anios else "Desconocido"
    else:
        p_precio = 0
        p_desc = 0
        p_mkt = 0
        p_cajas = 0
        moda_prod = "Desconocido"
        moda_anio = "Desconocido"

    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)

    # 5. Retornar en el orden esperado por view.py
    return (tiempo_ejecucion, N, p_precio, p_desc, p_mkt, p_cajas, moda_prod, moda_anio)

    # 4. Calcular promedios
    if N > 0:
        p_precio = suma_precio / N
        p_desc = suma_descuento / N
        p_mkt = suma_marketing / N
        p_cajas = suma_cajas / N
        
        # Encontrar la moda del producto (el más frecuente)
        moda_prod = max(conteo_productos, key=conteo_productos.get) if conteo_productos else "Desconocido"
        
        # Encontrar la moda del año (el año con más pedidos)
        moda_anio = max(conteo_anios, key=conteo_anios.get) if conteo_anios else "Desconocido"
    else:
        p_precio = 0
        p_desc = 0
        p_mkt = 0
        p_cajas = 0
        moda_prod = "Desconocido"
        moda_anio = "Desconocido"

    end_time = get_time()
    tiempo_ejecucion = delta_time(start_time, end_time)

    # 5. Retornar en el orden exacto que espera tu función print_req_3 en view.py
    return (tiempo_ejecucion, N, p_precio, p_desc, p_mkt, p_cajas, moda_prod, moda_anio)

def req_4(catalog, producto, pais):
    """
    Retorna el resultado del requerimiento 4
    """

    # TODO: Modificar el requerimiento 4
    inicio = get_time()
    
    total_pedidos = 0
    prom_price = 0
    prom_discount = 0
    prom_marketing = 0
    prom_boxes = 0
    
    top_amount_1 = None
    top_amount_2 = None
    
    n = sl.size(catalog["Product"])
    
    for i in range(1, n+1):
        if (sl.get_element(catalog["Product"], i) == producto) and (sl.get_element(catalog["Country"], i) == pais):
            
            total_pedidos+=1
            
            price = float(sl.get_element(catalog["Price_per_Box"], i))
            discount = float(sl.get_element(catalog["Discount_Pct"], i))
            marketing = float(sl.get_element(catalog["Marketing_Spend"], i))
            boxes = float(sl.get_element(catalog["Boxes_Shipped"], i))
            
            prom_price += price
            prom_discount += discount
            prom_marketing += marketing
            prom_boxes += boxes
            
            amount = float(sl.get_element(catalog["Amount"], i))
            order_id = sl.get_element(catalog["Order_ID"], i)
            channel = sl.get_element(catalog["Channel"], i)
            fecha = sl.get_element(catalog["Order_Date"], i)


            
            posible = {"amount": amount,
                       "marketing": marketing,
                       "order_id": order_id,
                       "channel": channel,
                       "fecha": fecha
                    }
            
            if top_amount_1 is None:
                top_amount_1 = posible
            
            elif (amount > top_amount_1["amount"]) or ((amount == top_amount_1["amount"]) and (marketing < top_amount_1["marketing"])) or ((amount == top_amount_1["amount"]) and (marketing == top_amount_1["marketing"]) and (order_id < top_amount_1["order_id"])):
                top_amount_2 = top_amount_1
                top_amount_1 = posible
        
            elif top_amount_2 is None:
                top_amount_2 = posible
            
            elif (amount > top_amount_2["amount"]) or ((amount == top_amount_2["amount"]) and (marketing < top_amount_2["marketing"])) or ((amount == top_amount_2["amount"]) and (marketing == top_amount_2["marketing"]) and (order_id < top_amount_2["order_id"])):
                top_amount_2 = posible
            
    if total_pedidos == 0:
        return "No hubo pedidos con esa combinación"
    
    prom_price = prom_price / total_pedidos
    prom_discount = prom_discount / total_pedidos
    prom_marketing = prom_marketing / total_pedidos
    prom_boxes = prom_boxes / total_pedidos
    
    final = get_time()
    tiempo_total = delta_time(inicio, final)
    
    return tiempo_total, prom_price, prom_discount, prom_marketing, prom_boxes, top_amount_1, top_amount_2


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
    catalog = catalog["single_linked"]
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
    start_time = get_time()
    tamaño = al.size(catalog["Order_ID"])
    N = 0
    canales = {}

    for i in range(tamaño):
        fecha = str(al.get_element(catalog["Order_Date"], i))
        
        if Fecha_inicial <= fecha <= Fecha_final:
            N += 1
            canal = al.get_element(catalog["Channel"], i)
            
            orden = al.get_element(catalog["Order_ID"], i)
            producto = al.get_element(catalog["Product"], i)
            pais = al.get_element(catalog["Country"], i)
            monto = float(al.get_element(catalog["Amount"], i))
            precio = float(al.get_element(catalog["Price_per_Box"], i))
            marketing = float(al.get_element(catalog["Marketing_Spend"], i))
            cajas = int(al.get_element(catalog["Boxes_Shipped"], i))
            
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
