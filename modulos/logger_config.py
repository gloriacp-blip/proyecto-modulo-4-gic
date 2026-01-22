"""
logger_config.py

Configuración del logger del proyecto.
- Guarda INFO y WARNING en archivo log
- En consola muestra SOLO ERRORES 
"""

import logging
from logging.handlers import RotatingFileHandler

from .rutas import ruta_log


def configurar_logger(nombre: str = "GIC") -> logging.Logger:
    """Crea y retorna un logger configurado."""
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    # Evitar duplicar handlers
    if logger.handlers:
        return logger

    # --- Handler a archivo (TODO queda registrado) ---
    file_handler = RotatingFileHandler(
        ruta_log("app.log"),
        maxBytes=300_000,
        backupCount=3,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.INFO)

    # --- Handler a consola (SOLO ERRORES) ---
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.ERROR)

    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formato)
    console_handler.setFormatter(formato)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def obtener_logger(nombre: str = "GIC") -> logging.Logger:
    """Devuelve el logger del sistema."""
    return configurar_logger(nombre)
