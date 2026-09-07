from DataStructures.List import single_linked_list as lt


def new_queue():
    queue = lt.new_list()
    return(queue) 


    

def enqueue(my_queue, element):
    my_queue= lt.add_last(my_queue, element)
    return(my_queue)
    


    
def dequeue(my_queue):
    if lt.is_empty(my_queue) == True:
        raise Exception('EmptyStructureError: queue is empty')
    elemento = lt.first_element(my_queue)
    lt.remove_first(my_queue)
    return (elemento) 
    



def is_empty(my_queue):
    return(lt.is_empty(my_queue))



def peek(my_queue):
    if lt.is_empty(my_queue) == True:
        raise Exception('EmptyStructureError: queue is empty')
    elemento = lt.first_element(my_queue)
    return elemento



def size(my_queue):
    return(lt.size(my_queue))
    