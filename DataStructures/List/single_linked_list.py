def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"] 

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    new = {
        "info": element,
        "next": my_list["first"]
    }
    my_list["first"] = new
    if my_list["last"] is None:
        my_list["last"] = new
    my_list["size"] += 1
    
def add_last(my_list, element):
    new = {
        "info": element,
        "next": None
    }
    if my_list["last"] is not None:
        my_list["last"]["next"] = new
    my_list["last"] = new
    if my_list["first"] is None:
        my_list["first"] = new
    my_list["size"] += 1
    
def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')


    if my_list["first"] is None:  
        return None 
    
    return my_list["first"]["info"]
    
def is_empty(my_list):
    if my_list["size"] == 0:
        return True
    return False

def last_element(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')

    if my_list["last"] is None:  
        return None  
    
    return my_list["last"]["info"]

def delete_element(my_list, pos):
    if pos >= my_list["size"] or pos < 0:
        raise Exception('IndexError: list index out of range')
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        if my_list["first"] is None:
            my_list["last"] = None
    else:
        now = my_list["first"]
        contador = 0
        centinela = True
        while centinela:
            if pos == contador:
                now["next"] = now["next"]["next"]
                if now["next"] is None:
                    my_list["last"] = now
                centinela = False
            else:
                now = now["next"]
                contador += 1
    my_list["size"] -= 1
    return my_list
  
def remove_first(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    
    element = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    
    if my_list["first"] is None:
        my_list["last"] = None
    my_list["size"] -= 1
    return element

def remove_last(my_list):
    if my_list["size"] == 0:
        raise Exception('IndexError: list index out of range')
    
    if my_list["first"] == my_list["last"]:
        element = my_list["first"]["info"]
        my_list["first"] = None
        my_list["last"] = None
    else:
        now = my_list["first"]
        while now["next"] != my_list["last"]:
            now = now["next"]
        element = my_list["last"]["info"]
        now["next"] = None
        my_list["last"] = now
    
    my_list["size"] -= 1
    return element

def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise IndexError("IndexError: list index out of range")
    
    new_node = {
        "info": element,
        "next": None
    }
    
    if pos == 0:
        new_node["next"] = my_list["first"]
        my_list["first"] = new_node
        if my_list["size"] == 0:
            my_list["last"] = new_node
    else:
        now = my_list["first"]
        for i in range(pos - 1):
            now = now["next"]
        new_node["next"] = now["next"]
        now["next"] = new_node
        
        if new_node["next"] is None:
            my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if pos >= my_list["size"] or pos < 0:
        raise Exception('IndexError: list index out of range')
    
    now = my_list["first"]
    contador = 0
    centinela = True
    while centinela:
        if pos == contador:
            now["info"] = new_info
            centinela = False
        else:
            now = now["next"]
            contador += 1
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 >= my_list["size"] or pos1 < 0 or pos2 >= my_list["size"] or pos2 < 0:
        raise Exception('IndexError: list index out of range')
    
    if pos1 == pos2:
        return my_list
    
    now1 = my_list["first"]
    now2 = my_list["first"]
    contador1 = 0
    contador2 = 0
    centinela1 = True
    centinela2 = True
    
    while centinela1 or centinela2:
        if centinela1 and pos1 == contador1:
            centinela1 = False
        else:
            now1 = now1["next"]
            contador1 += 1
        
        if centinela2 and pos2 == contador2:
            centinela2 = False
        else:
            now2 = now2["next"]
            contador2 += 1
    
    now1["info"] = now2["info"]
    now2["info"] = now1["info"]
    
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i >= my_list["size"] or pos_i < 0 or num_elements < 0 or pos_i + num_elements > my_list["size"]:
        raise Exception('IndexError: list index out of range')
    
    new_list = {
        "first": None,
        "last": None,
        "size": 0,
    }
    
    now = my_list["first"]
    contador = 0
    centinela = True
    
    while centinela:
        if pos_i <= contador < pos_i + num_elements:
            add_last(new_list, now["info"])
        
        if contador >= pos_i + num_elements - 1:
            centinela = False
        else:
            now = now["next"]
            contador += 1
    
    return new_list
