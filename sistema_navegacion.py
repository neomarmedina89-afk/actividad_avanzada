
from typing import Optional

class SistemaNavegacion:
    def __init__(self, version_mapa: str = "2025.1", modo_eco: bool = True):
        self.version_mapa = version_mapa
        self.modo_eco = modo_eco
        self._ruta_activa: Optional[str] = None

    def iniciar_ruta(self, destino: str) -> str:
       
        self._ruta_activa = destino
        modo = "ECO" if self.modo_eco else "NORMAL"
        return (
            f"[GPS] Ruta iniciada -> {destino} | "
            f"Modo: {modo} | Mapa v{self.version_mapa}"
        )

    def cancelar_ruta(self) -> str:
        if self._ruta_activa:
            mensaje = f"[GPS] Ruta hacia '{self._ruta_activa}' cancelada."
            self._ruta_activa = None
            return mensaje
        return "[GPS] No hay ninguna ruta activa."

    def estado_navegacion(self) -> str:
        ruta = self._ruta_activa if self._ruta_activa else "Ninguna"
        return f"[GPS] Mapa v{self.version_mapa} | Ruta activa: {ruta}"


if __name__ == "__main__":
    nav = SistemaNavegacion(version_mapa="2025.1", modo_eco=True)
    print(nav.iniciar_ruta("Riohacha, La Guajira"))
    print(nav.estado_navegacion())
    print(nav.cancelar_ruta())
    print(nav.cancelar_ruta())  
