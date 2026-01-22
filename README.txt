Gestor Inteligente de Clientes (GIC) – Módulo 4

Proyecto desarrollado en Python 3 que permite la gestión de clientes mediante una
interfaz por consola, aplicando Programación Orientada a Objetos, manejo de archivos,
validaciones y control de errores.

FUNCIONALIDADES PRINCIPALES

- Crear, listar, editar y eliminar clientes.
- Manejo de distintos tipos de clientes:
  - Regular
  - Premium
  - Corporativo
- Importación de clientes desde archivo CSV.
- Exportación de clientes a archivo CSV.
- Generación de reporte en formato TXT.
- Registro de eventos mediante archivo de log.

CÓMO EJECUTAR EL PROYECTO

1) Abrir una terminal en la carpeta raíz del proyecto.
2) Ejecutar el siguiente comando:

   python main.py

ESTRUCTURA Y RUTAS DE ARCHIVOS

Todos los archivos generados quedan dentro del proyecto:

- Importar clientes:
  datos/clientes_entrada.csv

- Exportar clientes:
  datos/clientes.csv

- Reporte generado:
  reportes/resumen.txt

- Registro de eventos (log):
  logs/app.log

CONSIDERACIONES IMPORTANTES

- El email se utiliza como identificador único del cliente para evitar duplicados.
- Los tipos de cliente válidos son:
  regular / premium / corporativo
- El sistema incluye validaciones de datos y manejo de errores mediante
  excepciones personalizadas.

DOCUMENTACIÓN INCLUIDA

El proyecto incluye:
- Documentación técnica.
- Informe de validación.
- Diagrama UML de clases.
- Presentación final del proyecto.

ESTADO DEL PROYECTO

Proyecto funcional y completo, desarrollado según los requisitos del Módulo 4.

AUTOR

Gloria Alejandra
