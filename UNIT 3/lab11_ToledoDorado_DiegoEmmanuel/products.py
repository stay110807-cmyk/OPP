from exceptions import  stockInsuficiente, CantidadInvalida


class Producto:
    def __init__(self, codigo, stock):
        self.codigo = codigo
        self.stock = stock
    # Validaton for quantity
    def retirar(self, cantidad):
        if cantidad is isinstance(cantidad,int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise CantidadInvalida("No es posible realizar esta operación")
    
    # Validation for stock  
        if self.stock >= cantidad:
            raise stockInsuficiente(f"Quantity: {self.cantidad}, stock: b{self.stock}")

        self.stock -= cantidad 
        return self.stock