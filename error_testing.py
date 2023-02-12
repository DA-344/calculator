from extensions.errors import error_handler
from typing import Union

def _calc(num1:Union[float, int], num2:Union[float, int], *, operacion:str = "+", truncamiento:bool = True) -> None:

    try:
        num1 = int(num1)
        num2 = int(num2)

    except:
        raise error_handler.InvalidObject(None, (num1, num2))

    if operacion not in ["+", "-", "/", "x", "×", "÷"]:
        raise error_handler.InvalidOperation(None, operacion)

    if operacion in ["÷", "/"]:
        if num2 == 0:
            raise error_handler.ZeroDivision(None, "num2")

        resultado:int = num1/num2

    if operacion in ["x", "×"]:
        resultado:int = num1*num2

    if operacion in ["+"]:
        resultado:int = num1+num2

    if operacion in ["-"]:
        resultado:int = num1-num2

    if truncamiento == True:
        return round(resultado, None)

    elif truncamiento == False:
        return resultado

print(_calc("5", "2", operacion="/", truncamiento=False))