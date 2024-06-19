class Permutador:
    """Generador de permutaciones usando recursión."""

    def __init__(self):
        self.permutaciones = []

    def generar_permutaciones(self, lista):
        """Genera todas las permutaciones posibles de una lista."""
        self.permutaciones = []
        self._permutar(lista, 0, len(lista))
        return self.permutaciones

    def _permutar(self, lista, inicio, fin):
        """Función recursiva auxiliar para generar permutaciones."""
        if inicio == fin:
            self.permutaciones.append(lista[:])
        else:
            for i in range(inicio, fin):
                lista[inicio], lista[i] = lista[i], lista[inicio]
                self._permutar(lista, inicio + 1, fin)
                lista[inicio], lista[i] = lista[i], lista[inicio]

# Ejemplo de uso
generador = Permutador()
numeros = [1, 2, 3, 4, 5]
permutaciones = generador.generar_permutaciones(numeros)
print(f"Permutaciones de {numeros}:")
for permutacion in permutaciones:
    print(permutacion)
