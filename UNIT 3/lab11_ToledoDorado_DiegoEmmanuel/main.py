from exceptions import ErrorInventario

def main():
    # Search the product
    inventario = inventario()
    codigo = input("Codigo del prodcuto").strip()
    try:
        # Operation
        cantidad = int(input("Cantidad a retirar: "))
        inventario.retirar(codigo, cantidad)
        print(
            "Retiro realizado. Stock restante: ",
            inventario.productos[codigo].stock
        )
        # Negative Quantity
    except ValueError:
        print("La cantidad debe de ser un numero entero")
        # Negavtive Stock
    except ErrorInventario as error:
        print("No se pudo realizar la operación: {error}")