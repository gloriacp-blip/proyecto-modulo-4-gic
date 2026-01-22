"""main.py

Gestor Inteligente de Clientes (GIC) - Interfaz por consola.

El menú implementa CRUD, importación/exportación CSV, generación de
reporte TXT y registro de logs.
"""

from __future__ import annotations

from modulos.archivos import exportar_csv, generar_reporte, importar_csv
from modulos.excepciones import ArchivoError
from modulos.gestor_clientes import GestorClientes


def mostrar_menu() -> None:
    print("\n======================================")
    print("   GESTOR INTELIGENTE DE CLIENTES")
    print("======================================")
    print("\nTipos de clientes permitidos: regular / premium / corporativo\n")

    print("1. Crear cliente")
    print("2. Cargar clientes desde CSV (datos/clientes_entrada.csv)")
    print("3. Guardar clientes a CSV (datos/clientes.csv)")
    print("4. Listar clientes")
    print("5. Editar cliente")
    print("6. Eliminar cliente")
    print("7. Generar reporte (reportes/resumen.txt)")
    print("8. Salir")


def menu() -> None:
    gestor = GestorClientes()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            gestor.crear_cliente()

        elif opcion == "2":
            try:
                agregados = importar_csv(gestor)
                print(f"Importación finalizada. Clientes agregados: {agregados}")
            except ArchivoError as exc:
                print(f"Error: {exc}")

        elif opcion == "3":
            try:
                exportar_csv(gestor)
                print("Clientes guardados correctamente en datos/clientes.csv")
            except ArchivoError as exc:
                print(f"Error: {exc}")

        elif opcion == "4":
            gestor.listar_clientes()

        elif opcion == "5":
            gestor.editar_cliente()

        elif opcion == "6":
            gestor.eliminar_cliente()

        elif opcion == "7":
            try:
                generar_reporte(gestor)
                print("Reporte generado correctamente en reportes/resumen.txt")
            except ArchivoError as exc:
                print(f"Error: {exc}")

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
