# Prompt: Creación de un nuevo endpoint

**Cuándo usarlo:** al iniciar un módulo o feature desde cero, cuando todavía no existe código previo con el cual anclar la generación (equivalente al Prompt 3 del laboratorio).

**Por qué funciona:** define rol, stack, ubicación del código y requisitos funcionales explícitos en formato "shall", eliminando la ambigüedad que provoca alucinaciones.

---

## Plantilla

```
Nosotros queremos hacer un/una "<nombre del sistema>". Nuestro objetivo actual
es crear el endpoint de <funcionalidad> con <framework> con una data_mock
basada en la información de <fuente de datos/docs>. Esto va a ir en el
<ruta del proyecto, ej. /src> folder y ya tú te enfocas en las mejores
prácticas y principios de software, separándolos correctamente.

Por favor actúa como un ingeniero de software senior y utiliza estos
requisitos para crear el código:

- <Requisito funcional 1, en formato "The system shall...">
- <Requisito funcional 2>
- <Requisito funcional 3>
- <Requisito funcional 4>

Para el formato de los archivos por favor utiliza clean code practices,
y el formato de industria de <lenguaje, ej. Python (PEP8)>.
```

## Checklist antes de enviar
- [ ] ¿Definí el rol/persona ("ingeniero de software senior")?
- [ ] ¿Los requisitos están escritos como especificaciones verificables (shall)?
- [ ] ¿Indiqué el stack técnico y la carpeta destino del código?
- [ ] ¿Especifiqué el estándar de formato/estilo esperado?

## Resultado esperado
Código separado en capas (rutas, servicios, modelos/esquemas, datos mock),
con validaciones explícitas y sin necesidad de inventar arquitectura no
solicitada.
