"""modulos/excepciones.py

Excepciones personalizadas para controlar errores esperados del sistema.
"""

# Excepción base del proyecto
class GICError(Exception):
    """Error base del sistema."""


# Errores de validación de datos
class ValidacionError(GICError):
    """Dato ingresado no cumple el formato requerido."""


# Errores del menú
class OpcionMenuError(GICError):
    """Opción seleccionada no existe en el menú."""


# Errores de archivos (CSV/TXT/LOG)
class ArchivoError(GICError):
    """Falla al leer o escribir un archivo."""


# Errores del dominio (clientes)
class ClienteExistenteError(GICError):
    """Se intenta registrar un cliente que ya existe."""


class ClienteNoEncontradoError(GICError):
    """No se encuentra el cliente solicitado."""


class TipoClienteInvalidoError(GICError):
    """Tipo de cliente no corresponde a los permitidos."""
