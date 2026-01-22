"""modulos/cliente_corporativo.py

Define el tipo de cliente Corporativo como subclase de Cliente (herencia).
Sobrescribe métodos para demostrar polimorfismo.
"""

from __future__ import annotations

from modulos.cliente import Cliente


class ClienteCorporativo(Cliente):
    # Retorna el nombre del tipo para mostrarlo en listados y reportes
    def tipo(self) -> str:
        return "Corporativo"

    # Beneficio específico del tipo (se usa en el reporte)
    def beneficio_exclusivo(self) -> str:
        return "Ejecutivo dedicado y facturación mensual."

    # Sobrescritura: agrega información extra manteniendo lo base
    def mostrar_info(self) -> str:
        return f"{super().mostrar_info()}\nBeneficio: {self.beneficio_exclusivo()}"
