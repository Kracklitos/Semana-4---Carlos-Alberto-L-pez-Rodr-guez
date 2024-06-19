class Producto:
    """Representa un producto en el inventario."""

    def __init__(self, nombre, categoria, precio):
        """Inicializa un producto."""
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __eq__(self, otro_producto):
        """Compara productos por precio y devuelve un mensaje informativo."""
        if isinstance(otro_producto, Producto):
            if self.precio < otro_producto.precio:
                return f"El producto '{self.nombre}' es más barato que '{otro_producto.nombre}'"
            elif self.precio > otro_producto.precio:
                return f"El producto '{self.nombre}' es más caro que '{otro_producto.nombre}'"
            else:
                return f"El producto '{self.nombre}' tiene el mismo precio que '{otro_producto.nombre}'"
        return False

    def __str__(self):
        """Representación en cadena del producto."""
        return f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}"

class Inventario:
    """Gestiona el inventario de productos."""

    def __init__(self):
        """Inicializa el inventario."""
        self.productos = []

    def agregar_producto(self, nombre, categoria, precio):
        """Agrega un nuevo producto al inventario."""
        producto = Producto(nombre, categoria, precio)
        self.productos.append(producto)
        print(f"Producto '{nombre}' agregado al inventario.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario por nombre."""
        for i, producto in enumerate(self.productos):
            if producto.nombre == nombre:
                del self.productos[i]
                print(f"Producto '{nombre}' eliminado del inventario.")
                return
        print(f"No se encontró el producto '{nombre}' en el inventario.")

    def listar_productos(self):
        """Lista todos los productos del inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        print("Productos en el inventario:")
        for producto in self.productos:
            print(producto)

    def buscar_producto(self, nombre=None, categoria=None, precio=None):
        """Busca productos por nombre, categoría o precio."""
        productos_encontrados = []
        for producto in self.productos:
            if nombre and producto.nombre == nombre:
                productos_encontrados.append(producto)
            elif categoria and producto.categoria == categoria:
                productos_encontrados.append(producto)
            elif precio and producto == Producto("", "", precio):  # Usa __eq__ para comparar precios
                productos_encontrados.append(producto)

        if productos_encontrados:
            print("Productos encontrados:")
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos que coincidan con la búsqueda.")

# Ejemplo de uso
inventario = Inventario()

# Agregar productos al inventario
inventario.agregar_producto("Laptop", "Electrónica", 1200)
inventario.agregar_producto("Camiseta", "Ropa", 20)
inventario.agregar_producto("Silla", "Muebles", 80)
inventario.agregar_producto("Teclado", "Electrónica", 50)

# Listar todos los productos
print("\nLista de productos:")
inventario.listar_productos()

# Eliminar un producto
print("\nEliminar producto 'Camiseta':")
inventario.eliminar_producto("Camiseta")

# Listar productos después de eliminar
print("\nLista de productos después de eliminar:")
inventario.listar_productos()

# Buscar productos por nombre
print("\nBuscar producto por nombre 'Laptop':")
inventario.buscar_producto(nombre="Laptop")

# Buscar productos por categoría
print("\nBuscar productos por categoría 'Electrónica':")
inventario.buscar_producto(categoria="Electrónica")

# Buscar productos por precio
print("\nBuscar productos por precio 50:")
inventario.buscar_producto(precio=50)

# Obtener productos para comparar
laptop = inventario.productos[0]
camiseta = inventario.productos[1]

# Comparar los productos y mostrar el resultado
comparacion = laptop == camiseta
print(comparacion) 
