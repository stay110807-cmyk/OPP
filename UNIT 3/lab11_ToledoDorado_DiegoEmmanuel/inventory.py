from exceptions import ProductNoEncontrado
from products import Producto

# products
class inventario:
    def __init__(self):
        self.productos = {
            "P01": Producto("P01", 5),
            "P02": Producto("P02", 10),
            "P03": Producto("P03", 8),
            "P04": Producto("P04", 15),
            "P05": Producto("P05", 89)
        
        }

    
    def retirar(self, codigo, cantidad):
        self.codigo = codigo
        self.cantidad = cantidad
        
        Producto.retirar(self, cantidad)
        
        if self.codigo in self.productos:
            print("El producto existe!")
        else:
            raise ProductNoEncontrado("El prodcuto no existe!")
