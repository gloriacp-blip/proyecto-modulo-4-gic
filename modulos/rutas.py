"""modulos/rutas.py

Centraliza rutas del proyecto para que los archivos generados queden
dentro de la carpeta del sistema (datos, reportes y logs).
"""

from __future__ import annotations

from pathlib import Path


# Carpeta raíz del proyecto: .../Proyecto modulo 4/
BASE_DIR = Path(__file__).resolve().parent.parent

# Subcarpetas usadas por el programa
DATA_DIR = BASE_DIR / "datos"
REPORTS_DIR = BASE_DIR / "reportes"
LOGS_DIR = BASE_DIR / "logs"


def dir_datos() -> Path:
    """Crea (si falta) y devuelve la carpeta /datos."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR


def dir_reportes() -> Path:
    """Crea (si falta) y devuelve la carpeta /reportes."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    return REPORTS_DIR


def dir_logs() -> Path:
    """Crea (si falta) y devuelve la carpeta /logs."""
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    return LOGS_DIR


def ruta_datos(nombre_archivo: str) -> Path:
    """Devuelve una ruta dentro de /datos."""
    return dir_datos() / nombre_archivo


def ruta_reporte(nombre_archivo: str) -> Path:
    """Devuelve una ruta dentro de /reportes."""
    return dir_reportes() / nombre_archivo


def ruta_log(nombre_archivo: str) -> Path:
    """Devuelve una ruta dentro de /logs."""
    return dir_logs() / nombre_archivo
