"""modulos/gestor_clientes.py

GestorClientes: administra la colección de clientes (CRUD).

Cumple con:
- POO con encapsulación + herencia + polimorfismo.
- Validaciones + excepciones personalizadas.
- Registro en log de altas/bajas/errores.
"""

from __future__ import annotations

from typing import Optional

from modulos.excepciones import (
    ClienteExistenteError,
    ClienteNoEncontradoError,
    TipoClienteInvalidoError,
)
from modulos.logger_config import obtener_logger
from modulos.validaciones import validar_direccion, validar_email, validar_telefono


class GestorClientes:
    """Clase encargada de administrar clientes del sistema."""

    def __init__(self):
        # Colección interna de clientes.
        self.clientes = []
        self.logger = obtener_logger()

    # -------- Utilidades --------
    def buscar_por_email(self, email: str) -> Optional[object]:
        """Retorna el cliente que coincide con el email o None."""
        e = (email or "").strip().lower()
        for c in self.clientes:
            if c.email.lower() == e:
                return c
        return None

    def agregar_cliente(self, cliente) -> None:
        """Agrega un cliente evitando duplicados por email."""
        if self.buscar_por_email(cliente.email):
            raise ClienteExistenteError(f"Ya existe un cliente con email: {cliente.email}")
        self.clientes.append(cliente)
        self.logger.info("ALTA cliente email=%s tipo=%s", cliente.email, cliente.tipo())

    def _crear_cliente_por_tipo(self, tipo: str, nombre: str, email: str, telefono: str, direccion: str):
        """Crea un objeto cliente según el tipo indicado."""
        t = (tipo or "").strip().lower()

        if t == "regular":
            from modulos.cliente_regular import ClienteRegular

            return ClienteRegular(nombre, email, telefono, direccion)

        if t == "premium":
            from modulos.cliente_premium import ClientePremium

            return ClientePremium(nombre, email, telefono, direccion)

        if t == "corporativo":
            from modulos.cliente_corporativo import ClienteCorporativo

            return ClienteCorporativo(nombre, email, telefono, direccion)

        raise TipoClienteInvalidoError(
            "Tipo de cliente inválido. Use: regular / premium / corporativo"
        )

    def contar_por_tipo(self):
        """Retorna un dict con la cantidad de clientes por tipo."""
        resumen = {}
        for cliente in self.clientes:
            resumen[cliente.tipo()] = resumen.get(cliente.tipo(), 0) + 1
        return resumen

    # -------- CRUD (Consola) --------
    def crear_cliente(self) -> None:
        """Solicita datos por consola y crea un cliente validado."""
        try:
            nombre = input("Ingrese nombre: ").strip()
            email = input("Ingrese email: ").strip()
            telefono = input("Ingrese teléfono: ").strip()
            direccion = input("Ingrese dirección: ").strip()

            # Validaciones (levantan excepciones personalizadas)
            validar_email(email)
            validar_telefono(telefono)
            validar_direccion(direccion)

            tipo = input("Tipo de cliente (regular / premium / corporativo): ").strip().lower()
            cliente = self._crear_cliente_por_tipo(tipo, nombre, email, telefono, direccion)

            self.agregar_cliente(cliente)
            print("Cliente creado correctamente.")

        except Exception as exc:  # manejo robusto en consola
            self.logger.error("ERROR al crear cliente: %s", exc)
            print(f"Error: {exc}")

    def listar_clientes(self) -> None:
        """Muestra todos los clientes registrados."""
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        for i, cliente in enumerate(self.clientes, start=1):
            print(f"\nCliente #{i}")
            print(cliente.mostrar_info())

    def editar_cliente(self) -> None:
        """Modifica nombre/teléfono/dirección y, si se desea, el tipo."""
        try:
            email = input("Ingrese el email del cliente a editar: ").strip()
            validar_email(email)

            cliente_actual = self.buscar_por_email(email)
            if not cliente_actual:
                raise ClienteNoEncontradoError("Cliente no encontrado.")

            print("\nCliente encontrado:")
            print(cliente_actual.mostrar_info())

            nuevo_nombre = input("Nuevo nombre (Enter para mantener): ").strip()
            nuevo_telefono = input("Nuevo teléfono (Enter para mantener): ").strip()
            nueva_direccion = input("Nueva dirección (Enter para mantener): ").strip()

            print("\nTipos permitidos: regular / premium / corporativo")
            nuevo_tipo = input("Nuevo tipo (Enter para mantener): ").strip().lower()

            # Mantener valores actuales si se omite.
            nombre = nuevo_nombre if nuevo_nombre else cliente_actual.nombre
            telefono = cliente_actual.telefono
            direccion = nueva_direccion if nueva_direccion else cliente_actual.direccion
            tipo = nuevo_tipo if nuevo_tipo else cliente_actual.tipo().lower()

            if nuevo_telefono:
                validar_telefono(nuevo_telefono)
                telefono = nuevo_telefono

            if nueva_direccion:
                validar_direccion(nueva_direccion)

            # Si cambia el tipo, se crea un nuevo objeto de la subclase correspondiente.
            cliente_editado = self._crear_cliente_por_tipo(tipo, nombre, cliente_actual.email, telefono, direccion)

            # Reemplazar en la lista
            for idx, c in enumerate(self.clientes):
                if c.email.lower() == cliente_actual.email.lower():
                    self.clientes[idx] = cliente_editado
                    break

            self.logger.info("UPDATE cliente email=%s tipo=%s", cliente_editado.email, cliente_editado.tipo())
            print("Cliente actualizado correctamente.")

        except Exception as exc:
            self.logger.error("ERROR al editar cliente: %s", exc)
            print(f"Error: {exc}")

    def eliminar_cliente(self) -> None:
        """Elimina un cliente según su email."""
        try:
            email = input("Ingrese email del cliente a eliminar: ").strip()
            validar_email(email)

            cliente = self.buscar_por_email(email)
            if not cliente:
                raise ClienteNoEncontradoError("Cliente no encontrado.")

            self.clientes = [c for c in self.clientes if c.email.lower() != email.lower()]
            self.logger.info("BAJA cliente email=%s tipo=%s", cliente.email, cliente.tipo())
            print("Cliente eliminado correctamente.")

        except Exception as exc:
            self.logger.error("ERROR al eliminar cliente: %s", exc)
            print(f"Error: {exc}")
