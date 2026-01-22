"""modulos/cliente_regular.py

ClienteRegular: subclase de Cliente.

Incluye polimorfismo redefiniendo mostrar_info() y un método específico
beneficio_exclusivo().
"""

from __future__ import annotations

from modulos.cliente import Cliente


class ClienteRegular(Cliente):
    def tipo(self) -> str:
        return "Regular"

    def beneficio_exclusivo(self) -> str:
        # Método específico de la subclase.
        return "Descuento base del 5% en servicios seleccionados."

    def mostrar_info(self) -> str:
        # Polimorfismo: agrega el beneficio al info base.
        return f"{super().mostrar_info()}\nBeneficio: {self.beneficio_exclusivo()}"
