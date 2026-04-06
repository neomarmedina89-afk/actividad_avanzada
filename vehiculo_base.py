"""
vehiculo_base.py
Clase abstracta base para la analogía de gestión de vehículos eléctricos.
Define el contrato que toda subclase debe cumplir.
"""

from abc import ABC, abstractmethod


class Vehiculo(ABC):
    """
    Clase abstracta que representa un vehículo genérico.

    Define los atributos base comunes a cualquier vehículo y declara
    los métodos abstractos que toda subclase está obligada a implementar.
    """

    def __init__(self, marca: str, modelo: str, anio: int):
        """
        Inicializa los atributos base del vehículo.

        Args:
            marca  (str): Fabricante del vehículo (ej. 'Tesla', 'BYD').
            modelo (str): Nombre del modelo (ej. 'Model 3').
            anio   (int): Año de fabricación.
        """
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    @abstractmethod
    def describir(self) -> str:
        """
        Retorna una descripción técnica del vehículo.
        Toda subclase debe proporcionar su propia implementación.
        """
        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Representación legible del vehículo para ser usada con print().
        Toda subclase debe proporcionar su propia implementación.
        """
        pass


# ─────────────────────────────────────────────
if __name__ == "__main__":
    try:
        v = Vehiculo("Toyota", "Corolla", 2020)
    except TypeError as error:
        print(f"[Correcto] No se puede instanciar ABC directamente: {error}")
