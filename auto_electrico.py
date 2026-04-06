
import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from vehiculo_base import Vehiculo
from sistema_navegacion import SistemaNavegacion
from sistema_bateria import SistemaBateria


class AutoElectrico(Vehiculo, SistemaNavegacion, SistemaBateria):
    def __init__(
        self,
        marca: str,
        modelo: str,
        anio: int,
        capacidad_kwh: float,
        autonomia_km: float,
        velocidad_max: float,
        nivel_carga: float = 100.0,
        version_mapa: str = "2025.1",
        modo_eco: bool = True,
        celdas: int = 96,
    ):
  
        Vehiculo.__init__(self, marca, modelo, anio)
        SistemaNavegacion.__init__(self, version_mapa, modo_eco)
        SistemaBateria.__init__(self, capacidad_kwh, celdas)

        # Atributos propios encapsulados
        self._nivel_carga: float = 0.0       # Se asigna a través del setter
        self.__autonomia_km: float = 0.0     # Privado, setter con validación
        self.__velocidad_max: float = 0.0    # Privado, setter con validación

        # Usar setters para garantizar validación desde la construcción
        self.nivel_carga = nivel_carga
        self.autonomia_km = autonomia_km
        self.velocidad_max = velocidad_max

    def describir(self) -> str:
        return (
            f"[AutoEléctrico] {self.marca} {self.modelo} ({self.anio}) | "
            f"Batería: {self.capacidad_kwh} kWh | "
            f"Autonomía: {self.__autonomia_km} km | "
            f"Vel. máx: {self.__velocidad_max} km/h | "
            f"Carga actual: {self._nivel_carga:.1f} %"
        )

    def __str__(self) -> str:
        return (
            f"[{self.marca} {self.modelo} {self.anio}] "
            f"Carga: {self._nivel_carga:.1f} % | "
            f"Autonomia: {self.__autonomia_km} km"
        )


    @property
    def nivel_carga(self) -> float:
        return self._nivel_carga

    @nivel_carga.setter
    def nivel_carga(self, valor: float) -> None:
        if not (0.0 <= valor <= 100.0):
            raise ValueError(
                f"El nivel de carga debe estar entre 0 y 100 %, "
                f"se recibió: {valor}"
            )
        self._nivel_carga = valor

    @property
    def autonomia_km(self) -> float:
        """Retorna la autonomía máxima en kilómetros."""
        return self.__autonomia_km

    @autonomia_km.setter
    def autonomia_km(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError(
                f"La autonomía debe ser un valor positivo en km, "
                f"se recibió: {valor}"
            )
        self.__autonomia_km = valor


    @property
    def velocidad_max(self) -> float:
        """Retorna la velocidad máxima de diseño en km/h."""
        return self.__velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor: float) -> None:
        if not (1 < valor <= 500):
            raise ValueError(
                f"La velocidad máxima debe estar entre 1 y 500 km/h, "
                f"se recibió: {valor}"
            )
        self.__velocidad_max = valor


    def calcular_autonomia_actual(self) -> float:
        return round(self.__autonomia_km * (self._nivel_carga / 100.0), 2)

    def cargar(self, porcentaje: float) -> str:
        nuevo_nivel = min(self._nivel_carga + porcentaje, 100.0)
        self.nivel_carga = nuevo_nivel
        self.registrar_ciclo_carga()
        return (
            f"[Carga] {self.marca} {self.modelo} -> "
            f"Nivel: {self._nivel_carga:.1f} % | "
            f"Autonomía disponible: {self.calcular_autonomia_actual()} km"
        )


if __name__ == "__main__":
    print("=" * 65)
    print("  SISTEMA DE GESTION DE VEHICULOS ELECTRICOS")
    print("=" * 65)

    auto1 = AutoElectrico(
        marca="Tesla", modelo="Model 3", anio=2024,
        capacidad_kwh=75.0, autonomia_km=560.0, velocidad_max=250.0,
        nivel_carga=85.0, modo_eco=True,
    )

    auto2 = AutoElectrico(
        marca="BYD", modelo="Atto 3", anio=2023,
        capacidad_kwh=60.5, autonomia_km=480.0, velocidad_max=185.0,
        nivel_carga=60.0, modo_eco=False,
    )

    auto3 = AutoElectrico(
        marca="Rivian", modelo="R1T", anio=2025,
        capacidad_kwh=135.0, autonomia_km=800.0, velocidad_max=200.0,
        nivel_carga=40.0, modo_eco=True,
    )

    vehiculos = [auto1, auto2, auto3]

    print("\n[POLIMORFISMO] __str__ y describir()\n")
    for v in vehiculos:
        print(str(v))           
        print(v.describir())    
        print("-" * 65)

    print("\n[ENCAPSULAMIENTO] Lectura via @property\n")
    print(f"  auto1.nivel_carga  = {auto1.nivel_carga} %")
    print(f"  auto2.nivel_carga  = {auto2.nivel_carga} %")
    print(f"  auto3.nivel_carga  = {auto3.nivel_carga} %")

    print("\n[ENCAPSULAMIENTO] Modificacion via setter\n")
    print(f"  [Antes]  auto1.nivel_carga = {auto1.nivel_carga} %")
    auto1.nivel_carga = 95.0
    print(f"  [Después] auto1.nivel_carga = {auto1.nivel_carga} %")

    print(f"\n  [Antes]  auto2.autonomia_km = {auto2.autonomia_km} km")
    auto2.autonomia_km = 500.0
    print(f"  [Después] auto2.autonomia_km = {auto2.autonomia_km} km")

    print("\n[VALIDACION] Setter rechaza valores invalidos\n")
    try:
        auto3.nivel_carga = 110.0  


    except ValueError as e:
        print(f"  [Error esperado] {e}")

    try:
        auto1.autonomia_km = -50    
    except ValueError as e:
        print(f"  [Error esperado] {e}")

    try:
        auto2.velocidad_max = 600   
    except ValueError as e:
        print(f"  [Error esperado] {e}")

    print("\n[MODULOS DE SOPORTE] GPS y Bateria\n")
    print(auto1.iniciar_ruta("Riohacha, La Guajira"))
    print(auto1.estado_navegacion())
    print(auto1.cancelar_ruta())

    print()
    print(auto2.cargar(25.0))
    print(auto2.salud_bateria())
    print(auto2.verificar_temperatura(42.0))

    print()
    print(auto3.info_bateria())
    print(auto3.calcular_autonomia_actual(), "km disponibles")

    print("\n" + "=" * 65)
    print("  FIN DE LA DEMOSTRACIÓN")
    print("=" * 65)
