from datetime import datetime, timedelta

def validar_fecha(fecha_str):
  """Valida si una cadena es una fecha válida."""
  try:
    datetime.strptime(fecha_str, '%Y-%m-%d')
    return True
  except ValueError:
    return False

def medir_tiempo(func):
  """Decorador para medir el tiempo de ejecución de una función."""
  def wrapper(*args, **kwargs):
    inicio = datetime.now()
    resultado = func(*args, **kwargs)
    fin = datetime.now()
    tiempo_ejecucion = fin - inicio
    print(f"Tiempo de ejecución de {func.__name__}: {tiempo_ejecucion}")
    return resultado
  return wrapper

class Tarea:
  """Representa una tarea."""

  def __init__(self, titulo, descripcion, fecha_vencimiento):
    """Inicializa una tarea."""
    self.titulo = titulo
    self.descripcion = descripcion
    self.fecha_vencimiento = fecha_vencimiento

  def __str__(self):
    """Representación en cadena de la tarea."""
    return f"Título: {self.titulo}\nDescripción: {self.descripcion}\nFecha de vencimiento: {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

class GestorTareas:
  """Gestiona las tareas."""

  def __init__(self):
    """Inicializa el gestor de tareas."""
    self.tareas = []

  @medir_tiempo
  def agregar_tarea(self, titulo, descripcion, fecha_vencimiento):
    """Agrega una nueva tarea."""
    if not isinstance(titulo, str):
      raise TypeError("El título debe ser una cadena.")
    if not isinstance(descripcion, str):
      raise TypeError("La descripción debe ser una cadena.")
    if not validar_fecha(fecha_vencimiento):
      raise ValueError("La fecha de vencimiento no es válida. Formato: YYYY-MM-DD")
    fecha_vencimiento = datetime.strptime(fecha_vencimiento, '%Y-%m-%d').date()
    tarea = Tarea(titulo, descripcion, fecha_vencimiento)
    self.tareas.append(tarea)
    print(f"Tarea '{titulo}' agregada exitosamente.")

  @medir_tiempo
  def eliminar_tarea(self, titulo):
    """Elimina una tarea por título."""
    if not isinstance(titulo, str):
      raise TypeError("El título debe ser una cadena.")
    for i, tarea in enumerate(self.tareas):
      if tarea.titulo == titulo:
        del self.tareas[i]
        print(f"Tarea '{titulo}' eliminada exitosamente.")
        return
    print(f"No se encontró la tarea '{titulo}'.")

  @medir_tiempo
  def listar_tareas(self):
    """Lista todas las tareas."""
    if not self.tareas:
      print("No hay tareas en la lista.")
      return
    print("Lista de tareas:")
    for i, tarea in enumerate(self.tareas):
      print(f"{i+1}. {tarea}")

# Ejemplo de uso
gestor = GestorTareas()

gestor.agregar_tarea("Tarea 1", "Completar el informe", "2024-01-15")
gestor.agregar_tarea("Tarea 2", "Enviar la presentación", "2024-01-20")

gestor.listar_tareas()

gestor.eliminar_tarea("Tarea 1")

gestor.listar_tareas()