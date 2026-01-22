"""validaciones.py

Funciones de validación y normalización de datos de clientes.
"""

import re

from .excepciones import ValidacionError


# Valida que el texto tenga el formato de correo usuario@dominio
def validar_email(email: str) -> str:
    email = email.strip()
    patron = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    if not re.match(patron, email):
        raise ValidacionError("Email inválido.")
    return email


# Acepta números y símbolos comunes en teléfonos (+, espacios, guiones)
def validar_telefono(telefono: str) -> str:
    telefono = telefono.strip()
    patron = r"^[0-9\s\-\+]{6,}$"
    if not re.match(patron, telefono):
        raise ValidacionError("Teléfono inválido.")
    return telefono


# Dirección mínima para evitar registros vacíos
def validar_direccion(direccion: str) -> str:
    direccion = direccion.strip()
    if len(direccion) < 5:
        raise ValidacionError("Dirección inválida.")
    return direccion


# Normaliza el nombre del tipo de cliente para mapearlo a la clase correcta
def normalizar_tipo_cliente(tipo: str) -> str:
    tipo = tipo.strip().lower()
    equivalencias = {
        "regular": "regular",
        "clienteregular": "regular",
        "premium": "premium",
        "clientepremium": "premium",
        "corporativo": "corporativo",
        "clientecorporativo": "corporativo",
    }
    return equivalencias.get(tipo, tipo)
