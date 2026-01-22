"""modulos/archivos.py

Manejo de archivos del proyecto (CSV/TXT/log).

Requisitos del PDF:
- Exportar clientes a datos/clientes.csv
- Importar clientes desde datos/clientes_entrada.csv
- Generar reporte reportes/resumen.txt
- Registrar actividad en logs/app.log

Este módulo usa rutas relativas al proyecto para que los archivos
queden SIEMPRE dentro de la carpeta del trabajo.
"""

from __future__ import annotations

import csv
from pathlib import Path

from modulos.excepciones import ArchivoError
from modulos.logger_config import obtener_logger
from modulos.rutas import dir_datos, dir_reportes


logger = obtener_logger()


def exportar_csv(gestor) -> Path:
    """Exporta los clientes registrados a datos/clientes.csv."""
    ruta_csv = dir_datos() / "clientes.csv"

    try:
        with open(ruta_csv, mode="w", newline="", encoding="utf-8") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(["nombre", "email", "telefono", "direccion", "tipo"])

            for cliente in gestor.clientes:
                escritor.writerow([
                    cliente.nombre,
                    cliente.email,
                    cliente.telefono,
                    cliente.direccion,
                    cliente.tipo(),
                ])

        logger.info("EXPORT CSV -> %s (registros=%s)", ruta_csv, len(gestor.clientes))
        return ruta_csv

    except Exception as exc:
        logger.error("ERROR exportando CSV: %s", exc)
        raise ArchivoError(f"No se pudo exportar el CSV: {exc}")


def importar_csv(gestor, archivo_entrada: Path | None = None) -> int:
    """Importa clientes desde datos/clientes_entrada.csv.

    Retorna la cantidad de clientes agregados (no duplicados).
    """
    ruta_csv = archivo_entrada or (dir_datos() / "clientes_entrada.csv")

    if not ruta_csv.exists():
        raise ArchivoError(f"No existe el archivo de entrada: {ruta_csv}")

    agregados = 0
    try:
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            # Soportar CSV con encabezados en mayúsculas/minúsculas.
            
            for fila in lector:
                fila_norm = {str(k).strip().lower(): (v or "").strip() for k, v in fila.items()}

                # Aceptar valores como "ClientePremium" o "Premium".
                tipo_raw = fila_norm.get("tipo", "")
                tipo = tipo_raw.replace("Cliente", "").strip().lower()

                cliente = gestor._crear_cliente_por_tipo(
                    tipo,
                    fila_norm.get("nombre", ""),
                    fila_norm.get("email", ""),
                    fila_norm.get("telefono", ""),
                    fila_norm.get("direccion", ""),
                )

                # Evitar duplicados por email
                if gestor.buscar_por_email(cliente.email):
                    logger.warning("DUPLICADO en import: email=%s", cliente.email)
                    continue

                gestor.clientes.append(cliente)
                agregados += 1

        logger.info("IMPORT CSV <- %s (agregados=%s)", ruta_csv, agregados)
        return agregados

    except Exception as exc:
        logger.error("ERROR importando CSV: %s", exc)
        raise ArchivoError(f"No se pudo importar el CSV: {exc}")


def generar_reporte(gestor) -> Path:
    """Genera reportes/resumen.txt con conteos y listado."""
    ruta_txt = dir_reportes() / "resumen.txt"

    try:
        with open(ruta_txt, mode="w", encoding="utf-8") as archivo:
            archivo.write("RESUMEN DE CLIENTES\n")
            archivo.write("===================\n\n")

            archivo.write(f"Total de clientes: {len(gestor.clientes)}\n\n")

            if not gestor.clientes:
                archivo.write("No hay clientes registrados.\n")
            else:
                archivo.write("LISTADO\n")
                archivo.write("-------\n")
                for i, cliente in enumerate(gestor.clientes, start=1):
                    archivo.write(f"\nCliente #{i}\n")
                    archivo.write(cliente.mostrar_info())
                    archivo.write("\n")

                archivo.write("\n\nRESUMEN POR TIPO\n")
                archivo.write("----------------\n")

                resumen = gestor.contar_por_tipo()
                for tipo, cantidad in resumen.items():
                    archivo.write(f"{tipo}: {cantidad}\n")

        logger.info("REPORTE generado -> %s", ruta_txt)
        return ruta_txt

    except Exception as exc:
        logger.error("ERROR generando reporte: %s", exc)
        raise ArchivoError(f"No se pudo generar el reporte: {exc}")
