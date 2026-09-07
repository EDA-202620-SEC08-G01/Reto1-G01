from DataStructures.List import single_linked_list as lt

def new_stack():
    stack = lt.new_list()
    return stack
    
    
def push(my_stack,element):    
    my_stack = lt.add_first(my_stack, element)
    return my_stack


def pop(my_stack):
    if lt.is_empty(my_stack) == True:
        raise Exception('EmptyStructureError: stack is empty')
    elemento = lt.first_element(my_stack)
    lt.remove_first(my_stack)
    return elemento
    

def is_empty(my_stack):
    return(lt.is_empty(my_stack))
    

# peek() = top()
def top(my_stack):
    if lt.is_empty(my_stack) == True:
        raise Exception('EmptyStructureError: stack is empty')
    elemento = lt.first_element(my_stack)
    return elemento

def size(my_stack):
    return lt.size(my_stack)