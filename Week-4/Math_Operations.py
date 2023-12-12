def basic_operations(a,b):
    try:
        add = a+b
        sub = a-b
        mul = a*b
        div = a/b
        return {"+":add,"-":sub,"*":mul,"/":div}
    except TypeError:
        return "Invalid input"
    except ZeroDivisionError:
        return "Can't divide by zero"
def power_operations(a,b,**kwargs):
    try:
        power = a**b
        modulo = kwargs.get("modulus")
        if modulo is not None:
            power %= modulo
        return power
    except TypeError:
        return "Invalid input"
    except ZeroDivisionError:
        return "Error: Division by zero."
def apply_operations(operations):
    result = list(map(lambda x: x[0](*x[1]), operations))
    return result
    
