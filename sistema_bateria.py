
class SistemaBateria:

    TEMPERATURA_MAX_C = 45.0  
    TEMPERATURA_MIN_C = -10.0 

    def __init__(self, capacidad_kwh: float, celdas: int = 96):
       
        self.capacidad_kwh = capacidad_kwh
        self.celdas = celdas
        self._ciclos_carga: int = 0

    def registrar_ciclo_carga(self) -> str:
        self._ciclos_carga += 1
        return f"[BMS] Ciclo #{self._ciclos_carga} registrado."

    def salud_bateria(self) -> str:
        degradacion = min(self._ciclos_carga * 0.02, 20.0) 
        salud = 100.0 - degradacion
        return (
            f"[BMS] Salud de batería: {salud:.1f} % "
            f"({self._ciclos_carga} ciclos completados)"
        )

    def verificar_temperatura(self, temp_actual: float) -> str:
        if temp_actual > self.TEMPERATURA_MAX_C:
            return (
                f"[BMS] ALERTA: {temp_actual}°C supera el máximo "
                f"({self.TEMPERATURA_MAX_C}°C). Activando enfriamiento."
            )
        if temp_actual < self.TEMPERATURA_MIN_C:
            return (
                f"[BMS] ALERTA:{temp_actual}°C bajo el mínimo "
                f"({self.TEMPERATURA_MIN_C}°C). Activando calefacción."
            )
        return f"[BMS]Temperatura normal:{temp_actual}°C"

    def info_bateria(self) -> str:
        return (
            f"[BMS] Capacidad: {self.capacidad_kwh} kWh | "
            f"Celdas: {self.celdas} | Ciclos: {self._ciclos_carga}"
        )

if __name__ == "__main__":
    bms = SistemaBateria(capacidad_kwh=75.0, celdas=96)
    print(bms.info_bateria())
    print(bms.registrar_ciclo_carga())
    print(bms.registrar_ciclo_carga())
    print(bms.salud_bateria())
    print(bms.verificar_temperatura(38.0))
    print(bms.verificar_temperatura(50.0))
    print(bms.verificar_temperatura(-15.0))
