# all binding
class ErrorInventario(Exception):
    pass

class ProductNoEncontrado(ErrorInventario):
    pass 

class CantidadInvalida(ErrorInventario):
    pass

class stockInsuficiente(ErrorInventario):
    pass