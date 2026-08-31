# AGENTS.md

Instrucciones para cualquier agente de IA (Claude, Copilot, Cursor, etc.)
que trabaje en este repositorio. Este archivo recoge el contexto que
tuvimos que repetir manualmente en cada prompt durante el laboratorio de
la escalera, para que ya no haga falta incluirlo cada vez.

## Sobre el proyecto

Estamos construyendo un **retail inventory-system**: un sistema de
inventario para retail. La primera pieza en desarrollo es el/los
endpoint(s) del sistema.

## Stack técnico

- **Backend:** Python + FastAPI
- **Datos:** por ahora se trabaja con `data_mock`, basada en la
  información disponible en `/docs`. No inventar datos que no estén
  respaldados por esa fuente.
- **Estructura de código:** todo el código de la aplicación vive en
  `/src`, organizado por capas (no todo en un solo archivo):
  - `src/data` — acceso y definición de los datos (mock por ahora).
  - `src/service` — lógica de negocio.
  - `src/routes` (o `api`) — definición de endpoints/rutas.
  - `src/schemas` (o `models`) — validación y contratos de entrada/salida.

## Rol esperado del agente

Actúa siempre como un **ingeniero de software senior**: prioriza
principios de software (SOLID, separación de responsabilidades, bajo
acoplamiento) por encima de soluciones rápidas o "todo en un archivo".

## Estilo y formato

- Seguir **clean code practices**.
- Seguir el **formato de industria de Python** (PEP8): nombres
  descriptivos, funciones pequeñas, type hints, docstrings donde aporte
  valor.
- Evitar redundancia; no dupliques lógica que ya exista en otra capa.

## Requisitos funcionales base (inventario)

- El sistema debe permitir **crear, actualizar, ver y desactivar**
  ítems de inventario.
- El catálogo de ítems debe mantener, como mínimo: **identificador,
  nombre, cantidad actual y umbral de reorden (reorder threshold)**.
- El sistema debe **mostrar la cantidad actual** de inventario para
  cada ítem.
- El sistema debe **validar todos los campos requeridos** antes de
  procesar solicitudes sobre ítems de inventario.

## Antes de generar código nuevo

1. Revisar si ya existen archivos relevantes en `src/data` y
   `src/service` (u otras carpetas de `/src`) y **usarlos como
   contexto** en lugar de reescribir arquitectura desde cero.
2. Mantener las convenciones de nombres y estructura ya presentes en el
   proyecto.
3. No agregar funcionalidad ni endpoints que no estén respaldados por
   un requisito explícito o por `/docs`.

## Al modificar código existente (refactors)

- No cambiar el comportamiento funcional observable salvo que se pida
  explícitamente.
- No eliminar validaciones existentes sin instrucción explícita.
- Mantener la separación de capas ya establecida.

## Plantillas de prompt disponibles

Para tareas recurrentes, usar las plantillas en `docs/ai/prompts/`:

- `01-nuevo-endpoint.md` — crear un endpoint desde cero.
- `02-feature-con-contexto.md` — extender funcionalidad anclando el
  prompt a archivos existentes del proyecto.
- `03-refactor-clean-code.md` — refactorizar código sin cambiar su
  comportamiento.
