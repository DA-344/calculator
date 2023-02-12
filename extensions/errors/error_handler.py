from __future__ import annotations

from typing import Dict, List, Optional, TYPE_CHECKING, Any, Tuple, Union

__all__ = (
    'LibraryException',
    'InvalidObject',
    'InvalidOperation',
    'OperationError',
    'ZeroDivision'
)

class LibraryException(Exception):
    """
    Excepción madre de todas las demás.

    Es la raíz de todas las excepciones que pueden detectarse.
    """

    pass

def _flatten_error_dict(d: Dict[str, Any], key: str = '') -> Dict[str, str]:
    items: List[Tuple[str, str]] = []

    for k, v in d.items():
        new_key = key +'.'+k if key else k

        if isinstance(v, dict):
            try:
                _errors: List[Dict[str, Any]] = v['_errors']

            except KeyError:
                items.extend(_flatten_error_dict(v, new_key).items())

            else:
                items.append((new_key, ' '.join(x.get('message', '') for x in _errors)))
        
        else:
            items.append((new_key, v))

    return dict(items)

class InvalidObject(LibraryException):
    """
    Error invocado cuando un objeto inválido se atribuye.

    Atributos
    ------------
    mensaje: :Optional:`str`
        El mensaje de respuesta del error.

    objeto: :class:`Any`
        El objeto que salta error.
    """

    def __init__(self, mensaje:Optional[str], objeto:Any) -> None:
        self.mensaje: str = mensaje if mensaje else "ERROR CACHED"
        self.objeto: Any = objeto

        super().__init__(f'{self.mensaje}: {self.objeto} es un objecto inválido.')

class InvalidOperation(LibraryException):
    """
    Error invocado cuando la operación especificada es inválida.

    Atributos
    -----------
    mensaje: :Optional:`str`
        El mensaje de respuesta del error

    operacion: :class:`str`
        La operación que se intentaba hacer
    """

    def __init__(self, mensaje:Optional[str], objeto:Any) -> None:
        self.mensaje: str = mensaje if mensaje else "ERROR CACHED"
        self.objeto: Any = objeto

        super().__init__(f'{self.mensaje}: {self.objeto} es una operación no permitida.')

class OperationError(LibraryException):
    """
    Excepción madre de todas las excepciones relacionadas con las operaciones.
    """

    pass

class ZeroDivision(OperationError):
    """
    Error invocado cuando la operación es una división y su variable :variable:`num2` es :int:`0`

    Atributos
    -----------
    mensaje: :Optional:`str`
        El mensaje de respuesta del error

    param: :Parameter:`Any`
        El parametro que resulta inválido
    """

    def __init__(self, mensaje:Optional[str], param:Any) -> None:
        self.mensaje:str = mensaje if mensaje else "ERROR CACHED"
        self.param: Any = param

        super().__init__(f'{self.mensaje}: El parámetro {self.param} no puede ser cero.')