class Conjunto:
    """Representa un conjunto de enteros."""

    def __init__(self, elementos=None):
        """Inicializa un conjunto."""
        self.elementos = set()
        if elementos is not None:
            for elemento in elementos:
                self.add(elemento)

    def add(self, elemento):
        """Agrega un elemento al conjunto."""
        self.elementos.add(elemento)

    def __add__(self, otro_conjunto):
        """Realiza la unión de conjuntos."""
        nuevo_conjunto = Conjunto()
        nuevo_conjunto.elementos = self.elementos.union(otro_conjunto.elementos)
        return nuevo_conjunto

    def __mul__(self, otro_conjunto):
        """Realiza la intersección de conjuntos."""
        nuevo_conjunto = Conjunto()
        nuevo_conjunto.elementos = self.elementos.intersection(otro_conjunto.elementos)
        return nuevo_conjunto

    def __str__(self):
        """Representación en cadena del conjunto."""
        return "{" + ", ".join(str(e) for e in self.elementos) + "}"


# Ejemplo de uso
conjunto1 = Conjunto([1, 2, 3])
conjunto2 = Conjunto([2, 3, 4])

print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}")

union = conjunto1 + conjunto2
print(f"Unión: {union}")

interseccion = conjunto1 * conjunto2
print(f"Intersección: {interseccion}")
