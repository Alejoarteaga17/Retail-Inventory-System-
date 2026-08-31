# Prompt: Refactor o mejora de código existente (clean code)

**Cuándo usarlo:** cuando el código ya funciona pero se quiere mejorar su
organización, legibilidad o adherencia a principios de software (SOLID,
separación de capas), sin cambiar el comportamiento funcional.

**Por qué funciona:** aplica la misma lección del laboratorio (rol +
requisitos explícitos + contexto real) pero orientada a mantenimiento en
vez de creación desde cero, acotando el "shall" a restricciones de calidad
en lugar de funcionalidad nueva.

---

## Plantilla

```
Por favor actúa como un ingeniero de software senior. Vamos a refactorizar
el módulo de <nombre del módulo/funcionalidad> del proyecto "<nombre del
sistema>", sin cambiar su comportamiento observable.

Utiliza como contexto los archivos dentro: @<ruta/carpeta 1> y
@<ruta/carpeta 2>

Requisitos para el refactor:

- El sistema debe mantener el mismo comportamiento funcional actual.
- El código debe seguir clean code practices y el formato de industria
  de <lenguaje, ej. Python (PEP8)>.
- Las responsabilidades deben quedar correctamente separadas entre
  <capas del proyecto, ej. rutas, servicios, acceso a datos, esquemas>.
- <Restricción adicional, ej. cobertura de tests, manejo de errores,
  nomenclatura consistente>.

No agregues funcionalidad nueva ni elimines validaciones existentes salvo
que te lo indique explícitamente.
```

## Checklist antes de enviar
- [ ] ¿Dejé claro que es refactor (no debe cambiar el comportamiento)?
- [ ] ¿Referencié los archivos reales a refactorizar (@ruta)?
- [ ] ¿Especifiqué el estándar de estilo/formato esperado?
- [ ] ¿Delimité qué NO debe cambiar (comportamiento, validaciones)?

## Resultado esperado
Mismo comportamiento, mejor separación de responsabilidades y estilo
consistente con las convenciones ya usadas en el proyecto, sin
alucinaciones de features no solicitadas.
