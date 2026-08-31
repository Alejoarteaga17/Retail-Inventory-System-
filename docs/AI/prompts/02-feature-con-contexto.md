# Prompt: Agregar feature usando código existente como contexto

**Cuándo usarlo:** cuando ya existe una base de código (carpetas, módulos, esquemas) y se quiere extender o completar funcionalidad sobre ella (equivalente al Prompt 4 del laboratorio, el de mejor resultado: 8/8, 1 alucinación).

**Por qué funciona:** anclar la generación a archivos reales del proyecto evita que el modelo infiera arquitectura, nombres o convenciones por su cuenta.

---

## Plantilla

```
Nosotros queremos hacer un/una "<nombre del sistema>". Nuestro objetivo
actual es crear/extender el endpoint de <funcionalidad> con <framework>
con una data_mock basada en la información de <fuente de datos/docs>.
Esto va a ir en el <ruta del proyecto> folder y ya tú te enfocas en las
mejores prácticas y principios de software, separándolos correctamente.

Por favor actúa como un ingeniero de software senior y utiliza estos
requisitos para crear el código:

- <Requisito funcional 1>
- <Requisito funcional 2>
- <Requisito funcional 3>
- <Requisito funcional 4>

Para el formato de los archivos por favor utiliza clean code practices,
y el formato de industria de <lenguaje>.

Ahora utiliza como contexto los archivos dentro: @<ruta/carpeta 1> y
@<ruta/carpeta 2>
```

## Checklist antes de enviar
- [ ] ¿Referencié explícitamente las carpetas/archivos existentes (@ruta)?
- [ ] ¿Esas rutas reflejan la arquitectura real del proyecto (data, service, etc.)?
- [ ] ¿Mantuve el mismo rol y los mismos requisitos que en la especificación base?
- [ ] ¿El nuevo código debe seguir convenciones ya presentes en esos archivos (naming, estructura)?

## Resultado esperado
Código consistente con los patrones ya establecidos en el proyecto
(mismos nombres de capas, mismo estilo de validación, mínima o nula
alucinación de arquitectura nueva).
