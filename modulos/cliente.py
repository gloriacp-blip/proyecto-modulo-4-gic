"""modulos/cliente.py

Clase base Cliente.

Incluye encapsulamiento (atributos privados) y métodos de acceso
(getters/setters) mediante properties, tal como solicita el PDF.
"""

from __future__ import annotations


class Cliente:
    """Clase base para cualquier tipo de cliente."""

    def __init__(self, nombre: str, email: str, telefono: str, direccion: str):
        # Encapsulamiento: atributos privados.
        self.__nombre = (nombre or "").strip()
        self.__email = (email or "").strip()
        self.__telefono = (telefono or "").strip()
        self.__direccion = (direccion or "").strip()

    # ---- Properties (getters/setters) ----
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = (valor or "").strip()

    @property
    def email(self) -> str:
        return self.__email

    # Email NO debería cambiar (clave de búsqueda), por eso no hay setter.

    @property
    def telefono(self) -> str:
        return self.__telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        self.__telefono = (valor or "").strip()

    @property
    def direccion(self) -> str:
        return self.__direccion

    @direccion.setter
    def direccion(self, valor: str) -> None:
        self.__direccion = (valor or "").strip()

    # ---- Métodos comunes ----
    def tipo(self) -> str:
        """Retorna un nombre de tipo humano para el cliente."""
        return "Base"

    def mostrar_info(self) -> str:
        """Devuelve información del cliente.

        Subclases pueden redefinirlo (polimorfismo) para agregar detalles.
        """
        return (
            f"Nombre: {self.nombre}\n"
            f"Email: {self.email}\n"
            f"Teléfono: {self.telefono}\n"
            f"Dirección: {self.direccion}\n"
            f"Tipo: {self.tipo()}"
        )

    def __str__(self) -> str:
        """Permite imprimir el cliente directamente."""
        return self.mostrar_info()