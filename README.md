# Nivelación Python — Gestión de Vehículos Eléctricos

## Descripción de la analogía

El proyecto modela un **sistema de gestión de vehículos eléctricos** compuesto por cuatro módulos:

| Archivo | Rol | Descripción |
|---|---|---|
| `vehiculo_base.py` | Clase abstracta | Define el contrato base con dos métodos abstractos |
| `sistema_navegacion.py` | Clase de soporte | GPS: rutas, modo ECO, versiones de mapa |
| `sistema_bateria.py` | Clase de soporte | BMS: ciclos de carga, salud y temperatura |
| `auto_electrico.py` | Clase final | Herencia múltiple + encapsulamiento + demostración completa |

---

## Requisitos

- **Python 3.10+** (se usa la sintaxis `str | None` para uniones de tipos)
- Sin dependencias externas — solo módulos de la librería estándar (`abc`)

---

## Cómo ejecutar cada ejercicio

> Todos los comandos deben ejecutarse desde la carpeta `nivelacion_python/`.

```bash
# 1. Clase abstracta base (muestra que no se puede instanciar directamente)
python vehiculo_base.py

# 2. Sistema de navegación GPS (prueba de métodos propios)
python sistema_navegacion.py

# 3. Sistema de gestión de batería — BMS (prueba de métodos propios)
python sistema_bateria.py

# 4. Demostración completa: herencia múltiple, encapsulamiento y polimorfismo
python auto_electrico.py
```

---

## Conceptos POO aplicados

### 1. Clase abstracta (`vehiculo_base.py`)
- Usa `ABC` y `@abstractmethod` del módulo `abc`.
- Declara `describir()` y `__str__()` como métodos abstractos obligatorios.

### 2. Clases de soporte independientes
- `SistemaNavegacion` — gestiona rutas GPS y modo ECO.
- `SistemaBateria` — monitorea ciclos de carga, salud y temperatura.

### 3. Herencia múltiple (`auto_electrico.py`)
```
AutoElectrico
├── Vehiculo          (ABC)
├── SistemaNavegacion
└── SistemaBateria
```
- El constructor llama explícitamente a cada `__init__` padre.

### 4. Encapsulamiento
| Atributo | Tipo | Acceso |
|---|---|---|
| `_nivel_carga` | Protegido | `@property` + setter con rango `[0, 100]` |
| `__autonomia_km` | Privado | `@property` + setter con valor `> 0` |
| `__velocidad_max` | Privado | `@property` + setter con rango `(1, 500]` |

### 5. Polimorfismo
Los métodos `__str__()` y `describir()` se invocan de forma polimórfica
sobre una lista de instancias de `AutoElectrico`.

---

## Convención de nombres utilizada

**`snake_case`** en todo el proyecto (variables, funciones, archivos).

---

## Estructura del repositorio

```
nivelacion_python/
├── vehiculo_base.py        # Punto 1 — clase abstracta
├── sistema_navegacion.py   # Punto 2 — clase de soporte GPS
├── sistema_bateria.py      # Punto 2 — clase de soporte BMS
├── auto_electrico.py       # Puntos 3, 4 y 5 — clase final + pruebas
└── README.md               # Este archivo
```
